from flask import request, jsonify, Blueprint
from publication.models import journal, journal_corresponding_author, patent, other_publication, \
    get_all_publication_byCat, get_all_publication, get_publication_byID,edit_publication, delete_experience
import os

publication_blueprint = Blueprint('publication_bluepint', __name__)
# Allowed file extension
ALLOWED_EXTENSIONS = {'docx', 'pdf'}


@publication_blueprint.route('/publication/<cat>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def process_publication(cat):
    # check the request method
    # if method == GET
    if request.method == 'GET':

        # check is there parameter ID
        if request.args.get('id') is None:
            return jsonify(get_all_publication_byCat(cat))
        return jsonify(get_publication_byID(cat, request.args.get('id')))

    # # if method == POST
    # elif request.method == 'POST':
    #     # get data from request json
    #     lecturer_nip = request.json['lecturer_nip']
    #     job_name = request.json['job_name']
    #     job_type = request.json['job_type']
    #     year = request.json['year']
    #     term = request.json['term']
    #
    #     # get file data into a list
    #     files = request.files.getlist('experiences_files')
    #
    #     # loop over the file list
    #     filepath = []
    #     for file in files:
    #
    #         # if the extension not allowed
    #         if not allowed_file(file.filename):
    #             ret = {
    #                 'status': 200,
    #                 'message': 'File Extension must be PDF or DOCX!'
    #             }
    #             return jsonify(ret)
    #
    #         # check the directory to save the file
    #         if not os.path.exists('datas/files/experiences'):
    #             # make a directory if it doesn't exist
    #             os.makedirs('datas/files/experiences')
    #
    #         # save file to /datas/files/finalTasks
    #         file.save(os.path.join('datas/files/achievements', file.filename))
    #
    #         # append the path to filepath list
    #         filepath.append('datas/files/achievements/' + file.filename)
    #
    #     # build new experience method
    #     new_experience = experience(lecturer_nip=lecturer_nip, job_name=job_name, job_type=job_type, year=year,
    #                                 term=term, filepath=str(filepath))
    #
    #     # call save method from experience module
    #     res = new_experience.save()
    #     return jsonify(res)
    #
    # # if method == PUT
    # elif request.method == 'PUT':
    #     # get id from the query string
    #     id = request.args.get('id')
    #
    #     # call the edit method from experience module
    #     res = edit_experience(id, request.json)
    #     return jsonify(res)
    #
    # # if method == DELETE
    # elif request.method == 'DELETE':
    #
    #     # get id from the query string
    #     id = request.args.get('id')
    #     return jsonify(delete_experience(id))
    #
    # # if methods aren't recognized
    # else:
    #     res = {
    #         'status': 500,
    #         'message': 'Sorry, your request method is not recognized!'
    #     }
    #     return jsonify(res)