from flask import request, jsonify, Blueprint
from achievement.models import achievement, get_all_achievements, edit_achievement, delete_achievement, get_achievement_byID
import os

achievement_blueprint = Blueprint('achievement_blueprint', __name__)
# Allowed file extension
ALLOWED_EXTENSIONS = {'docx', 'pdf'}


def allowed_file(filename):
    # Return boolean based on the ALLOWED_EXTENSION list
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@achievement_blueprint.route('/achievements', methods=['GET', 'POST', 'PUT', 'DELETE'])
def process_achievements():
    # check the request method
    # if method == GET
    if request.method == 'GET':

        # check is there parameter ID
        if request.args.get('id') is None:
            return jsonify(get_all_achievements())
        return jsonify(get_achievement_byID(request.args.get('id')))

    # if method == POST
    elif request.method == 'POST':
        # get data from request json
        lecturer_nip = request.json['lecturer_nip']
        title = request.json['title']
        issuer = request.json['issuer']
        year = request.json['year']

        # get file data into a list
        files = request.files.getlist('achievement_files')

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
            if not os.path.exists('datas/files/achievements'):
                # make a directory if it doesn't exist
                os.makedirs('datas/files/achievements')

            # save file to /datas/files/finalTasks
            file.save(os.path.join('datas/files/achievements', file.filename))

            # append the path to filepath list
            filepath.append('datas/files/achievements/' + file.filename)

        # build new achievement method
        new_achievement = achievement(lecturer_nip=lecturer_nip, title=title, issuer=issuer, year=year, filepath=str(filepath))

        # call save method from achievement module
        res = new_achievement.save()
        return jsonify(res)

    # if method == PUT
    elif request.method == 'PUT':
        # get id from the query string
        id = request.args.get('id')

        # call the edit method from achievement module
        res = edit_achievement(id, request.json)
        return jsonify(res)

    # if method == DELETE
    elif request.method == 'DELETE':

        # get id from the query string
        id = request.args.get('id')
        return jsonify(delete_achievement(id))

    # if methods aren't recognized
    else:
        res = {
            'status': 500,
            'message': 'Sorry, your request method is not recognized!'
        }
        return jsonify(res)
