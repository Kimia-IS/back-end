from flask import request, jsonify, Blueprint
from academic.models import academic, academic_lecturer, get_all_academic_lecturer, get_all_courses, \
    get_academicLecturer_byID, get_academicCourses_byID
from ast import literal_eval as make_tuple

academic_blueprint = Blueprint('academic_blueprint', __name__)


@academic_blueprint.route('/academic/courses', methods=['GET', 'POST', 'PUT', 'DELETE'])
def process_academic_courses():
    # check request method
    # if request method = POST
    if request.method == 'GET':
        if request.args.get('id'):
            return jsonify(get_academicCourses_byID(request.args.get('id')))
        # call get all academic courses method from academic module
        return jsonify(get_all_courses())

    # if request method = POST
    elif request.method == 'POST':

        # get data from json request
        course_id = request.json['course_id']
        course_name = request.json['course_name']
        
        total_classes = request.json['total_classes']

        # build new academic object with initial value
        new_course = academic(course_id=course_id, course_name=course_name, total_classes=total_classes)

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
        if request.args.get('id'):
            return jsonify(get_academicLecturer_byID(request.args.get('id')))
        # call get all academic lecturer method from academic module
        return jsonify(get_all_academic_lecturer())

    # if request method = POST
    elif request.method == 'POST':

        # get data from json request
        course_id = request.json['course_id']
        course_class = request.json['course_class']
        lecturer = request.json['lecturer']
        total_credit = request.json['total_credit']

        ret = []
        for lecturer in lecturer:
            data = make_tuple(lecturer)
            # build new academic lecturer object with initial value
            new_academic_lecturer = academic_lecturer(course_id=course_id, course_class=course_class, total_credit=total_credit, lecturer_nip=data[0], lecturer_credit=data[1])

            # call the save method from academic lecturer object
            ret.append(new_academic_lecturer.save())
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
