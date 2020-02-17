from db_config import db, sess
from flask import session as logged_in
import secrets
import bcrypt

roles = ['', 'Super Admin', 'Admin Akademik', 'Admin Non-Akademik', 'Tendik', 'Dosen', 'Kaprodi']


def logout():
    try:
        print(logged_in)
        if logged_in['status']:
            logged_in.clear()
            ret ={
                'status': 200,
                'message': 'Log out Success',
                'results': logged_in.get('user')
            }
            print(logged_in)
            return ret
        else:
            ret = {
                'status': 200,
                'message': 'You are not logged in!'
            }
        return ret
    except Exception as e:
        ret = {
            'status': 200,
            'message': e.args
        }
        return ret


def sessionCheck():
    # res = logged_in.get('user')
    # return res
    if 'status' not in logged_in:
        res ={
            'status': False,
            'token': 999,
            'user': None
        }
    else:
        res = {
            'status': logged_in.get('status'),
            'token': logged_in.get('token'),
            'user': logged_in.get('user')
        }
    return res


def login(cat, id, password):
    try:
        if 'status' not in logged_in:
            logged_in['status'] = False
            logged_in['token'] = 999
            logged_in['user'] = None
        if not logged_in['status']:
            if cat != 'lecturer' and cat != 'admin':
                ret = {
                    'status': 200,
                    'message': 'wrong category'
                }
                return ret
            if cat == 'lecturer':
                checkuser = sess.query(lecturer).filter(lecturer.nip == id).first()
            else:
                checkuser = sess.query(admin).filter(admin.auth_id == id).first()
            if checkuser is not None:
                if bcrypt.checkpw(password.encode('utf-8'), checkuser.password.encode('utf-8')):
                    if cat == 'lecturer':
                        user = {
                            'nip': checkuser.nip,
                            'email': checkuser.email,
                            'name': checkuser.name
                        }
                    else:
                        user = {
                            'auth_id': checkuser.auth_id,
                            'email': checkuser.email,
                            'name': checkuser.name
                        }
                    logged_in['status'] = True
                    logged_in['token'] = secrets.token_hex(16)[0:100]
                    logged_in['user'] = user
                    logged_in.modified = True
                    sessions = {
                        'token': logged_in.get('token'),
                        'user': logged_in.get('user')
                    }
                    ret = {
                        'status': True,
                        'message': 'Login successful',
                        'results': sessions
                    }

                    return ret
                else:
                    ret = {
                        'status': False,
                        'message': "You've entered the wrong password"
                    }
                    return ret
            else:
                ret = {
                    'status': 200,
                    'message': 'ID is not registered'
                }
                return ret
        else:
            ret = {
                'status': 200,
                'message': "You've logged in with token "+str(logged_in['token'])
            }
            return ret
    except Exception as e:
        ret = {
            'status': 200,
            'message': e.args
        }
        return ret


class lecturer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    role = db.Column(db.Integer, unique=True, nullable=False)
    nip = db.Column(db.String(255), primary_key=True, unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)

    def save(self):
        try:
            check_user = sess.query(lecturer).filter(lecturer.nip == self.nip).first()
            if check_user is not None:
                ret = {
                    'status': 200,
                    'message': "NIP already registered, try again another NIP"
                }
                return ret
            new_lecturer = {
                'name': self.name,
                'role': self.role,
                'nip': self.nip,
                'email': self.email
            }
            ret = {
                'status': 200,
                'message': 'Lecturer Registered',
                'results': new_lecturer
            }
            sess.add(self)
            sess.commit()
            return ret
        except Exception as e:
            ret = {
                'status': 200,
                'message': e.args,
            }
            return ret

    def edit(self, nip, request):
        try:
            selected_lecturer = sess.query(lecturer).filter(lecturer.nip == nip).first()
            if selected_lecturer is not None:
                data = {}
                for k in request.keys():
                    param = k
                    if param == "password":
                        data[k] = bcrypt.hashpw(request[param].encode('utf-8'), bcrypt.gensalt())
                    else:
                        data[k] = request[param]
                check = sess.query(lecturer).filter(lecturer.nip == nip).update(data, synchronize_session=False)
                sess.commit()
                if check == 1:
                    ret = {
                        'status': 200,
                        'message': 'Data updated!'
                    }
                else:
                    ret = {
                        'status': 500,
                        'message': "Something's went wrong with our server. Please try again later!"
                    }
                return ret
            else:
                ret = {
                    'status': 200,
                    'message': "NIP is not registered"
                }
                return ret
        except Exception as e:
            ret = {
                'status': 500,
                'message': e.args
            }
            return ret

    def delete(self, nip):
        try:
            selected_lecturer = sess.query(lecturer).filter(lecturer.nip == nip).first()
            if selected_lecturer is not None:
                sess.delete(selected_lecturer)
                sess.commit()
                ret = {
                    'status': 200,
                    'message': 'Data deleted!'
                }
                return ret
            else:
                ret = {
                    'status': 200,
                    'message': "NIP is not registered"
                }
                return ret
        except Exception as e:
            ret = {
                'status': 500,
                'message': e.args
            }
            return ret


class admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    role = db.Column(db.Integer, unique=True, nullable=False)
    auth_id = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)

    def save(self):
        try:
            check_user = sess.query(admin).filter(admin.auth_id == self.auth_id).first()
            if check_user is not None:
                ret = {
                    'status': 200,
                    'message': "Auth_ID already registered, try again another Auth_ID"
                }
                return ret
            sess.add(self)
            sess.commit()
            new_admin = {
                'id': self.id,
                'auth_id': self.auth_id,
                'name': self.name,
                'role': self.role,
                'email': self.email
            }
            ret = {
                'status': 200,
                'message': 'Admin Registered',
                'results': new_admin
            }
            return ret
        except Exception as e:
            ret = {
                'status': 500,
                'message': e.args,
            }
            return ret

    def edit(self, auth_id, request):
        try:
            selected_admin = sess.query(admin).filter(admin.auth_id == auth_id).first()
            if selected_admin is not None:
                data = {}
                for k in request.keys():
                    param = k
                    if param == "password":
                        data[k] = bcrypt.hashpw(request[param].encode('utf-8'), bcrypt.gensalt())
                    else:
                        data[k] = request[param]
                check = sess.query(admin).filter(admin.auth_id == auth_id).update(data, synchronize_session=False)
                sess.commit()
                if check == 1:
                    ret = {
                        'status': 200,
                        'message': 'Data updated!'
                    }
                else:
                    ret = {
                        'status': 500,
                        'message': "Something's wrong with our server. Please try again later!"
                    }
                return ret
            else:
                ret = {
                    'status': False,
                    'message': "Auth_ID is not registered"
                }
                return ret
        except Exception as e:
            ret = {
                'status': 500,
                'message': e.args
            }
            return ret

    def delete(self, auth_id):
        try:
            selected_admin = sess.query(admin).filter(admin.auth_id == auth_id).first()
            if selected_admin is not None:
                sess.delete(selected_admin)
                sess.commit()
                ret = {
                    'status': 200,
                    'message': 'Data deleted!'
                }
                return ret
            else:
                ret = {
                    'status': 200,
                    'message': "Auth_ID is not registered"
                }
                return ret
        except Exception as e:
            ret = {
                'status': 500,
                'message': e.args
            }
            return ret


def getAll(cat):
    try:
        if cat == 'lecturer':
            lecturers = sess.query(lecturer).all()
            hasil = []
            for data in lecturers:
                res = {
                    'id': data.id,
                    'name': data.name,
                    'role': roles[data.role],
                    'user_id': data.nip,
                    'email': data.email
                }
                hasil.append(res)
            ret = {
                'status': 200,
                'results': hasil,
                'message': 'These are the registered lecturers'
            }
        elif cat == 'admin':
            admins = sess.query(admin).all()
            hasil = []
            for data in admins:
                res = {
                    'id': data.id,
                    'name': data.name,
                    'role': roles[data.role],
                    'user_id': data.auth_id,
                    'email': data.email
                }
                hasil.append(res)
            ret = {
                'status': 200,
                'results': hasil,
                'message': 'These are the registered admins'
            }
        else:
            ret = {
                'status': 200,
                'message': 'Category not recognized'
            }
        return ret
    except Exception as e:
        ret = {
            'status': 200,
            'message': e.args
        }
        return ret


def getAllUsersWithoutSuperAdmin():
    try:
        hasil = []

        lecturers = sess.query(lecturer).all()
        for data in lecturers:
            res = {
                'id': data.id,
                'name': data.name,
                'role': roles[data.role],
                'nip': data.nip,
                'email': data.email
            }
            hasil.append(res)

        admins = sess.query(admin).all()
        for data in admins:
            res = {
                'id': data.id,
                'name': data.name,
                'role': roles[data.role],
                'auth_id': data.auth_id,
                'email': data.email
            }
            if roles[data.role] != 'Super Admin':
                hasil.append(res)

        ret = {
            'status': 200,
            'results': hasil,
            'message': 'These are the registered users without super admin'
        }

        return ret
    except Exception as e:
        ret = {
            'status': 500,
            'message': e.args
        }
        return ret


def getByID(cat, id):
    try:
        if cat == 'lecturer':
            lecturers = sess.query(lecturer).filter(lecturer.nip == id).first()
            if lecturers is not None:
                res = {
                    'id': lecturers.id,
                    'name': lecturers.name,
                    'role': roles[lecturers.role],
                    'nip': lecturers.nip,
                    'email': lecturers.email
                }
                ret ={
                    'status': 200,
                    'results': res,
                    'message': 'This is lecturer with NIP '+ lecturers.nip
                }
            else:
                ret = {
                    'status': 200,
                    'message': 'NIP is not registered'
                }
        elif cat == 'admin':
            admins = sess.query(admin).filter(admin.auth_id == id).first()
            if admins is not None:
                res = {
                    'id': admins.id,
                    'name': admins.name,
                    'role': roles[admins.role],
                    'auth_id': admins.auth_id,
                    'email': admins.email
                }
                ret = {
                    'status': 200,
                    'results': res,
                    'message': 'This is admin with auth id ' + admins.auth_id
                }
            else:
                ret = {
                    'status': 200,
                    'message': 'ID is not registered'
                }
        else:
            ret = {
                'status': 200,
                'message': 'Category not recognized'
            }
        return ret
    except Exception as e:
        ret = {
            'status': 200,
            'message': e.args
        }
        return ret
