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
        sess.add(self)
        sess.commit()

        return "success"

    def search(self, password, nip):
        selected_lecturer = sess.query(lecturer).filter(lecturer.nip == nip).first()
        if bcrypt.checkpw(password.encode('utf-8'), selected_lecturer.password.encode('utf-8')):
            ret = {
                'status': True,
                'message': 'Account Found',
                'lecturer': selected_lecturer
            }
            return ret
        ret = {
            'status': False,
            'message': "Account not Found!"
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
        sess.add(self)
        sess.commit()

        return "success"

    def search(self, password, nip):
        selected_admin = sess.query(lecturer).filter(lecturer.nip == nip).first()
        if bcrypt.checkpw(password.encode('utf-8'), admin.password.encode('utf-8')):
            ret = {
                'status': True,
                'message': 'Account Found',
                'admin': selected_admin
            }
            return ret
        ret = {
            'status': False,
            'message': "Account not Found!"
        }
        return ret
