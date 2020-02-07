from db_config import db, sess
from sqlalchemy import ForeignKey


class experience(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    lecturer_nip = db.Column(db.String(255), ForeignKey("lecturer.nip"), unique=False)
    job_name = db.Column(db.String(255), unique=False)
    job_type = db.Column(db.String(255), unique=False)
    year = db.Column(db.String(255), unique=False)
    term = db.Column(db.Integer, unique=False)
    filepath = db.Column(db.String(255), unique=False)

    def save(self):
        try:
            check_experience = sess.query(experience).filter(experience.lecturer_nip == self.lecturer_nip).\
                filter(experience.job_name == self.job_name).first()
            if check_experience is None:
                sess.add(self)
                sess.commit()
                new_experience = {
                    'id': self.id,
                    'lecturer_nip': self.lecturer_nip,
                    'job_name': self.job_name,
                    'job_type': self.job_type,
                    'year': self.year,
                    'term': self.term,
                    'filepath': self.filepath
                }
                ret = {
                    'status': 200,
                    'message': 'New Experience Registered',
                    'results': new_experience
                }
            else:
                ret = {
                    'status': 200,
                    'message': 'Your experience already registered before, please try again another experience!'
                }
            return ret
        except Exception as e:
            ret ={
                'status': 200,
                'message': e.args
            }
            return ret


def get_all_experiences():
    try:
        experiences = sess.query(experience).all()
        res = []
        for data in experiences:
            temp = {
                'id': data.id,
                'lecturer_nip': data.lecturer_nip,
                'job_name': data.job_name,
                'job_type': data.job_type,
                'year': data.year,
                'term': data.term,
                'filepath': data.filepath
            }
            res.append(temp)
        ret = {
            'status': 200,
            'message': 'This are the registered Experience',
            'results': res
        }
        return ret
    except Exception as e:
        ret = {
            'status': 200,
            'message': e.args,
        }
        return ret


def get_experience_byID(id):
    try:
        data = sess.query(experience).filter(experience.id == id).first()
        selected_experience = {
            'id': data.id,
            'lecturer_nip': data.lecturer_nip,
            'job_name': data.job_name,
            'job_type': data.job_type,
            'year': data.year,
            'term': data.term,
            'filepath': data.filepath
        }
        ret = {
            'status': 200,
            'message': 'This is the '+data.lecturer_nip+' Experience',
            'results': selected_experience
        }
        return ret
    except Exception as e:
        ret = {
            'status': 200,
            'message': e.args,
        }
        return ret


def get_experience_byLecturer(id):
    try:
        data = sess.query(experience).filter(experience.lecturer_nip == id).first()
        if data is not None:
            selected_experience = {
                'id': data.id,
                'lecturer_nip': data.lecturer_nip,
                'job_name': data.job_name,
                'job_type': data.job_type,
                'year': data.year,
                'term': data.term,
                'filepath': data.filepath
            }
            ret = {
                'status': 200,
                'message': 'This is the '+data.lecturer_nip+' Experience',
                'results': selected_experience
            }
            return ret
        else:
            ret = {
                'status': 200,
                'message': 'ID is not registered'
            }
            return ret
    except Exception as e:
        ret = {
            'status': 200,
            'message': e.args,
        }
        return ret


def edit_experience(id, request):
    try:
        selected_experience = sess.query(experience).filter(experience.id == id).first()
        if selected_experience is not None:
            data = {}
            for k in request.keys():
                param = k
                data[k] = request[param]
            edit = sess.query(experience).filter(experience.id == id).update(data, synchronize_session=False)
            sess.commit()
            if edit == 1:
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
                'message': "Experience is not registered"
            }
            return ret
    except Exception as e:
        ret = {
            'status': 200,
            'message': e.args,
        }
        return ret


def delete_experience(id):
    try:
        selected_experience = sess.query(experience).filter(experience.id == id).first()
        if selected_experience is not None:
            sess.delete(selected_experience)
            sess.commit()
            ret = {
                'status': 200,
                'message': 'Data deleted!'
            }
            return ret
        else:
            ret = {
                'status': 200,
                'message': "Experience is not registered"
            }
            return ret
    except Exception as e:
        ret = {
            'status': 200,
            'message': e.args
        }
        return ret
