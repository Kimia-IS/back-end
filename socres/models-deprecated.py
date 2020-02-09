# from db_config import db, sess
# from sqlalchemy import ForeignKey


# class social_responsibility(db.Model):
#     id = db.Column(db.Integer, unique=True, primary_key=True)
#     year = db.Column(db.String(255), unique=False)
#     title = db.Column(db.String(255), unique=False)
#     lecturer_nip = db.Column(db.String(255), ForeignKey('lecturer.nip'), unique=False)
#     investor = db.Column(db.String(255), unique=False)
#     amount = db.Column(db.String(255), unique=False)
#     position = db.Column(db.String(255), unique=False)
#     filepath = db.Column(db.String(255), unique=False)
#     other_parties = db.Column(db.String(255), unique=False)

#     def save(self):
#         try:
#             check_socres = sess.query(social_responsibility).filter(
#                 social_responsibility.lecturer_nip == self.lecturer_nip). \
#                 filter(social_responsibility.title == self.title).first()
#             if check_socres is None:
#                 save = True
#                 for data in self.filepath:
#                     files = social_responsibility_file(socres_id=self.id, filepath=data)
#                     save = save and files.save()
#                 for data in self.other_parties:
#                     other_parties = social_responsibility_other_parties(socres_id=self.id, name=data)
#                     save = save and other_parties.save()
#                 new_socres = {
#                     'id': self.id,
#                     'lecturer_nip': self.lecturer_nip,
#                     'title': self.title,
#                     'investor': self.investor,
#                     'amount': self.amount,
#                     'position': self.position,
#                     'year': self.year,
#                     'term': self.term,
#                 }
#                 if save:
#                     sess.add(new_socres)
#                     sess.commit()
#                     ret = {
#                         'status': 200,
#                         'message': 'New Social Responsibility Registered',
#                         'results': new_socres
#                     }
#                 else:
#                     ret = {
#                         'status': 200,
#                         'message': 'Saving failed'
#                     }
#             else:
#                 ret = {
#                     'status': 200,
#                     'message': 'Your Social Responsibility already registered before, '
#                                'please try again another Social Responsibility!'
#                 }
#             return ret
#         except Exception as e:
#             ret = {
#                 'status': 200,
#                 'message': e.args
#             }
#             return ret


# class social_responsibility_file(db.Model):
#     id = db.Column(db.Integer, unique=True, primary_key=True)
#     socres_id = db.Column(db.Integer, unique=False)
#     filepath = db.Column(db.String(255), unique=False)

#     def save(self):
#         try:
#             sess.add(self)
#             sess.commit()
#             return True
#         except Exception as e:
#             return False


# class social_responsibility_other_parties(db.Model):
#     id = db.Column(db.Integer, unique=True, primary_key=True)
#     socres_id = db.Column(db.Integer, unique=False)
#     name = db.Column(db.String(255), unique=False)

#     def save(self):
#         try:
#             sess.add(self)
#             sess.commit()
#             return True
#         except Exception as e:
#             return False

#     def save_additional_parties(self):
#         try:
#             check_socres = sess.query(social_responsibility).filter(social_responsibility.id == self.socres_id).first()
#             if check_socres is not None:
#                 sess.add(self)
#                 sess.commit()

#                 new_socres_parties = {
#                     'id': self.id,
#                     'socres_id': self.socres_id,
#                     'name': self.name
#                 }
#                 ret = {
#                     'status': 200,
#                     'message': 'New socres parties Registered',
#                     'results': new_socres_parties
#                 }
#             else:
#                 ret = {
#                     'status': 200,
#                     'message': 'Your socres has not registered before, please try again another socres!'
#                 }
#             return ret
#         except Exception as e:
#             ret = {
#                 'status': 200,
#                 'message': e.args
#             }
#             return ret


# def get_all_socres():
#     try:
#         socreses = sess.query(social_responsibility, social_responsibility_file, social_responsibility_other_parties). \
#             filter(social_responsibility.id == social_responsibility_file.socres_id). \
#             filter(social_responsibility.id == social_responsibility_other_parties.socres_id).all()
#         socreses_res = []
#         for data in socreses:
#             res = {
#                 'id': data.social_responsibility.id,
#                 'lecturer_nip': data.social_responsibility.lecturer_nip,
#                 'title': data.social_responsibility.title,
#                 'investor': data.research.investor,
#                 'amount': data.research.amount,
#                 'position': data.research.position,
#                 'year': data.research.year,
#                 'filepath': data.social_responsibility_file.filepath,
#                 'other_parties': data.social_responsibility_other_parties.name
#             }
#             socreses_res.append(res)
#         ret = {
#             'status': 200,
#             'message': 'These are the registered socres',
#             'results': socreses_res
#         }
#         return ret

#     except Exception as e:
#         ret = {
#             'status': 200,
#             'message': e.args
#         }
#         return ret


# def get_socres_byID(id):
#     try:
#         socreses = sess.query(social_responsibility, social_responsibility_file, social_responsibility_other_parties). \
#             filter(social_responsibility.id == id). \
#             filter(social_responsibility.id == social_responsibility_other_parties.socres_id). \
#             filter(social_responsibility.id == social_responsibility_file.socres_id).first()

#         res = {
#             'id': socreses.research.id,
#             'lecturer_nip': socreses.research.lecturer_nip,
#             'title': socreses.research.title,
#             'investor': socreses.research.investor,
#             'amount': socreses.research.amount,
#             'position': socreses.research.position,
#             'year': socreses.research.year,
#             'term': socreses.research.term,
#             'filepath': socreses.research_file.filepath
#         }
#         ret = {
#             'status': 200,
#             'message': 'These are the registered research',
#             'results': res
#         }
#         return ret
#     except Exception as e:
#         ret = {
#             'status': 200,
#             'message': e.args
#         }
#         return ret


# def edit_socres(id, request):
#     try:
#         selected_socres = sess.query(social_responsibility).filter(social_responsibility.id == id)
#         selected_socres_file = sess.query(social_responsibility_file).filter(social_responsibility_file.id == id)
#         selected_socres_parties = sess.query(social_responsibility_other_parties).filter(
#             social_responsibility_other_parties.id == id)
#         if selected_socres.first() is not None:
#             data_socres = {}
#             data_socres_file = {}
#             data_socres_parties = {}
#             for k in request.keys():
#                 param = k
#                 if param == 'filepath':
#                     data_socres_file[param] = request[param]
#                 elif param == 'other_parties':
#                     data_socres_parties[param] = request[param]
#                 else:
#                     data_socres[param] = request[param]
#             edit = selected_socres.update(data_socres, synchronize_session=False) and \
#                    selected_socres_file.update(data_socres_file, synchronize_session=False) and \
#                    selected_socres_parties.update(data_socres_parties, synchronize_session=False)
#             sess.commit()
#             if edit == 1:
#                 ret = {
#                     'status': 200,
#                     'message': 'Data updated!'
#                 }
#             else:
#                 ret = {
#                     'status': 500,
#                     'message': "Something's went wrong with our server. Please try again later!"
#                 }
#             return ret
#         else:
#             ret = {
#                 'status': 200,
#                 'message': "Socres is not registered"
#             }
#             return ret
#     except Exception as e:
#         ret = {
#             'status': 200,
#             'message': e.args,
#         }
#         return ret


# def delete_socres(id):
#     try:
#         selected_socres = sess.query(social_responsibility).filter(social_responsibility.id == id).first()
#         if selected_socres is not None:
#             sess.delete(selected_socres)
#             sess.commit()
#             ret = {
#                 'status': 200,
#                 'message': 'Data deleted!'
#             }
#             return ret
#         else:
#             ret = {
#                 'status': 200,
#                 'message': "Social Responsibility is not registered"
#             }
#             return ret
#     except Exception as e:
#         ret = {
#             'status': 200,
#             'message': e.args
#         }
#         return ret
