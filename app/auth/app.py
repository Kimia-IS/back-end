import bcrypt
from flask import request, jsonify, Blueprint
from auth.models import lecturer, admin, getAll, getByID, getAllUsersWithoutSuperAdmin, login, logout, sessionCheck, getToken, getUser, getByID_login_alternative

auth_blueprint = Blueprint('auth_blueprint', __name__)


def generatePassword():
    return "password"


@auth_blueprint.route('/auth/login/alternative/<cat>', methods=['POST'])
def alternative_login(cat):
    res = getByID_login_alternative(cat, request.form['id'], request.form['password'])
    return jsonify(res)


@auth_blueprint.route('/auth/get-token', methods=['GET'])
def get_token():
    token = getToken()
    user = getUser()
    print(token + ' oii')
    print(user)
    return jsonify({'token': token, 'user': user})

@auth_blueprint.route('/auth/check', methods=['POST'])
def check_auth():
    if request.form['token'] is not None:
        token = request.form['token']
        print('token =', token)
        print('sessionCheck() =', sessionCheck())
        if token == sessionCheck()['token']:
            res = {
                'status': 202,
                'token_verification': True,
                'message': 'You are authorized to access this data',
                'payload': sessionCheck()
            }
        else:
            res = {
                'status': 203,
                'token_verification': False,
                'message': 'You are not authorized to access this data'
            }
        return jsonify(res)
    else:
        res = {
            'status': 203,
            'token_verification': False,
            'message': 'Need token'
        }
        return jsonify(res)
    # return str(sessionCheck())


@auth_blueprint.route('/auth/logout', methods=['POST'])
def process_logout():
    res = logout()
    print('res =', res)
    return jsonify(res)


@auth_blueprint.route('/auth/lecturer/register', methods=['POST'])
def lecturer_register():
    try:
        nip = request.json['nip']
        password = bcrypt.hashpw(generatePassword().encode('utf-8'), bcrypt.gensalt())
        email = request.json['email']
        name = request.json['name']
        role = request.json['role']

        # build new lecturer object
        selected_lecturer = lecturer(nip=nip, password=password, email=email, name=name, role=role)

        # store new lecturer to database via Lecturer model
        res = selected_lecturer.save()
        return res
    except Exception as e:
        res = {
            'status': 200,
            'message': e.args
        }
        return res


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


@auth_blueprint.route('/auth/login/<cat>', methods=['POST'])
def lecturer_login(cat):

    print('request =', request.form['id'])

    # get response from login lecturer method
    res = login(cat, request.form['id'], request.form['password'])

    return jsonify(res)


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


@auth_blueprint.route('/auth/admin/edit/<auth_id>', methods=['PUT'])
def admin_edit(auth_id):

    # build new admin object
    selected_admin = admin()

    # get response from edit admin method
    res = selected_admin.edit(auth_id, request.json)
    return jsonify(res)


@auth_blueprint.route('/auth/admin/delete/<auth_id>', methods=['DELETE'])
def admin_delete(auth_id):

    # build new admin object
    selected_admin = admin()

    # get response from delete admin method
    res = selected_admin.delete(auth_id)
    return jsonify(res)


@auth_blueprint.route('/auth/user', methods=['GET'])
def get_user_by_id():
    role = int(request.args.get('role'))
    if (role == 4) or (role == 5) or (role == 6):
        cat = 'lecturer'
    elif (role == 1) or (role == 2) or (role == 3):
        cat = 'admin'
    else:
        ret = {
            'status': 400,
            'message': 'Role is undefined',
        }
        return jsonify(ret)

    # check is the ID parameter exist
    if request.args.get('id'):

        # call getByID method
        return jsonify(getByID(cat, request.args.get('id')))

    else:

        ret = {
            'status': 400,
            'message': 'Id is undefined',
        }
        return jsonify(ret)


@auth_blueprint.route('/auth/users/<cat>', methods=['GET'])
def get_lecturer_admin(cat):
    # check is the category parameter exist
    if cat:

        # call getAll method
        return jsonify(getAll(cat))

    else:

        ret = {
            'status': 400,
            'message': 'Category is undefined',
        }
        return jsonify(ret)


@auth_blueprint.route('/auth/users/no-super-admin', methods=['GET'])
def get_all_users_without_superadmin():

    return jsonify(getAllUsersWithoutSuperAdmin())


@auth_blueprint.route('/auth/register', methods=['POST'])
def register():
    user_id = request.json['user_id']
    password = bcrypt.hashpw(generatePassword().encode('utf-8'), bcrypt.gensalt())
    email = request.json['email']
    name = request.json['name']
    role = request.json['role']

    if (role == 4) or (role == 5) or (role == 6):
        # build new lecturer object
        selected_lecturer = lecturer(nip=user_id, password=password, email=email, name=name, role=role)

        # store new lecturer to database via Lecturer model
        res = selected_lecturer.save()
        return jsonify(res)

    elif (role == 1) or (role == 2) or (role == 3):
        # build new admin object
        selected_admin = admin(auth_id=user_id, password=password, email=email, name=name, role=role)

        # store new admin to database via Admin model
        res = selected_admin.save()
        return jsonify(res)

    else:
        ret = {
            'status': 400,
            'message': 'Role is undefined',
        }
        return jsonify(ret)