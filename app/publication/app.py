from flask import request, jsonify, Blueprint
from publication.models import journal, patent, other_publication, \
    get_all_publication_byCat, get_all_publication, get_publication_byID, edit_publication, delete_publication, \
    count_journal
import os

publication_blueprint = Blueprint('publication_bluepint', __name__)
# Allowed file extension
ALLOWED_EXTENSIONS = {'docx', 'pdf', 'jpg', 'jpeg'}


def allowed_file(filename):
    # Return boolean based on the ALLOWED_EXTENSION list
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def process_file_upload(nip, cat, files):
    try:
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

            filename = nip + '_' + file.filename.replace(' ', '_')

            # save file to /datas/files/finalTasks
            file.save(os.path.join('datas/files/publications/'+cat, filename))

            # append the path to filepath list
            filepath.append('datas/files/publications/'+cat+'/' + filename)

        # return the filepath
        return str(filepath)
    except Exception as e:
        res = {
            'message': e.args
        }
        return res


@publication_blueprint.route('/publication', methods=['GET'])
def get_pub():
    try:
        return jsonify(get_all_publication())
    except Exception as e:
        res = {
            'message': e.args
        }
        return res

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
                    title = request.form['title']
                    lecturer_nip = request.form['lecturer_nip']
                    year = request.form['year']
                    number = request.form['number']
                    issue = request.form['issue']
                    total_page = request.form['total_page']
                    type = request.form['type']
                    doi = request.form['doi']
                    link = request.form['link']
                    filepath = process_file_upload(nip=lecturer_nip, cat=cat, files=request.files.getlist('publication_files'))

                    # data for corresponding author
                    names = request.form['names']

                    # build new journal object
                    new_publication = journal(title=title, lecturer_nip=lecturer_nip, year=year, number=number, issue=issue,
                                              total_page=total_page, type=type, doi=doi, link=link, filepath=filepath, names=names)

                    # call save method
                    res = new_publication.save()
                    return jsonify(res)

                # if category == patent
                elif cat == 'patent':

                    # get data from request json
                    lecturer_nip = request.form['lecturer_nip']
                    title = request.form['title']
                    status = request.form['status']
                    publisher = request.form['publisher']
                    year = request.form['year']
                    filepath = process_file_upload(nip=lecturer_nip, cat=cat, files=request.files.getlist('publication_files'))

                    # build new patent object
                    new_patent = patent(lecturer_nip=lecturer_nip, title=title, status=status, publisher=publisher,
                                        year=year, filepath=filepath)
                    # call save method from patent module
                    res = new_patent.save()
                    return jsonify(res)

                # if category == other
                elif cat == 'other':

                    # get data from request json
                    title = request.form['title']
                    lecturer_nip = request.form['lecturer_nip']
                    year = request.form['year']
                    publisher = request.form['publisher']
                    filepath = process_file_upload(nip=lecturer_nip, cat=cat, files=request.files.getlist('publication_files'))

                    # build new other publication object
                    new_other_publication = other_publication(title=title, lecturer_nip=lecturer_nip,
                                                              year=year, publisher=publisher, filepath=filepath)

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
            res = edit_publication(cat, id, request.form)
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
