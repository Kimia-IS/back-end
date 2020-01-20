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
                    'message': 'Your journal already registered before, please try again another journal!'
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
    lecturer_nip = db.Column(db.String(255), ForeignKey('lecturer.nip'), unique=False)
    title = db.Column(db.String(255), unique=True)
    status = db.Column(db.String(255), unique=False)
    publisher = db.Column(db.String(255), unique=False)
    year = db.Column(db.String(255), unique=False)
    filepath = db.Column(db.String(255), unique=False)

    def save(self):
        try:
            check_patent = sess.query(patent).filter(patent.lecturer_nip == self.lecturer_nip).\
                filter(patent.title == self.title).first()
            if check_patent is None:
                sess.add(self)
                sess.commit()
                new_patent = {
                    'id': self.id,
                    'lecturer_nip': self.lecturer_nip,
                    'title': self.title,
                    'status': self.status,
                    'year': self.year,
                    'publisher': self.publisher,
                    'filepath': self.filepath
                }
                ret = {
                    'status': 200,
                    'message': 'New Patent Registered',
                    'results': new_patent
                }
            else:
                ret = {
                    'status': 200,
                    'message': 'Your patent already registered before, please try again another patent!'
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

    def save(self):
        try:
            check_others = sess.query(other_publication).filter(other_publication.lecturer_nip == self.lecturer_nip).\
                filter(other_publication.title == self.title).first()
            if check_others is None:
                sess.add(self)
                sess.commit()
                new_other_publication = {
                    'id': self.id,
                    'lecturer_nip': self.lecturer_nip,
                    'title': self.title,
                    'date': self.date,
                    'publisher': self.publisher,
                    'filepath': self.filepath
                }
                ret = {
                    'status': 200,
                    'message': 'New Publication Registered',
                    'results': new_other_publication
                }
            else:
                ret = {
                    'status': 200,
                    'message': 'Your publication already registered before, please try again another publication!'
                }
            return ret
        except Exception as e:
            ret ={
                'status': 200,
                'message': e.args
            }
            return ret


def get_all_publication():
    try:
        journals = sess.query(journal, journal_corresponding_author).filter(journal.id == journal_corresponding_author.journal_id).all()
        patents = sess.query(patent).all()
        others = sess.query(other_publication).all()

        res = {
            'status': 200,
            'message': 'These are the registered publications',
            'results': {
                'journals': journals,
                'patents': patents,
                'other_publications': others
            }
        }

        return res
    except Exception as e:
        res = {
            'status': 200,
            'message': e.args
        }

        return res


def get_all_publication_byCat(cat):
    try:
        if cat == 'journal':
            publications = sess.query(journal, journal_corresponding_author).\
                filter(journal.id == journal_corresponding_author.journal_id).all()
        else:
            publications = sess.query(cat).all()

        res = {
            'status': 200,
            'message': 'These are the registered publications',
            'results': {
                cat: publications
            }
        }

        return res
    except Exception as e:
        res = {
            'status': 200,
            'message': e.args
        }

        return res


def get_publication_byID(cat, id):
    try:
        selected_publication = sess.query(cat).filter(cat.id==id).first()
        if cat == 'journal':
            corresponding_author = sess.query(journal_corresponding_author).filter(journal_corresponding_author.journal_id == id).first()
            res ={
                'status': 200,
                'message': 'This is the requested publication',
                'result': {
                    'category': 'journal',
                    'publication': selected_publication,
                    'corresponding_author': ast.literal_eval(corresponding_author.names)
                }
            }
        else:
            res = {
                'status': 200,
                'message': 'This is the requested publication',
                'result': {
                    'category': cat,
                    'publication': selected_publication
                }
            }
        return res
    except Exception as e:
        ret = {
            'status': 200,
            'message': e.args,
        }
        return ret


def edit_publication(cat, id, request):
    try:
        selected_publication = sess.query(cat).filter(cat.id == id).first()
        if selected_publication is not None:
            data = {}
            for k in request.keys():
                param = k
                data[k] = request[param]
            edit = sess.query(cat).filter(cat.id == id).update(data, synchronize_session=False)
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
                'message': "Publication is not registered"
            }
            return ret
    except Exception as e:
        ret = {
            'status': 200,
            'message': e.args,
        }
        return ret


def delete_experience(cat, id):
    try:
        selected_publication = sess.query(cat).filter(cat.id == id).first()
        if selected_publication is not None:
            sess.delete(selected_publication)
            sess.commit()
            ret = {
                'status': 200,
                'message': 'Data deleted!'
            }
            return ret
        else:
            ret = {
                'status': 200,
                'message': "Publication is not registered"
            }
            return ret
    except Exception as e:
        ret = {
            'status': 200,
            'message': e.args
        }
        return ret
