import bcrypt
import random
import string
from flask import request, jsonify, Blueprint
from auth.models import lecturer, admin

auth_blueprint = Blueprint('auth_blueprint', __name__)
lecturer = lecturer
admin = admin


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
    new_lecturer = lecturer(nip=nip, password=password, email=email, name=name, role=role)

    # store new lecturer to database via Lecturer model
    res = new_lecturer.save()
    return jsonify(res)


@auth_blueprint.route('/auth/lecturer/login', methods=['POST'])
def lecturer_login():
    search_lecturer = lecturer()
    res = search_lecturer.search(request.json['password'], request.json['nip'])
    if res['status']:
        ret = {
            'status': 200,
            'message': 'Berhasil Log In '+res['lecturer'].name
        }
        return jsonify(ret)

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
    new_admin = admin(auth_id=auth_id, password=password, email=email, name=name, role=role)

    # store new admin to database via Admin model
    res = new_admin.save()
    return jsonify(res)


@auth_blueprint.route('/auth/lecturer/login', methods=['POST'])
def admin_login():
    search_admin = admin()
    res = search_admin.search(request.json['password'], request.json['nip'])
    if res['status']:
        ret = {
            'status': 200,
            'message': 'Berhasil Log In ' + res['admin'].name
        }
        return jsonify(ret)

    ret = {
        'status': 200,
        'message': res['message']
    }
    return jsonify(ret)
