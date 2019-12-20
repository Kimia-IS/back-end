from db_config import db, sess
from auth.models import lecturer
import json


class academic (db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    course_id = db.Column(db.String(255), unique=True, nullable=False)
    course_name = db.Column(db.String(255), nullable=False)
    total_credit = db.Column(db.Integer, nullable=False)

    def get(self):
        try:
            datas =sess.query(academic, lecturer, academic_lecturer).filter(academic_lecturer.lecturer_nip == lecturer.nip).filter(academic.course_id == academic_lecturer.course_id).all()
            res = []
            for data in datas:
                temp = {
                    'course_id': data.academic.course_id,
                    'course_name': data.academic.course_name,
                    'class': data.academic_lecturer.course_class,
                    'lecturer(s)': data.lecturer.name,
                    'total_credit': data.academic.total_credit
                }
                res.append(temp)
            ret = {
                'status': 200,
                'message': 'This are the registered courses',
                'results': res
            }
            return ret
        except Exception as e:
            ret = {
                'status': 200,
                'message': e.args,
            }
            return ret

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
                'results': new_course
            }
            return ret
        except Exception as e:
            ret = {
                'status': 200,
                'message': e.args,
            }
            return ret

    def edit(self, academic_id, request):
        try:
            selected_course = sess.query(academic).filter(academic.id == academic_id).first()
            if selected_course is not None:
                data = {}
                for k in request.keys():
                    param = k
                    data[k] = request[param]
                edit = sess.query(academic).filter(academic.id == academic_id).update(data, synchronize_session=False)
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
                    'message': "Course ID is not registered"
                }
                return ret
        except Exception as e:
            ret = {
                'status': 200,
                'message': e.args,
            }
            return ret

    def delete(self, academic_id):
        try:
            selected_course = sess.query(academic).filter(academic.id == academic_id).first()
            if selected_course is not None:
                sess.delete(selected_course)
                sess.commit()
                ret = {
                    'status': 200,
                    'message': 'Data deleted!'
                }
                return ret
            else:
                ret = {
                    'status': 200,
                    'message': "Course ID is not registered"
                }
                return ret
        except Exception as e:
            ret = {
                'status': 200,
                'message': e.args
            }
            return ret


class academic_lecturer(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    course_id = db.Column(db.String(255), unique=True, nullable=False)
    course_class = db.Column(db.Integer, unique=True, nullable=False)
    lecturer_nip = db.Column(db.String(255), unique=True, nullable=False)
    lecturer_credit = db.Column(db.String(255), nullable=False)