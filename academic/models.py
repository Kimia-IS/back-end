from db_config import db, sess


class academic (db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    course_id = db.Column(db.String, unique=True, nullable=False)
    course_name = db.Column(db.String, nullable=False)
    total_credit = db.Column(db.Integer, nullable=False)

    def save(self):
        try:
            check_course = sess.query(academic).filter(academic.course_id == self.course_id).first()
            if check_course is not None:
                ret = {
                    'status': 200,
                    'message': "Course already registered, try again another Course"
                }
                return ret
            sess.add(self)
            sess.commit()
            new_course = {
                'id': self.id,
                'course_id': self.course_id,
                'course_name': self.course_name,
                'total_creadit': self.total_credit
            }
            ret = {
                'status': 200,
                'message': 'Course Registered',
                'new_course': new_course
            }
            return ret
        except Exception as e:
            ret = {
                'status': 200,
                'message': e.args,
            }
            return ret

