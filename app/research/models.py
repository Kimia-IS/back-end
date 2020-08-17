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
    term = db.Column(db.String(255), unique=False)
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
            sess.rollback()
            ret = {
                'status': 200,
                'message': e.args
            }
            return ret
        finally:
            sess.close()


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
            sess.rollback()
            res = {
                'status': 200,
                'message': e.args
            }
            return res
        finally:
            sess.close()


def get_all_research():
    try:
        #research_datas = sess.query(research, research_file).filter(research.id == research_file.research_id).all()
        research_datas = sess.query(research).all()

        research_res = []
        for data in research_datas:
            res = {
                'id': data.id,
                'lecturer_nip': data.lecturer_nip,
                'title': data.title,
                'investor': data.investor,
                'amount': data.amount,
                'position': data.position,
                'year': data.year,
                #'term': data.term,
                'filepath': data.filepath
                #'filepath': data_file.filepath
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
    finally:
        sess.close()


def get_research_byLecturer(id):
    try:
        datas = sess.query(research).filter(research.lecturer_nip == id).all()
        if datas is not None:
            res = []
            for data in datas:
                temp = {
                    'id': data.id,
                    'lecturer_nip': data.lecturer_nip,
                    'title': data.title,
                    'investor': data.investor,
                    'amount': data.amount,
                    'position': data.position,
                    'year': data.year,
                    # 'term': data.term,
                    'filepath': data.filepath
                }
                res.append(temp)
            ret = {
                'status': 200,
                'message': 'These are the registered research',
                'results': res
            }
            return ret
        else:
            res = {
                'status': 200,
                'message': 'NIP is not registered'
            }
            return res
    except Exception as e:
        ret = {
            'status': 500,
            'message': e.args
        }
        return ret
    finally:
        sess.close()


def get_research_byID(id):
    try:
        # research_datas = sess.query(research, research_file).filter(research.id == id). \
        #     filter(research.id == research_file.research_id).first()

        research_datas = sess.query(research).filter(research.id == id).first()

        res = {
            'id': research_datas.id,
            'lecturer_nip': research_datas.lecturer_nip,
            'title': research_datas.title,
            'investor': research_datas.investor,
            'amount': research_datas.amount,
            'position': research_datas.position,
            'year': research_datas.year,
            # 'term': research_datas.term,
            'filepath': research_datas.filepath
        }
        ret = {
            'status': 200,
            'message': 'These are the registered research',
            'results': res
        }
        return ret
    except Exception as e:
        ret = {
            'status': 500,
            'message': e.args
        }
        return ret
    finally:
        sess.close()


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
        sess.rollback()
        ret = {
            'status': 200,
            'message': e.args,
        }
        return ret
    finally:
        sess.close()


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
        sess.rollback()
        ret = {
            'status': 200,
            'message': e.args,
        }
        return ret
    finally:
        sess.close()


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
        sess.rollback()
        ret = {
            'status': 200,
            'message': e.args
        }
        return ret
    finally:
        sess.close()