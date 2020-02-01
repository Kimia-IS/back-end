from db_config import db, sess
from sqlalchemy import ForeignKey


class research(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    lecturer_nip = db.Column(db.String(255), ForeignKey("lecturer.nip"), unique=False)
    year = db.Column(db.String(255), unique=False)
    title = db.Column(db.String(255), unique=False)
    investor = db.Column(db.String(255), unique=False)
    amount = db.Column(db.String(255), unique=False)
    position = db.Column(db.String(255), unique=False)
    filepath = db.Column(db.String(255), unique=False)

    def save(self):
        try:
            check_research = sess.query(research).filter(research.lecturer_nip == self.lecturer_nip). \
                filter(research.title == self.title).first()
            if check_research is None:
                sess.add(self)
                sess.commit()

                files = research_file(research_id=self.id, filepath=self.filepath)
                new_research = {
                    'id': self.id,
                    'lecturer_nip': self.lecturer_nip,
                    'title': self.title,
                    'investor': self.investor,
                    'amount': self.amount,
                    'position': self.position,
                    'year': self.year,
                    'term': self.term,
                }
                ret = {
                    'status': 200,
                    'message': 'New Research Registered',
                    'results': [new_research, files.save()]
                }
            else:
                ret = {
                    'status': 200,
                    'message': 'Your research already registered before, please try again another research!'
                }
            return ret
        except Exception as e:
            ret = {
                'status': 200,
                'message': e.args
            }
            return ret


class research_file(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    research_id = db.Column(db.String(255), ForeignKey("research.id"), unique=False)
    filepath = db.Column(db.String(255), unique=False)

    def save(self):
        try:
            sess.add(self)
            sess.commit()
            res = {
                'research_id': self.research_id,
                'filepath': self.filepath
            }
            return res
        except Exception as e:
            res = {
                'status': 200,
                'message': e.args
            }
            return res


def get_all_research():
    try:
        research_datas = sess.query(research, research_file).filter(research.id == research_file.research_id).all()

        research_res = []
        for data in research_datas:
            res = {
                'id': data.research.id,
                'lecturer_nip': data.research.lecturer_nip,
                'title': data.research.title,
                'investor': data.research.investor,
                'amount': data.research.amount,
                'position': data.research.position,
                'year': data.research.year,
                'term': data.research.term,
                'filepath': data.research_file_filepath
            }
            research_res.append(res)
        ret = {
            'status': 200,
            'message': 'These are the registered research',
            'results': research_res
        }
        return ret
    except Exception as e:
        ret = {
            'status': 200,
            'message': e.args
        }
        return ret


def get_research_byID(id):
    try:
        research_datas = sess.query(research, research_file).filter(research.id == id). \
            filter(research.id == research_file.research_id).first()

        res = {
            'id': research_datas.research.id,
            'lecturer_nip': research_datas.research.lecturer_nip,
            'title': research_datas.research.title,
            'investor': research_datas.research.investor,
            'amount': research_datas.research.amount,
            'position': research_datas.research.position,
            'year': research_datas.year,
            'term': research_datas.research.term,
            'filepath': research_datas.research_file.filepath
        }
        ret = {
            'status': 200,
            'message': 'These are the registered research',
            'results': res
        }
        return ret
    except Exception as e:
        ret = {
            'status': 200,
            'message': e.args
        }
        return ret


def edit_research(id, request):
    try:
        selected_research = sess.query(research).filter(research.id == id).first()
        if selected_research is not None:
            data = {}
            for k in request.keys():
                param = k
                data[k] = request[param]
            edit = sess.query(research).filter(research.id == id).update(data, synchronize_session=False)
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
                'message': "Research is not registered"
            }
            return ret
    except Exception as e:
        ret = {
            'status': 200,
            'message': e.args,
        }
        return ret


def edit_research_file(id, filepath):
    try:
        selected_research = sess.query(research_file).filter(research_file.research_id == id).first()
        if selected_research is not None:
            data = {
                'filepath': filepath
            }
            edit = sess.query(research_file).filter(research_file.research_id == id).update(data, synchronize_session=False)
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
                'message': "Research is not registered"
            }
            return ret
    except Exception as e:
        ret = {
            'status': 200,
            'message': e.args,
        }
        return ret


def delete_research(id):
    try:
        selected_research = sess.query(research).filter(research.id == id).first()
        if selected_research is not None:
            sess.delete(selected_research)
            sess.commit()
            ret = {
                'status': 200,
                'message': 'Data deleted!'
            }
            return ret
        else:
            ret = {
                'status': 200,
                'message': "Research is not registered"
            }
            return ret
    except Exception as e:
        ret = {
            'status': 200,
            'message': e.args
        }
        return ret