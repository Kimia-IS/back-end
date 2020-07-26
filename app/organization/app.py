from flask import request, jsonify, Blueprint
from organization.models import organization, get_all_organizations, edit_organization, delete_organization, get_organization_byID
import os

organization_blueprint = Blueprint('organization_blueprint', __name__)
# Allowed file extension
ALLOWED_EXTENSIONS = {'docx', 'pdf', 'jpg', 'jpeg'}


def allowed_file(filename):
    # Return boolean based on the ALLOWED_EXTENSION list
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@organization_blueprint.route('/organizations', methods=['GET', 'POST', 'PUT', 'DELETE'])
def process_organizations():
    # check the request method
    # if method == GET
    if request.method == 'GET':

        # check is there parameter ID
        if request.args.get('id') is None:
            return jsonify(get_all_organizations())
        return jsonify(get_organization_byID(request.args.get('id')))

    # if method == POST
    elif request.method == 'POST':
        # get data from request json
        lecturer_nip = request.form['lecturer_nip']
        organization_name = request.form['organization_name']
        position = request.form['position']
        year = request.form['year']

        # get file data into a list
        files = request.files.getlist('organization_files')

        # loop over the file list
        filepath = []
        for file in files:

            # if the extension not allowed
            if not allowed_file(file.filename):
                ret = {
                    'status': 200,
                    'message': 'File Extension must be PDF or DOCX!'
                }
                return jsonify(ret)

            # check the directory to save the file
            if not os.path.exists('datas/files/organizations'):
                # make a directory if it doesn't exist
                os.makedirs('datas/files/organizations')

            filename = lecturer_nip + '_' + file.filename.replace(' ', '_')

            # save file to /datas/files/finalTasks
            file.save(os.path.join('datas/files/organizations', filename))

            # append the path to filepath list
            filepath.append('datas/files/organizations/' + filename)

        # build new organization method
        new_organization = organization(lecturer_nip=lecturer_nip, organization_name=organization_name, position=position, year=year, filepath=str(filepath))

        # call save method from organization module
        res = new_organization.save()
        return jsonify(res)

    # if method == PUT
    elif request.method == 'PUT':
        # get id from the query string
        id = request.args.get('id')

        # call the edit method from organization module
        res = edit_organization(id, request.form)
        return jsonify(res)

    # if method == DELETE
    elif request.method == 'DELETE':

        # get id from the query string
        id = request.args.get('id')
        return jsonify(delete_organization(id))

    # if methods aren't recognized
    else:
        res = {
            'status': 500,
            'message': 'Sorry, your request method is not recognized!'
        }
        return jsonify(res)
