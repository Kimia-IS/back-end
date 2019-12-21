from flask import request, jsonify, Blueprint
from academic.models import academic, get_all_lecturer
from announcement import announcement

academic_blueprint = Blueprint('academic_blueprint', __name__)


@academic_blueprint.route('/academic', methods=['GET'])
def getCourses():
    courses = academic()
    hasil = courses.get()
    return jsonify(hasil)


@academic_blueprint.route('/academic/lecturer', methods=['GET'])
def get_lecturer():

    # call get all lecturer method from academic module
    # send parameter request to check nip query in URL is exist or not
    return jsonify(get_all_lecturer(request))


@academic_blueprint.route('/academic/announcements', methods=['GET', 'POST', 'PUT', 'DELETE'])
def process_announcements():
    # check request method
    # if request method = POST
    if request.method == 'GET':

        # build new announcement object
        announcement_object = announcement()

        # call the getAll method from announcement object
        ret = announcement_object.getAll()
        return jsonify(ret)

    # if request method = POST
    elif request.method == 'POST':

        # get data from json request
        title = request.json['title']
        content = request.json['content']
        author = 'Admin Kimia'
        module = 1
        created_at = '2019-12-12'

        # build new announcement object with initial value
        new_announcement = announcement(title=title, content=content, author=author, module=module,
                                        created_at=created_at)

        # call the save method from announcement object
        ret = new_announcement.save()
        return jsonify(ret)

    # if request method = PUT
    elif request.method == 'PUT':

        # get id from query
        id = request.args.get('id')

        # build new announcement object
        announcement_object = announcement()

        # call the edit method from announcement object
        ret = announcement_object.edit(id, request.json)
        return jsonify(ret)

    # if request method = DELETE
    elif request.method == 'DELETE':
        # get id from query
        id = request.args.get('id')

        # build new announcement object
        announcement_object = announcement()

        # call the delete method from announcement object
        ret = announcement_object.delete(id)
        return jsonify(ret)

    # if request method is unknown
    else:
        return jsonify({'status': 500, 'message': 'Sorry, your request method is not recognized!'})
