from sqlalchemy import ForeignKey
from db_config import db, sess


class achievement(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    lecturer_nip = db.Column(db.String(255), ForeignKey("lecturer.nip"), unique=False)
    title = db.Column(db.String(255), unique=False)
    issuer = db.Column(db.String(255), unique=False)
    year = db.Column(db.String(5), unique=False)
    filepath = db.Column(db.String(255), unique=True)

    def save(self):
        try:
            check_achievement = sess.query(achievement).filter(achievement.lecturer_nip == self.lecturer_nip).filter(achievement.title==self.title).\
                filter(achievement.year == self.year).first()
            if check_achievement is None:
                sess.add(self)
                sess.commit()
                new_achievement = {
                    'id': self.id,
                    'lecturer_nip': self.lecturer_nip,
                    'title': self.title,
                    'issuer': self.issuer,
                    'year': self.year,
                    'filepath': self.filepath
                }
                ret = {
                    'status': 200,
                    'message': 'New Achievement Registered',
                    'results': new_achievement
                }
            else:
                ret = {
                    'status': 200,
                    'message': 'Your achievement already registered before, please try again another achievement!'
                }
            return ret
        except Exception as e:
            ret ={
                'status': 200,
                'message': e.args
            }
            return ret


def get_all_achievements():
    try:
        achievements = sess.query(achievement).all()
        res = []
        for data in achievements:
            temp = {
                'id': data.id,
                'lecturer_nip': data.lecturer_nip,
                'title': data.title,
                'issuer': data.issuer,
                'year': data.year,
                'filepath': data.filepath
            }
            res.append(temp)
        ret = {
            'status': 200,
            'message': 'These are the registered Achievements',
            'results': res
        }
        return ret
    except Exception as e:
        ret = {
            'status': 200,
            'message': e.args,
        }
        return ret


def get_achievement_byID(id):
    try:
        data = sess.query(achievement).filter(achievement.id == id).first()
        selected_achievement = {
            'id': data.id,
            'lecturer_nip': data.lecturer_nip,
            'title': data.title,
            'issuer': data.issuer,
            'year': data.year,
            'filepath': data.filepath
        }
        ret = {
            'status': 200,
            'message': 'This is the '+data.lecturer_nip+' Achievement',
            'results': selected_achievement
        }
        return ret
    except Exception as e:
        ret = {
            'status': 200,
            'message': e.args,
        }
        return ret


def edit_achievement(id, request):
    try:
        selected_achievement = sess.query(achievement).filter(achievement.id == id).first()
        if selected_achievement is not None:
            data = {}
            for k in request.keys():
                param = k
                data[k] = request[param]
            edit = sess.query(achievement).filter(achievement.id == id).update(data, synchronize_session=False)
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
                'message': "Achievement is not registered"
            }
            return ret
    except Exception as e:
        ret = {
            'status': 200,
            'message': e.args,
        }
        return ret


def delete_achievement(id):
    try:
        selected_achievement = sess.query(achievement).filter(achievement.id == id).first()
        if selected_achievement is not None:
            sess.delete(selected_achievement)
            sess.commit()
            ret = {
                'status': 200,
                'message': 'Data deleted!'
            }
            return ret
        else:
            ret = {
                'status': 200,
                'message': "Achievement is not registered"
            }
            return ret
    except Exception as e:
        ret = {
            'status': 200,
            'message': e.args
        }
        return ret


def get_achievement_byLecturer(nip):
    try:
        datas = sess.query(achievement).filter(achievement.lecturer_nip == nip).all()
        if datas is not None:
            res = []
            for data in datas:
                temp = {
                    'id': data.id,
                    'lecturer_nip': data.lecturer_nip,
                    'title': data.title,
                    'issuer': data.issuer,
                    'year': data.year,
                    'filepath': data.filepath
                }
                res.append(temp)
            ret = {
                'status': 200,
                'message': 'This is the registered academic lecturer',
                'results': res
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