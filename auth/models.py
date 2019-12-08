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
                'new_lecturer': new_lecturer
            }
            return ret
        except Exception as e:
            ret = {
                'status': 200,
                'message': e.args,
            }
            return ret

    def search(self, password, nip):
        try:
            selected_lecturer = sess.query(lecturer).filter(lecturer.nip == nip).first()
            if selected_lecturer is not None:
                if bcrypt.checkpw(password.encode('utf-8'), selected_lecturer.password.encode('utf-8')):
                    ret = {
                        'status': True,
                        'message': 'Login successful',
                        'lecturer': selected_lecturer
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
                'new_lecturer': new_admin
            }
            return ret
        except Exception as e:
            ret = {
                'status': 200,
                'message': e.args,
            }
            return ret

    def search(self, password, auth_id):
        try:
            selected_admin = sess.query(admin).filter(admin.auth_id == auth_id).first()
            if selected_admin is not None:
                if bcrypt.checkpw(password.encode('utf-8'), selected_admin.password.encode('utf-8')):
                    ret = {
                        'status': True,
                        'message': 'Login successful',
                        'admin': selected_admin
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
