from sqlalchemy import ForeignKey
from db_config import db, sess


class achievement(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    lecturer_nip = db.Column(db.String(255), ForeignKey("lecturer.nip"), unique=False)
    title = db.Column(db.String(255), unique=False)
    issuer = db.Column(db.String(255), unique=False)
    year = db.Column(db.String(255), unique=False)
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