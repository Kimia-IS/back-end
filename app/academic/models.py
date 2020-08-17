from db_config import db, sess
from auth.models import lecturer
from sqlalchemy import ForeignKey


class academic(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    course_id = db.Column(db.String(255), unique=True, nullable=False, primary_key=True)
    course_name = db.Column(db.String(255), nullable=False)
    total_classes = db.Column(db.Integer, nullable=False)

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
                'total_classes': self.total_classes
            }
            ret = {
                'status': 200,
                'message': 'Course Registered',
                'results': new_course
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
            sess.rollback()
            ret = {
                'status': 200,
                'message': e.args,
            }
            return ret
        finally:
            sess.close()

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
            sess.rollback()
            ret = {
                'status': 200,
                'message': e.args
            }
            return ret
        finally:
            sess.close()


class academic_lecturer(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    course_id = db.Column(db.String(255),ForeignKey("academic.course_id"), unique=True, nullable=False)
    course_class = db.Column(db.Integer, unique=True, nullable=False)
    lecturer_nip = db.Column(db.String(255), ForeignKey("lecturer.nip"), unique=True, nullable=False)
    lecturer_credit = db.Column(db.String(255), nullable=False)
    total_credit = db.Column(db.Integer, nullable=False)

    def save(self):
        try:
            check_course = sess.query(academic).filter(academic.course_id == self.course_id).first()
            if check_course is None:
                ret = {
                    'status': 200,
                    'message': "Course is not registered yet, try again another Course"
                }
                return ret
            check_lecturer = sess.query(academic_lecturer).filter(academic_lecturer.course_id == self.course_id,
                                                                  academic_lecturer.lecturer_nip == self.lecturer_nip).first()
            if check_lecturer is not None:
                ret = {
                    'status': 200,
                    'message': 'You have already registered for this course!'
                }
                return ret
            sess.add(self)
            sess.commit()
            new_academic_lecturer = {
                'id': self.id,
                'course_id': self.course_id,
                'course_name': check_course.course_name,
                'course_class': self.course_class,
                'lecturer_nip': self.lecturer_nip,
                'lecturer_credit': self.lecturer_credit,
                'total_credit': self.total_credit,
            }
            ret = {
                'status': 200,
                'message': 'New Academic Lecturer Registered',
                'results': new_academic_lecturer
            }
            return ret
        except Exception as e:
            sess.rollback
            ret = {
                'status': 200,
                'message': e.args,
            }
            return ret
        finally:
            sess.close()

    def edit(self, id, request):
        try:
            selected_academic_lecturer = sess.query(academic_lecturer).filter(academic_lecturer.id == id).first()
            if selected_academic_lecturer is not None:
                data = {}
                for k in request.keys():
                    param = k
                    data[k] = request[param]
                edit = sess.query(academic_lecturer).filter(academic_lecturer.id == id).update(data, synchronize_session=False)
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
                    'message': "Academic Lecturer is not registered"
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

    def delete(self, id):
        try:
            selected_academic_lecturer = sess.query(academic_lecturer).filter(academic_lecturer.id == id).first()
            if selected_academic_lecturer is not None:
                sess.delete(selected_academic_lecturer)
                sess.commit()
                ret = {
                    'status': 200,
                    'message': 'Data deleted!'
                }
                return ret
            else:
                ret = {
                    'status': 200,
                    'message': "Academic Lecturer is not registered"
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


def get_academicCourses_byID(id):
    try:
        data = sess.query(academic).filter(academic.id == id).first()
        if data is not None:
            res = {
                'id': data.id,
                'course_id': data.course_id,
                'course_name': data.course_name,
                'total_classes': data.total_classes
            }
            ret = {
                'status': 200,
                'message': 'This is the selected academic lecturer',
                'results': res
            }
            return ret
        else:
            ret ={
                'status': 200,
                'message': 'ID is not registered'
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


def get_academicLecturer_byID(id):
    try:
        data = sess.query(academic, lecturer, academic_lecturer).filter(academic_lecturer.id == id). \
            filter(academic.course_id == academic_lecturer.course_id). \
            filter(lecturer.nip == academic_lecturer.lecturer_nip).first()
        if data is not None:
            res = {
                'id': data.academic_lecturer.id,
                'course_id': data.academic.course_id,
                'course_name': data.academic.course_name,
                'total_credit': data.academic_lecturer.total_credit,
                'class': data.academic_lecturer.course_class,
                'lecturer(s)': data.lecturer.name,
                'lecturer_credit': data.academic_lecturer.lecturer_credit
            }
            ret = {
                'status': 200,
                'message': 'This is the selected course',
                'results': res
            }
            return ret
        else:
            ret ={
                'status': 200,
                'message': 'ID is not registered'
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


def get_all_academic_lecturer():
    try:
        datas = sess.query(academic, lecturer, academic_lecturer).\
            filter(academic.course_id == academic_lecturer.course_id).\
            filter(lecturer.nip == academic_lecturer.lecturer_nip).all()
        res = []
        for data in datas:
            temp = {
                'id': data.academic_lecturer.id,
                'course_id': data.academic.course_id,
                'course_name': data.academic.course_name,
                'total_credit': data.academic_lecturer.total_credit,
                'class': data.academic_lecturer.course_class,
                'lecturer(s)': data.lecturer.name,
                'lecturer_credit': data.academic_lecturer.lecturer_credit
            }
            res.append(temp)
        ret = {
            'status': 200,
            'message': 'This are the registered academic lecturer',
            'results': res
        }
        return ret
    except Exception as e:
        ret = {
            'status': 200,
            'message': e.args,
        }
        return ret
    finally:
        sess.close()


def get_all_courses():
    try:
        datas = sess.query(academic).all()
        res = []
        for data in datas:
            temp = {
                'id': data.id,
                'course_id': data.course_id,
                'course_name': data.course_name,
                'total_classes': data.total_classes
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
    finally:
        sess.close()


def get_academic_byLecturer(nip):
    try:
        datas = sess.query(academic, lecturer, academic_lecturer).filter(academic_lecturer.lecturer_nip == nip).\
            filter(academic.course_id == academic_lecturer.course_id).\
            filter(lecturer.nip == academic_lecturer.lecturer_nip).all()
        if datas is not None:
            res = []
            for data in datas:
                temp = {
                    'id': data.academic_lecturer.id,
                    'course_id': data.academic.course_id,
                    'course_name': data.academic.course_name,
                    'total_credit': data.academic_lecturer.total_credit,
                    'class': data.academic_lecturer.course_class,
                    'lecturer(s)': data.lecturer.name,
                    'lecturer_credit': data.academic_lecturer.lecturer_credit
                }
                res.append(temp)
            ret = {
                'status': 200,
                'message': 'These are the registered academic lecturer',
                'results': res
            }
            return ret
        else:
            ret = {
                'status': 200,
                'message': 'ID is not registered'
            }
            return ret
    except Exception as e:
        ret = {
            'status': 200,
            'message': e.args,
        }
        return ret
    finally:
        sess.close()
