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
    total_page = db.Column(db.Integer, unique=False, nullable=True)
    type = db.Column(db.String(255), unique=False)
    doi = db.Column(db.String(255), unique=False, nullable=True)
    link = db.Column(db.String(255), unique=False)
    filepath = db.Column(db.String(255), unique=False)
    names = db.Column(db.String(255), unique=False, nullable=True)

    def save(self):
        global saveJourCorr
        try:
            check_journal = sess.query(journal).filter(journal.lecturer_nip == self.lecturer_nip). \
                filter(journal.title == self.title).first()
            if check_journal is None:
                sess.add(self)
                sess.commit()
                new_journal = {
                    'lecturer_nip': self.lecturer_nip,
                    'title': self.title,
                    'issue': self.issue,
                    'year': self.year,
                    'number': self.number,
                    'total_page': self.total_page,
                    'type': self.type,
                    'doi': self.doi,
                    'link': self.link,
                    'filepath': self.filepath,
                    'names': self.names
                }
                print('before the sess.add self')
                # print('before the sess.add new_journal')
                # sess.add(new_journal)       # masalah broo
                print('lwaaatt')
                print('lwaaattasdasd')
                print('self names = ', self.names)
                print('id = ', self.id)
                
                # savejourCorr = True
                # for name in self.names:
                #     if saveJourCorr:
                #         saveJourCorr = journalCorrespondingAuthor(journal_id=self.id, names=name).save()
                #     else:
                #         return {'status': 200,
                #                 'message': 'something went wrong when we try to save corresponding author!'}
                if self.names:
                    names = self.names.split(",")
                    print('masuk if')
                    for name in names:
                        print('masukloop')
                        print('name = ', name)
                        journalCorrespondingAuthor(journal_id=self.id, names=name).save()
                # else:
                #     return {'status': 200, 'message': 'no corresponding author'}

                print('lewat')
                
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
            print('masukjournalcoor', self)
            sess.add(self)
            sess.commit()
            return True
        except Exception as e:
            return e


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
                    'year': self.year,
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
            print('masukkik journal')
            # publications = sess.query(journal, journalCorrespondingAuthor). \
            #    filter(journal.id == journalCorrespondingAuthor.journal_id).all()
            publications = sess.query(journal).all()
            res = []
            for data in publications:
                temp = {
                    'id': data.id,
                    'lecturer_nip': data.lecturer_nip,
                    'title': data.title,
                    'issue': data.issue,
                    'year': data.year,
                    'number': data.number,
                    'total_page': data.total_page,
                    'type': data.type,
                    'doi': data.doi,
                    'link': data.link,
                    'filepath': data.filepath,
                    'names': data.names
                }
                res.append(temp)
            print(res)
        elif cat == 'patent':
            print('masukkik patent')
            publications = sess.query(patent).all()
            res = []
            for data in publications:
                temp = {
                    'id': data.id,
                    'lecturer_nip': data.lecturer_nip,
                    'title': data.title,
                    'status': data.status,
                    'year': data.year,
                    'publisher': data.publisher,
                    'filepath': data.filepath
                }
                res.append(temp)
            print(res)
        elif cat == 'other':
            print('masukkik other_publication')
            publications = sess.query(other_publication).all()
            res = []
            for data in publications:
                temp = {
                    'id': data.id,
                    'lecturer_nip': data.lecturer_nip,
                    'title': data.title,
                    'year': data.year,
                    'publisher': data.publisher,
                    'filepath': data.filepath
                }
                res.append(temp)
            print(res)
        else:
            publications = 'category is not defined'

        res = {
            'status': 200,
            'message': 'These are the registered publications',
            'results': res
        }

        print('res = ', res)
        return res
    except Exception as e:
        res = {
            'status': 200,
            'message': e.args
        }

        return res


def get_publication_byLecturer(cat, id):
    try:
        print('in id = ', id)
        if cat == 'journal':
            selected_publication = sess.query(journal).filter(journal.lecturer_nip == id).first()
            # corresponding_author = sess.query(journalCorrespondingAuthor).filter(
            #     journalCorrespondingAuthor.journal_id == id).first()
            if selected_publication is not None:
                temp = {
                    'id': selected_publication.id,
                    'lecturer_nip': selected_publication.lecturer_nip,
                    'title': selected_publication.title,
                    'issue': selected_publication.issue,
                    'year': selected_publication.year,
                    'number': selected_publication.number,
                    'total_page': selected_publication.total_page,
                    'type': selected_publication.type,
                    'doi': selected_publication.doi,
                    'link': selected_publication.link,
                    'filepath': selected_publication.filepath,
                    'names': selected_publication.names
                }
                res = {
                    'status': 200,
                    'message': 'This is the requested publication',
                    # 'result': {
                    #     'category': 'journal',
                    #     'publication': selected_publication,
                    #     'corresponding_author': ast.literal_eval(corresponding_author.names)
                    # }
                    'results': temp
                }
            else:
                res = {
                    'status': 200,
                    'message': 'NIP is not registered'
                }
        elif cat == 'patent':
            selected_publication = sess.query(patent).filter(patent.lecturer_nip == id).first()
            if selected_publication is not None:
                temp = {
                    'id': selected_publication.id,
                    'lecturer_nip': selected_publication.lecturer_nip,
                    'title': selected_publication.title,
                    'status': selected_publication.status,
                    'year': selected_publication.year,
                    'publisher': selected_publication.publisher,
                    'filepath': selected_publication.filepath
                }
                res = {
                    'status': 200,
                    'message': 'This is the requested publication',
                    'results': temp
                }
            else:
                res = {
                    'status': 200,
                    'message': 'NIP is not registered'
                }
        elif cat == 'otherpub':
            selected_publication = sess.query(other_publication).filter(other_publication.lecturer_nip == id).first()
            if selected_publication is not None:
                temp = {
                    'id': selected_publication.id,
                    'lecturer_nip': selected_publication.lecturer_nip,
                    'title': selected_publication.title,
                    'year': selected_publication.year,
                    'publisher': selected_publication.publisher,
                    'filepath': selected_publication.filepath
                }
                res = {
                    'status': 200,
                    'message': 'This is the requested publication',
                    'results': temp
                }
            else:
                res = {
                    'status': 200,
                    'message': 'NIP is not registered'
                }
        else:
            res = {
                'status': 400,
                'message': 'Wrong category request'
            }

        print(res)
        return res
    except Exception as e:
        ret = {
            'status': 200,
            'message': e.args,
        }
        return ret


def get_publication_byID(cat, id):
    try:
        print('in id = ', id)
        if cat == 'journal':
            selected_publication = sess.query(journal).filter(journal.id == id).first()
            # corresponding_author = sess.query(journalCorrespondingAuthor).filter(
            #     journalCorrespondingAuthor.journal_id == id).first()
            temp = {
                'id': selected_publication.id,
                'lecturer_nip': selected_publication.lecturer_nip,
                'title': selected_publication.title,
                'issue': selected_publication.issue,
                'year': selected_publication.year,
                'number': selected_publication.number,
                'total_page': selected_publication.total_page,
                'type': selected_publication.type,
                'doi': selected_publication.doi,
                'link': selected_publication.link,
                'filepath': selected_publication.filepath,
                'names': selected_publication.names
            }
            res = {
                'status': 200,
                'message': 'This is the requested publication',
                # 'result': {
                #     'category': 'journal',
                #     'publication': selected_publication,
                #     'corresponding_author': ast.literal_eval(corresponding_author.names)
                # }
                'results': temp
            }
        elif cat == 'patent':
            selected_publication = sess.query(patent).filter(patent.id == id).first()
            temp = {
                'id': selected_publication.id,
                'lecturer_nip': selected_publication.lecturer_nip,
                'title': selected_publication.title,
                'status': selected_publication.status,
                'year': selected_publication.year,
                'publisher': selected_publication.publisher,
                'filepath': selected_publication.filepath
            }
            res = {
                'status': 200,
                'message': 'This is the requested publication',
                'results': temp
            }
        elif cat == 'other':
            selected_publication = sess.query(other_publication).filter(other_publication.id == id).first()
            temp = {
                'id': selected_publication.id,
                'lecturer_nip': selected_publication.lecturer_nip,
                'title': selected_publication.title,
                'year': selected_publication.year,
                'publisher': selected_publication.publisher,
                'filepath': selected_publication.filepath
            }
            res = {
                'status': 200,
                'message': 'This is the requested publication',
                'results': temp
            }
        else:
            res = {
                'status': 400,
                'message': 'Wrong category request'
            }

        print(res)
        return res
    except Exception as e:
        ret = {
            'status': 200,
            'message': e.args,
        }
        return ret


def edit_publication(cat, id, request):
    try:
        if cat == 'journal':
            selected_publication = sess.query(journal).filter(journal.id == id)
        elif cat == 'patent':
            selected_publication = sess.query(patent).filter(patent.id == id)
        elif cat == 'other':
            selected_publication = sess.query(other_publication).filter(other_publication.id == id)
        else:
            ret = {
                'status': 400,
                'message': "Wrong category"
            }
            return ret

        if selected_publication is not None:
            data = {}
            for k in request.keys():
                param = k
                data[k] = request[param]
            edit = selected_publication.update(data, synchronize_session=False)
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
        else:
            ret = {
                'status': 400,
                'message': "Publication is not registered"
            }
        return ret
            # if selected_publication is not None:
            #     data = {}
            #     for k in request.keys():
            #         param = k
            #         data[k] = request[param]
            #     edit = sess.query(cat).filter(cat.id == id).update(data, synchronize_session=False)
            #     sess.commit()
            #     if edit == 1:
            #         ret = {
            #             'status': 200,
            #             'message': 'Data updated!'
            #         }
            #     else:
            #         ret = {
            #             'status': 500,
            #             'message': "Something's went wrong with our server. Please try again later!"
            #         }
            #     return ret
            # else:
            #     ret = {
            #         'status': 200,
            #         'message': "Publication is not registered"
            #     }
            #     return ret
        # else:
        #     selected_journal = sess.query(cat).filter(cat.id == id)
        #     print('sel journal =', selected_journal)
        #     if selected_journal is not None:
        #         # del request['publication_files']    # exclude files
        #         data = {}
        #         dataCorr = {}
        #         for k in request.keys():
        #             param = k
        #             data[k] = request[param]
        #             # if param != 'names':
        #             #     data[k] = request[param]
        #             # else:
        #             #     dataCorr[k] = request[param]
        #         edit = selected_journal.update(data, synchronize_session=False)
        #         # edit = sess.query(journal).filter(journal.id == id).update(data, synchronize_session=False)
        #         # edit = edit and sess.query(journalCorrespondingAuthor).\
        #         #     filter(journalCorrespondingAuthor.journal_id == selected_journal.first().id).\
        #         #     update(dataCorr, synchronize_session=False)
        #         sess.commit()
        #         if edit == 1:
        #             ret = {
        #                 'status': 200,
        #                 'message': 'Data updated!'
        #             }
        #         else:
        #             ret = {
        #                 'status': 500,
        #                 'message': "Something's went wrong with our server. Please try again later!"
        #             }
        #         return ret
        #     else:
        #         ret = {
        #             'status': 200,
        #             'message': "Publication is not registered"
        #         }
        #         return ret
    except Exception as e:
        ret = {
            'status': 500,
            'message': e.args,
        }
        return ret


def delete_publication(cat, id):
    try:
        # selected_publication = sess.query(cat).filter(cat.id == id).first()
        if cat == 'journal':
            selected_publication = sess.query(journal).filter(journal.id == id).first()
        elif cat == 'patent':
            selected_publication = sess.query(patent).filter(patent.id == id).first()
        elif cat == 'other':
            selected_publication = sess.query(other_publication).filter(other_publication.id == id).first()
        else:
            ret = {
                'status': 400,
                'message': "Wrong category"
            }
            return ret
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
