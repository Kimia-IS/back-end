from flask import request, jsonify, Blueprint
from academic.models import academic, academic_lecturer, get_all_academic_lecturer, get_all_courses
from announcement import announcement

academic_blueprint = Blueprint('academic_blueprint', __name__)


@academic_blueprint.route('/academic/courses', methids=['GET', 'POST', 'PUT', 'DELETE'])
def process_academic_courses():
    # check request method
    # if request method = POST
    if request.method == 'GET':
        # call get all academic courses method from academic module
        return jsonify(get_all_courses())

    # if request method = POST
    elif request.method == 'POST':

        # get data from json request
        course_id = request.json['course_id']
        course_name = request.json['course_name']
        total_credit = request.json['total_credit']

        # build new academic object with initial value
        new_course = academic(course_id=course_id, course_name=course_name, total_credit=total_credit)

        # call the save method from academic object
        ret = new_course.save()
        return jsonify(ret)

    # if request method = PUT
    elif request.method == 'PUT':

        # get id from query
        id = request.args.get('id')

        # build new academic object
        academic_object = academic()

        # call the edit method from academic object
        ret = academic_object.edit(id, request.json)
        return jsonify(ret)

    # if request method = DELETE
    elif request.method == 'DELETE':
        # get id from query
        id = request.args.get('id')

        # build new announcement object
        academic_object = academic()

        # call the delete method from announcement object
        ret = academic_object.delete(id)
        return jsonify(ret)

    # if request method is unknown
    else:
        return jsonify({'status': 500, 'message': 'Sorry, your request method is not recognized!'})


@academic_blueprint.route('/academic/lecturer', methods=['GET', 'POST', 'PUT', 'DELETE'])
def process_academic_lecturer():

    # check request method
    # if request method = POST
    if request.method == 'GET':

        # call get all academic lecturer method from academic module
        return jsonify(get_all_academic_lecturer())

    # if request method = POST
    elif request.method == 'POST':

        # get data from json request
        course_id = request.json['course_id']
        course_class = request.json['course_class']
        lecturer_nip = request.json['lecturer_nip']
        lecturer_credit = request.json['lecturer_credit']

        # build new academic lecturer object with initial value
        new_academic_lecturer = academic_lecturer(course_id=course_id, course_class=course_class, lecturer_nip=lecturer_nip, lecturer_credit=lecturer_credit)

        # call the save method from academic lecturer object
        ret = new_academic_lecturer.save()
        return jsonify(ret)

    # if request method = PUT
    elif request.method == 'PUT':

        # get id from query
        id = request.args.get('id')

        # build new academic lecturer object
        academic_lecturer_object = academic_lecturer()

        # call the edit method from academic lecturer object
        ret = academic_lecturer_object.edit(id, request.json)
        return jsonify(ret)

    # if request method = DELETE
    elif request.method == 'DELETE':
        # get id from query
        id = request.args.get('id')

        # build new announcement object
        academic_lecturer_object = academic_lecturer()

        # call the delete method from announcement object
        ret = academic_lecturer_object.delete(id)
        return jsonify(ret)

    # if request method is unknown
    else:
        return jsonify({'status': 500, 'message': 'Sorry, your request method is not recognized!'})


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
        author = request.json['author']
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
