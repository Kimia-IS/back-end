from db_config import db, sess
from sqlalchemy import ForeignKey


class socres(db.Model):
    __tablename__ = 'social_responsibility'
    id = db.Column(db.Integer, unique=True, primary_key=True)
    year = db.Column(db.String(255), unique=False)
    title = db.Column(db.String(255), unique=False)
    lecturer_nip = db.Column(db.String(255), ForeignKey('lecturer.nip'), unique=False)
    investor = db.Column(db.String(255), unique=False)
    amount = db.Column(db.String(255), unique=False)
    position = db.Column(db.String(255), unique=False)
    filepath = db.Column(db.String(255), unique=False)
    other_parties = db.Column(db.String(255), unique=False)

    def save(self):
        try:
            check_socres = sess.query(socres).filter(socres.lecturer_nip == self.lecturer_nip).\
                filter(socres.title == self.title).first()
            if check_socres is None:
                sess.add(self)
                sess.commit()
                new_socres = {
                    'id': self.id,
                    'lecturer_nip': self.lecturer_nip,
                    'title': self.title,
                    'investor': self.investor,
                    'year': self.year,
                    'amount': self.amount,
                    'position': self.position,
                    'filepath': self.filepath,
                    'other_parties': self.other_parties,
                }
                ret = {
                    'status': 200,
                    'message': 'New socres Registered',
                    'results': new_socres
                }
            else:
                ret = {
                    'status': 200,
                    'message': 'Your socres already registered before, please try again another socres!'
                }
            return ret
        except Exception as e:
            sess.rollback()
            ret ={
                'status': 200,
                'message': e.args
            }
            return ret
        finally:
            sess.close()


def get_all_socres():
    try:
        socress = sess.query(socres).all()
        res = []
        for data in socress:
            temp = {
                'id': data.id,
                'lecturer_nip': data.lecturer_nip,
                'title': data.title,
                'investor': data.investor,
                'year': data.year,
                'amount': data.amount,
                'position': data.position,
                'filepath': data.filepath,
                'other_parties': data.other_parties,
            }
            res.append(temp)
        ret = {
            'status': 200,
            'message': 'This are the registered socres',
            'results': res
        }
        return ret
    except Exception as e:
        ret = {
            'status': 200,
            'message': e.args,
        }
        return ret
    finally:
        sess.close()


def get_socres_byID(id):
    try:
        data = sess.query(socres).filter(socres.id == id).first()
        selected_socres = {
            'id': data.id,
            'lecturer_nip': data.lecturer_nip,
            'title': data.title,
            'investor': data.investor,
            'year': data.year,
            'amount': data.amount,
            'position': data.position,
            'filepath': data.filepath,
            'other_parties': data.other_parties,
        }
        ret = {
            'status': 200,
            'message': 'This is the '+data.lecturer_nip+' socres',
            'results': selected_socres
        }
        return ret
    except Exception as e:
        ret = {
            'status': 200,
            'message': e.args,
        }
        return ret
    finally:
        sess.close()


def get_socres_byLecturer(id):
    try:
        datas = sess.query(socres).filter(socres.lecturer_nip == id).all()
        if datas is not None:
            res = []
            for data in datas:
                temp = {
                    'id': data.id,
                    'lecturer_nip': data.lecturer_nip,
                    'title': data.title,
                    'investor': data.investor,
                    'year': data.year,
                    'amount': data.amount,
                    'position': data.position,
                    'filepath': data.filepath,
                    'other_parties': data.other_parties,
                }
                res.append(temp)
            ret = {
                'status': 200,
                'message': 'This is the  socres',
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
    finally:
        sess.close()


def edit_socres(id, request):
    try:
        selected_socres = sess.query(socres).filter(socres.id == id).first()
        if selected_socres is not None:
            data = {}
            for k in request.keys():
                param = k
                data[k] = request[param]
            edit = sess.query(socres).filter(socres.id == id).update(data, synchronize_session=False)
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
                'message': "socres is not registered"
            }
            return ret
    except Exception as e:
        sess.rollback()
        ret = {
            'status': 200,
            'message': e.args,
        }
        return ret
    finally:
        sess.close()


def delete_socres(id):
    try:
        selected_socres = sess.query(socres).filter(socres.id == id).first()
        if selected_socres is not None:
            sess.delete(selected_socres)
            sess.commit()
            ret = {
                'status': 200,
                'message': 'Data deleted!'
            }
            return ret
        else:
            ret = {
                'status': 200,
                'message': "socres is not registered"
            }
            return ret
    except Exception as e:
        sess.rollback()
        ret = {
            'status': 200,
            'message': e.args
        }
        return ret
    finally:
        sess.close()
