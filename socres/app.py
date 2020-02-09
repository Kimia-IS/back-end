from flask import request, jsonify, Blueprint
from socres.models import socres, get_all_socres, get_socres_byID, edit_socres, delete_socres
import os

socres_blueprint = Blueprint('socres_blueprint', __name__)
# Allowed file extension
ALLOWED_EXTENSIONS = {'docx', 'pdf', 'jpg', 'jpeg'}


def allowed_file(filename):
    # Return boolean based on the ALLOWED_EXTENSION list
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@socres_blueprint.route('/socres', methods=['GET', 'POST', 'PUT', 'DELETE'])
def process_socres():
    try:
        # check the request method
        # if method == GET
        if request.method == 'GET':

            # check is there parameter ID
            if request.args.get('id') is None:
                return jsonify(get_all_socres())
            return jsonify(get_socres_byID(request.args.get('id')))

        # if method == POST
        elif request.method == 'POST':
            # get data from request json
            lecturer_nip = request.form['lecturer_nip']
            title = request.form['title']
            investor = request.form['investor']
            year = request.form['year']
            amount = request.form['amount']
            position = request.form['position']
            other_parties = request.form['other_parties']

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

                # save file to /datas/files/finalTasks
                file.save(os.path.join('datas/files/socres', file.filename))

                # append the path to filepath list
                filepath.append('datas/files/socres/' + file.filename)

            # build new socres method
            new_socres = socres(lecturer_nip=lecturer_nip, title=title, investor=investor, year=year, amount=amount, position=position,
                                        other_parties=other_parties, filepath=str(filepath))

            # call save method from socres module
            res = new_socres.save()
            return jsonify(res)

        # if method == PUT
        elif request.method == 'PUT':
            # get id from the query string
            id = request.args.get('id')

            # call the edit method from socres module
            res = edit_socres(id, request.form)
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
    except Exception as e:
        ret = {
            'status': 200,
            'message': e.args,
        }
        return ret