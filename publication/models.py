from db_config import db, sess
from sqlalchemy import ForeignKey
import ast


class journal(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    lecturer_nip = db.Column(db.String(255), ForeignKey('lecturer.nip'), unique=False)
    year = db.Column(db.String(5), unique=False)
    number = db.Column(db.String(255), unique=False)
    issue = db.Column(db.Integer, unique=False, nullable=True)
    type = db.Column(db.String(255), unique=False)
    doi = db.Column(db.String(255), unique=False, nullable=True)
    link = db.Column(db.String(255), unique=False)
    filepath = db.Column(db.String(255), unique=False)
    names = db.Column(db.String(255), unique=False)

    def save(self):
        global saveJourCorr
        try:
            check_journal = sess.query(journal).filter(journal.lecturer_nip == self.lecturer_nip). \
                filter(journal.title == self.title).first()
            if check_journal is None:
                new_journal = {
                    'id': self.id,
                    'lecturer_nip': self.lecturer_nip,
                    'title': self.title,
                    'issue': self.issue,
                    'year': self.year,
                    'number': self.number,
                    'total_page': self.total_page,
                    'type': self.type,
                    'doi': self.doi,
                    'link': self.link,
                    'filepath': self.filepath
                }
                savejourCorr = True
                for name in self.names:
                    if saveJourCorr:
                        saveJourCorr = journalCorrespondingAuthor(journal_id=self.id, names=name).save()
                    else:
                        return {'status': 200,
                                'message': 'something went wrong when we try to save corresponding author!'}

                sess.add(new_journal)
                sess.commit()
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
            ret = {
                'status': 200,
                'message': e.args
            }
            return ret


class journalCorrespondingAuthor(db.Model):
    __tablename__ = 'journal_corr_author'
    id = db.Column(db.Integer, unique=False, primary_key=True)
    journal_id = db.Column(db.Integer, ForeignKey('journal.id'), unique=False)
    names = db.Column(db.String(255), unique=False)

    def save(self):
        try:
            sess.add(self)
            sess.commit()
            return True
        except Exception as e:
            return False


class patent(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    lecturer_nip = db.Column(db.String(255), ForeignKey('lecturer.nip'), unique=False)
    title = db.Column(db.String(255), unique=True)
    status = db.Column(db.String(255), unique=False)
    publisher = db.Column(db.String(255), unique=False)
    year = db.Column(db.String(5), unique=False)
    filepath = db.Column(db.String(255), unique=False)

    def save(self):
        try:
            check_patent = sess.query(patent).filter(patent.lecturer_nip == self.lecturer_nip). \
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
            ret = {
                'status': 200,
                'message': e.args
            }
            return ret


class other_publication(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    lecturer_nip = db.Column(db.String(255), ForeignKey('lecturer.nip'), unique=False)
    year = db.Column(db.String(5), unique=False)
    publisher = db.Column(db.String(255), unique=False)
    filepath = db.Column(db.String(255), unique=False)

    def save(self):
        try:
            check_others = sess.query(other_publication).filter(other_publication.lecturer_nip == self.lecturer_nip). \
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
            ret = {
                'status': 200,
                'message': e.args
            }
            return ret


def get_all_publication():
    try:
        journals = sess.query(journal, journalCorrespondingAuthor).filter(
            journal.id == journalCorrespondingAuthor.journal_id).all()
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
            publications = sess.query(journal, journalCorrespondingAuthor). \
                filter(journal.id == journalCorrespondingAuthor.journal_id).all()
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
        selected_publication = sess.query(cat).filter(cat.id == id).first()
        if cat == 'journal':
            corresponding_author = sess.query(journalCorrespondingAuthor).filter(
                journalCorrespondingAuthor.journal_id == id).first()
            res = {
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
        if cat != 'journal':
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
        else:
            selected_journal = sess.query(journal).filter(journal.id == id)
            if selected_journal is not None:
                data = {}
                dataCorr = {}
                for k in request.keys():
                    param = k
                    if param != 'names':
                        data[k] = request[param]
                    else:
                        dataCorr[k] = request[param]
                edit = sess.query(journal).filter(journal.id == id).update(data, synchronize_session=False)
                edit = edit and sess.query(journalCorrespondingAuthor).\
                    filter(journalCorrespondingAuthor.journal_id == selected_journal.first().id).\
                    update(dataCorr, synchronize_session=False)
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


def delete_publication(cat, id):
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


def count_journal():
    return sess.query(journal).count()
