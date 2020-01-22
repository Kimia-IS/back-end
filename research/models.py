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
                    'investor':  self.investor,
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
                 'filepath':data.research_file_filepath
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