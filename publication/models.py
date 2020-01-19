from db_config import db, sess
from sqlalchemy import ForeignKey
import ast


class journal(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    lecturer_nip = db.Column(db.String(255), ForeignKey('lecturer.nip'), unique=False)
    year = db.Column(db.String(255), unique=False)
    issue = db.Column(db.String(255), unique=False, nullable=True)
    total_page = db.Column(db.String(255), unique=False, nullable=True)
    type = db.Column(db.String(255), unique=False)
    doi = db.Column(db.String(255), unique=False, nullable=True)
    link = db.Column(db.String(255), unique=False)
    filepath = db.Column(db.String(255), unique=False)

    def save(self):
        try:
            check_journal = sess.query(journal).filter(journal.lecturer_nip == self.lecturer_nip).\
                filter(journal.title == self.title).first()
            if check_journal is None:
                sess.add(self)
                sess.commit()
                new_journal = {
                    'id': self.id,
                    'lecturer_nip': self.lecturer_nip,
                    'title': self.title,
                    'issue': self.issue,
                    'year': self.year,
                    'total_page': self.total_page,
                    'type': self.type,
                    'doi': self.doi,
                    'link': self.link,
                    'filepath': self.filepath
                }
                ret = {
                    'status': 200,
                    'message': 'New Journal Registered',
                    'results': new_journal
                }
            else:
                ret = {
                    'status': 200,
                    'message': 'Your jornal already registered before, please try again another journal!'
                }
            return ret
        except Exception as e:
            ret ={
                'status': 200,
                'message': e.args
            }
            return ret


class journal_corresponding_author(db.Model):
    id = db.Column(db.Integer, unique=False)
    journal_id = db.Column(db.Integer, ForeignKey('journal.id'), unique=False)
    names = db.Column(db.String(255), unique=False)

    def save(self):
        try:
            check_journal = sess.query(journal).filter(journal.id == self.journal_id).first()
            if check_journal is not None:
                sess.add(self)
                sess.commit()
                new_journal_corresponding_author = {
                    'id': check_journal.id,
                    'lecturer_nip': check_journal.lecturer_nip,
                    'title': check_journal.title,
                    'issue': check_journal.issue,
                    'year': check_journal.year,
                    'total_page': check_journal.total_page,
                    'type': check_journal.type,
                    'doi': check_journal.doi,
                    'link': check_journal.link,
                    'filepath': check_journal.filepath,
                    'corresponding_author': ast.literal_eval(self.names)
                }
                ret = {
                    'status': 200,
                    'message': 'New Corresponding Author Registered',
                    'results': new_journal_corresponding_author
                }
            else:
                ret = {
                    'status': 200,
                    'message': 'Your journal is not registered yet, please input your journal first!'
                }
            return ret
        except Exception as e:
            ret ={
                'status': 200,
                'message': e.args
            }
            return ret


class patent(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    lecturer_nip = db.Column(db.String(255), ForeignKey('lecturer.nip'), unique=False)
    status = db.Column(db.String(255), unique=False)
    publisher = db.Column(db.String(255), unique=False)
    year = db.Column(db.String(255), unique=False)
    filepath = db.Column(db.String(255), unique=False)

    def save(self):
        try:
            check_journal = sess.query(journal).filter(journal.lecturer_nip == self.lecturer_nip).\
                filter(journal.title == self.title).first()
            if check_journal is None:
                sess.add(self)
                sess.commit()
                new_journal = {
                    'id': self.id,
                    'lecturer_nip': self.lecturer_nip,
                    'title': self.title,
                    'issue': self.issue,
                    'year': self.year,
                    'total_page': self.total_page,
                    'type': self.type,
                    'doi': self.doi,
                    'link': self.link,
                    'filepath': self.filepath
                }
                ret = {
                    'status': 200,
                    'message': 'New Journal Registered',
                    'results': new_journal
                }
            else:
                ret = {
                    'status': 200,
                    'message': 'Your jornal already registered before, please try again another journal!'
                }
            return ret
        except Exception as e:
            ret ={
                'status': 200,
                'message': e.args
            }
            return ret

class other_publication(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    lecturer_nip = db.Column(db.String(255), ForeignKey('lecturer.nip'), unique=False)
    date = db.Column(db.Date, unique=False)
    publisher = db.Column(db.String(255), unique=False)
    filepath = db.Column(db.String(255), unique=False)