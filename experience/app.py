from flask import request, jsonify, Blueprint
from experience.models import experience, get_all_experiences, get_experience_byID, edit_experience, delete_experience
import os

experience_blueprint = Blueprint('experience_blueprint', __name__)
# Allowed file extension
ALLOWED_EXTENSIONS = {'docx', 'pdf', 'jpg', 'jpeg'}


def allowed_file(filename):
    # Return boolean based on the ALLOWED_EXTENSION list
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@experience_blueprint.route('/experiences', methods=['GET', 'POST', 'PUT', 'DELETE'])
def process_experiences():
    try:
        # check the request method
        # if method == GET
        if request.method == 'GET':

            # check is there parameter ID
            if request.args.get('id') is None:
                return jsonify(get_all_experiences())
            return jsonify(get_experience_byID(request.args.get('id')))

        # if method == POST
        elif request.method == 'POST':
            # get data from request json
            lecturer_nip = request.form['lecturer_nip']
            job_name = request.form['job_name']
            job_type = request.form['job_type']
            year = request.form['year']
            term = request.form['term']

            # get file data into a list
            files = request.files.getlist('experiences_files')

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
                if not os.path.exists('datas/files/experiences'):
                    # make a directory if it doesn't exist
                    os.makedirs('datas/files/experiences')

                # save file to /datas/files/finalTasks
                file.save(os.path.join('datas/files/experiences', file.filename))

                # append the path to filepath list
                filepath.append('datas/files/experiences/' + file.filename)

            # build new experience method
            new_experience = experience(lecturer_nip=lecturer_nip, job_name=job_name, job_type=job_type, year=year,
                                        term=term, filepath=str(filepath))

            # call save method from experience module
            res = new_experience.save()
            return jsonify(res)

        # if method == PUT
        elif request.method == 'PUT':
            # get id from the query string
            id = request.args.get('id')

            # call the edit method from experience module
            res = edit_experience(id, request.form)
            return jsonify(res)

        # if method == DELETE
        elif request.method == 'DELETE':

            # get id from the query string
            id = request.args.get('id')
            return jsonify(delete_experience(id))

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