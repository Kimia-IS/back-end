import bcrypt
from flask import Flask, request, jsonify, Blueprint
from auth.models import lecturer, admin

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.secret_key = "GB981UA7YT91"

auth_blueprint = Blueprint('auth_blueprint', __name__)

lecturer = lecturer
admin = admin


@auth_blueprint.route('/auth/lecturer/register', methods=['POST'])
def lecturer_register():
    nip = request.json['nip']
    password = bcrypt.hashpw(request.json['password'].encode('utf-8'), bcrypt.gensalt())
    email = request.json['email']
    name = request.json['name']
    role = request.json['role']
    new_lecturer = lecturer(nip=nip, password=password, email=email, name=name, role=role)
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
        'status': 401,
        'message': 'You are not Authorized to Logging In'
    }
    return ret
