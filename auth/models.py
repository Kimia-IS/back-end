from db_config import db, sess
import bcrypt


class lecturer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    role = db.Column(db.Integer, unique=True, nullable=False)
    nip = db.Column(db.String(255), unique=True, nullable=False)
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
            sess.add(self)
            sess.commit()
            new_lecturer = {
                'id': self.id,
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
                'status': 200,
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
                'status': 200,
                'message': e.args
            }
            return ret

    def login(self, password, nip):
        try:
            selected_lecturer = sess.query(lecturer).filter(lecturer.nip == nip).first()
            if selected_lecturer is not None:
                if bcrypt.checkpw(password.encode('utf-8'), selected_lecturer.password.encode('utf-8')):
                    ret = {
                        'status': True,
                        'message': 'Login successful',
                        'results': selected_lecturer
                    }
                    return ret
                ret = {
                    'status': False,
                    'message': "You've entered wrong password!"
                }
                return ret
            else:
                ret = {
                    'status': False,
                    'message': "NIP is not registered"
                }
                return ret
        except Exception as e:
            ret = {
                'status': False,
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
                'status': 200,
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
                'status': False,
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
                'status': 200,
                'message': e.args
            }
            return ret

    def login(self, password, auth_id):
        try:
            selected_admin = sess.query(admin).filter(admin.auth_id == auth_id).first()
            if selected_admin is not None:
                if bcrypt.checkpw(password.encode('utf-8'), selected_admin.password.encode('utf-8')):
                    ret = {
                        'status': True,
                        'message': 'Login successful',
                        'results': selected_admin
                    }
                    return ret
                ret = {
                    'status': False,
                    'message': "You've entered wrong password!"
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
                'status': False,
                'message': e.args
            }
            return ret
