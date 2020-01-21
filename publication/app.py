from flask import request, jsonify, Blueprint
from publication.models import journal, journal_corresponding_author, patent, other_publication, \
    get_all_publication_byCat, get_all_publication, get_publication_byID,edit_publication, delete_publication, \
    count_journal
import os

publication_blueprint = Blueprint('publication_bluepint', __name__)
# Allowed file extension
ALLOWED_EXTENSIONS = {'docx', 'pdf'}


def allowed_file(filename):
    # Return boolean based on the ALLOWED_EXTENSION list
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def process_file_upload(cat, files):
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
        if not os.path.exists('datas/files/publications/'+cat):
            # make a directory if it doesn't exist
            os.makedirs('datas/files/publications/'+cat)

        # save file to /datas/files/finalTasks
        file.save(os.path.join('datas/files/publications/'+cat, file.filename))

        # append the path to filepath list
        filepath.append('datas/files/publications/'+cat+'/' + file.filename)

    # return the filepath
    return str(filepath)


@publication_blueprint.route('/publication/<cat>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def process_publication(cat):
    try:
        # check the request method
        # if method == GET
        if request.method == 'GET':

            # check is there parameter ID
            if request.args.get('id') is None:
                return jsonify(get_all_publication_byCat(cat))
            return jsonify(get_publication_byID(cat, request.args.get('id')))

        # if method == POST
        elif request.method == 'POST':

            # if request file exist
            if request.files:
                # if category == journal
                if cat == 'journal':

                    # get expected id from existing data to store it into task lecturer & file
                    temp_id = count_journal() + 1

                    # get data from request json
                    title = request.json['title']
                    lecturer_nip = request.json['lecturer_nip']
                    year = request.json['year']
                    issue = request.json['issue']
                    total_page = request.json['total_page']
                    type = request.json['type']
                    doi = request.json['doi']
                    link = request.json['link']
                    filepath = process_file_upload(cat, request.files.getlist('publication_files'))

                    # data for corresponding author
                    names = request.json['names']

                    # build new journal object
                    new_publication = journal(title=title, lecturer_nip=lecturer_nip, year=year, issue=issue,
                                              total_page=total_page, type=type, doi=doi, link=link, filepath=filepath)

                    # build new journal corresponding author object
                    new_journal_corresponding_author = journal_corresponding_author(journal_id=temp_id, names=str(names))

                    # call save method
                    new_publication.save()
                    res = new_journal_corresponding_author.save()
                    return jsonify(res)

                # if category == patent
                elif cat == 'patent':

                    # get data from request json
                    lecturer_nip = request.json['lecturer_nip']
                    title = request.json['title']
                    status = request.json['status']
                    publisher = request.json['publisher']
                    year = request.json['year']
                    filepath = process_file_upload(cat, request.files.getlist('publication_files'))

                    # build new patent object
                    new_patent = patent(lecturer_nip=lecturer_nip, title=title, status=status, publisher=publisher,
                                        year=year, filepath=filepath)
                    # call save method from patent module
                    res = new_patent.save()
                    return jsonify(res)

                # if category == other
                elif cat == 'other':

                    # get data from request json
                    title = request.json['title']
                    lecturer_nip = request.json['lecturer_nip']
                    date = request.json['date']
                    publisher = request.json['publisher']
                    filepath = process_file_upload(cat, request.files.getlist('publication_files'))

                    # build new other publication object
                    new_other_publication = other_publication(title=title, lecturer_nip=lecturer_nip,
                                                              date=date, publisher=publisher, filepath=filepath)

                    # call save method
                    res = new_other_publication.save()
                    return jsonify(res)
                else:
                    res = {
                        'status': 200,
                        'message': 'category is not recognized!'
                    }
                    return jsonify(res)
            else:
                res = {
                    'status': 200,
                    'message': 'Please attach your final task file, required minimal 1'
                }
                return jsonify(res)

        # if request method == PUT
        elif request.method == 'PUT':

            # get id from the query string
            id = request.args.get('id')

            # call the edit method from experience module
            res = edit_publication(cat, id, request.json)
            return jsonify(res)

        # if request method == DELETE
        elif request.method == 'DELETE':
            # get id from the query string
            id = request.args.get('id')
            return jsonify(delete_publication(cat, id))

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
