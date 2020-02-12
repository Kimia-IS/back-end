from flask import request, jsonify, Blueprint
from research.models import research, research_file, get_all_research, get_research_byID, edit_research, \
    edit_research_file, delete_research
import os

research_blueprint = Blueprint('research_blueprint', __name__)
# Allowed file extension
ALLOWED_EXTENSIONS = {'docx', 'pdf', 'jpg', 'jpeg'}

def allowed_file(filename):
    # Return boolean based on the ALLOWED_EXTENSION list
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@research_blueprint.route('/research', methods=['GET', 'POST', 'PUT', 'DELETE'])
def process_research():
    try:
        # check the request method
        # if method == GET
        if request.method == 'GET':
            # check is there parameter ID
            if request.args.get('id') is None:
                return jsonify(get_all_research())
            return jsonify(get_research_byID(request.args.get('id')))

        # if method == POST
        elif request.method == 'POST':
            if request.files:
                # get data from request json
                lecturer_nip = request.form['lecturer_nip']
                title = request.form['title']
                investor = request.form['investor']
                year = request.form['year']
                amount = request.form['amount']
                position = request.form['position']

                # get file data into a list
                files = request.files.getlist('research_files')

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
                    if not os.path.exists('datas/files/research'):
                        # make a directory if it doesn't exist
                        os.makedirs('datas/files/research')

                    filename = lecturer_nip + '_' + file.filename.replace(' ', '_')

                    # save file to /datas/files/finalTasks
                    file.save(os.path.join('datas/files/research', filename))

                    # append the path to filepath list
                    filepath.append('datas/files/research/' + filename)

                # build new research method
                new_research = research(lecturer_nip=lecturer_nip, year=year, title=title, investor=investor,
                                          amount=amount, position=position, filepath=str(filepath))

                # call save method from research module
                res = new_research.save()
                return jsonify(res)
            else:
                res ={
                    'status': 200,
                    'message': 'Please upload at least 1 file'
                }
                return jsonify(res)

        # if method == PUT
        elif request.method == 'PUT':
            # get id from the query string
            id = request.args.get('id')

            # call the edit method from research module
            res = edit_research(id, request.form)
            return jsonify(res)

        # if method == DELETE
        elif request.method == 'DELETE':

            # get id from the query string
            id = request.args.get('id')
            return jsonify(delete_research(id))

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


@research_blueprint.route('/research/files/edit/<id>')
def edit_file(id):
    try:
        if request.files:
            # get file data into a list
            files = request.files.getlist('research_files')

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
                if not os.path.exists('datas/files/research'):
                    # make a directory if it doesn't exist
                    os.makedirs('datas/files/research')

                # save file to /datas/files/finalTasks
                file.save(os.path.join('datas/files/research', file.filename))

                # append the path to filepath list
                filepath.append('datas/files/research/' + file.filename)
            return jsonify(edit_research_file(id, str(filepath)))

        # if file doesn't exist
        else:
            res = {
                'status': 200,
                'message': 'Please attach your research file, required minimal 1'
            }
            return jsonify(res)
    except Exception as e:
        res = {
            'status': 200,
            'message': e.args
        }
        return jsonify(res)
