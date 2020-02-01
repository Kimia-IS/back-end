from flask import request, jsonify, Blueprint
from socres.models import social_responsibility, get_all_socres, get_socres_byID, edit_socres, delete_socres
import os

socres_blueprint = Blueprint('socres_blueprint', __name__)
# Allowed file extension
ALLOWED_EXTENSIONS = {'docx', 'pdf'}


def allowed_file(filename):
    # Return boolean based on the ALLOWED_EXTENSION list
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@socres_blueprint.route('/socres', methods=['GET', 'POST', 'PUT', 'DELETE'])
def process_socres():
    if request.method == 'GET':
        if request.args.get('id'):
            return jsonify(get_socres_byID(request.args.get('id')))
        return jsonify(get_all_socres())
    elif request.method == 'POST':
        if request.files:
            # get data from request form
            lecturer_nip = request.json['lecturer_nip']
            title = request.json['title']
            investor = request.json['investor']
            year = request.json['year']
            amount = request.json['amount']
            position = request.json['position']
            other_parties = request.json.getlist('other_parties')

            # get file data into a list
            files = request.files.getlist('socres_files')

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
                if not os.path.exists('datas/files/socres'):
                    # make a directory if it doesn't exist
                    os.makedirs('datas/files/socres')

                # save file to /datas/files/form
                file.save(os.path.join('datas/files/socres', file.filename))

                # append the path to filepath list
                filepath.append('datas/files/socres/' + file.filename)

            # build new socres method
            new_socres = social_responsibility(lecturer_nip=lecturer_nip, year=year, title=title, investor=investor,
                                               amount=amount, position=position, filepath=str(filepath),
                                               other_parties=str(other_parties))

            # call save method from socres module
            res = new_socres.save()
            return jsonify(res)
        else:
            res = {
                'status': 200,
                'message': 'Please upload at least 1 file'
            }
            return jsonify(res)
    elif request.method == 'PUT':
        # get id from the query string
        id = request.args.get('id')

        # call the edit method from research module
        res = edit_socres(id, request.json)
        return jsonify(res)
    # if method == DELETE
    elif request.method == 'DELETE':

        # get id from the query string
        id = request.args.get('id')
        return jsonify(delete_socres(id))

    # if methods aren't recognized
    else:
        res = {
            'status': 500,
            'message': 'Sorry, your request method is not recognized!'
        }
        return jsonify(res)
