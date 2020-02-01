import bcrypt
import random
import string
from flask import request, jsonify, Blueprint
from auth.models import lecturer, admin, get_all_admin, get_all_lecturer

auth_blueprint = Blueprint('auth_blueprint', __name__)


def generatePassword():
    password = string.ascii_letters + string.digits
    return ''.join(random.choice(password) for i in range(10))


@auth_blueprint.route('/auth/lecturer/register', methods=['POST'])
def lecturer_register():
    nip = request.json['nip']
    password = bcrypt.hashpw(generatePassword().encode('utf-8'), bcrypt.gensalt())
    email = request.json['email']
    name = request.json['name']
    role = request.json['role']

    # build new lecturer object
    selected_lecturer = lecturer(nip=nip, password=password, email=email, name=name, role=role)

    # store new lecturer to database via Lecturer model
    res = selected_lecturer.save()
    return jsonify(res)


@auth_blueprint.route('/auth/lecturer/edit/<nip>', methods=['PUT'])
def lecturer_edit(nip):

    # build new lecturer object
    selected_lecturer = lecturer()

    # get response from edit lecturer method
    res = selected_lecturer.edit(nip, request.json)
    return jsonify(res)


@auth_blueprint.route('/auth/lecturer/delete/<nip>', methods=['DELETE'])
def lecturer_delete(nip):

    # build new lecturer object
    selected_lecturer = lecturer()

    # get response from delete lecturer method
    res = selected_lecturer.delete(nip)
    return jsonify(res)


@auth_blueprint.route('/auth/lecturer/login', methods=['POST'])
def lecturer_login():

    # build new lecturer object
    selected_lecturer = lecturer()

    # get response from login lecturer method
    res = selected_lecturer.login(request.json['password'], request.json['nip'])

    # if found, loggin in
    if res['status']:
        ret = {
            'status': 200,
            'message': 'Berhasil Log In '+res['lecturer'].name
        }
        return jsonify(ret)

    # else, not found
    ret = {
        'status': 200,
        'message': res['message']
    }
    return jsonify(ret)


@auth_blueprint.route('/auth/admin/register', methods=['POST'])
def admin_register():
    auth_id = request.json['auth_id']
    password = bcrypt.hashpw(generatePassword().encode('utf-8'), bcrypt.gensalt())
    email = request.json['email']
    name = request.json['name']
    role = request.json['role']

    # build new admin object
    selected_admin = admin(auth_id=auth_id, password=password, email=email, name=name, role=role)

    # store new admin to database via Admin model
    res = selected_admin.save()
    return jsonify(res)


@auth_blueprint.route('/auth/admin/edit/<auth_id>', methods=['POST'])
def admin_edit(auth_id):

    # build new admin object
    selected_admin = admin()

    # get response from edit admin method
    res = selected_admin.edit(auth_id, request.json)
    return jsonify(res)


@auth_blueprint.route('/auth/admin/delete/<auth_id>', methods=['POST'])
def admin_delete(auth_id):

    # build new admin object
    selected_admin = admin()

    # get response from delete admin method
    res = selected_admin.delete(auth_id)
    return jsonify(res)


@auth_blueprint.route('/auth/lecturer/login', methods=['POST'])
def admin_login():

    # build new admin object
    selected_admin = admin()

    # get response from delete lecturer method
    res = selected_admin.login(request.json['password'], request.json['nip'])

    # if found, logging in
    if res['status']:
        ret = {
            'status': 200,
            'message': 'Berhasil Log In ' + res['admin'].name
        }
        return jsonify(ret)

    # else, not found
    ret = {
        'status': 200,
        'message': res['message']
    }
    return jsonify(ret)


@auth_blueprint.route('/lecturers', methods=['GET'])
def get_lecturers():

    # call get all lecturer method from academic module
    # send parameter request to check nip query in URL is exist or not
    return jsonify(get_all_lecturer(request))


@auth_blueprint.route('/admins', methods=['GET'])
def get_admins():

    # call get all admin method from academic module
    # send parameter request to check id query in URL is exist or not
    return jsonify(get_all_admin(request))
