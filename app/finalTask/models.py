from sqlalchemy import ForeignKey
from db_config import db, sess


class finalTask(db.Model):
    __tablename__ = 'final_task'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    student_name = db.Column(db.String(255), nullable=False)
    student_nim = db.Column(db.String(255), nullable=False)
    student_type = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    starting_date = db.Column(db.Date, nullable=False)
    graduation_date = db.Column(db.Date, nullable=False)

    def save(self):
        try:
            sess.add(self)
            sess.commit()
            new_final_task = {
                'id': self.id,
                'student_name': self.student_name,
                'student_nim': self.student_nim,
                'student_type': self.student_type,
                'title': self.title,
                'starting_date': self.starting_date,
                'graduation_date': self.graduation_date
            }
            ret = {
                'status': 200,
                'message': 'New Final Task Registered',
                'results': new_final_task
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


class finalTask_lecturer(db.Model):
    __tablename__ = 'final_task_lecturer'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    final_task_id = db.Column(db.Integer, ForeignKey("final_task.id"), nullable=False)
    lecturer_nip = db.Column(db.String(255), nullable=False)
    lecturer_position = db.Column(db.String(255), nullable=False)

    def save(self):
        try:
            sess.add(self)
            sess.commit()
            new_final_task_lecturer = {
                'id': self.id,
                'final_task_id': self.final_task_id,
                'lecturer_nip': self.lecturer_nip,
                'lecturer_position': self.lecturer_position,
            }
            ret = {
                'status': 200,
                'message': 'New Final Task Lecturer Registered',
                'results': "Sukses"
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


class finalTask_file(db.Model):
    __tablename__ = 'final_task_file'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    final_task_id = db.Column(db.Integer, ForeignKey("final_task.id"), nullable=False)
    file_path = db.Column(db.String(255), nullable=False)

    def save(self):
        try:
            sess.add(self)
            sess.commit()
            new_final_task_path = {
                'id': self.id,
                'final_task_id': self.final_task_id,
                'file_path': self.file_path,
            }
            ret = {
                'status': 200,
                'message': 'New Final Task File Saved',
                'results': new_final_task_path
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


def get_finalTask_byID(id):
    try:
        data = sess.query(finalTask, finalTask_file, finalTask_lecturer).filter(finalTask.id == id).\
            filter(finalTask.id == finalTask_file.final_task_id).\
            filter(finalTask.id == finalTask_lecturer.final_task_id).first()
        res = {
            'final_task_id': data.finalTask.id,
            'student_name': data.finalTask.student_name,
            'student_nim': data.finalTask.student_nim,
            'student_type': data.finalTask.student_type,
            'title': data.finalTask.title,
            'lecturer_nip': data.finalTask_lecturer.lecturer_nip,
            'lecturer_position': data.finalTask_lecturer.lecturer_position,
            'file_path': data.finalTask_file.file_path,
            'starting_date': data.finalTask.starting_date,
            'graduation_date': data.finalTask.graduation_date,
        }
        ret = {
            'status': 200,
            'message': 'This is the registered final tasks',
            'results': res
        }
        return ret
    except Exception as e:
        ret = {
            'status': 500,
            'message': e.args,
        }
        return ret
    finally:
        sess.close()


def get_finalTask_byLecturer(nip):
    try:
        datas = sess.query(finalTask, finalTask_file, finalTask_lecturer).\
            filter(finalTask_lecturer.lecturer_nip == nip).filter(finalTask.id == finalTask_lecturer.id).\
            filter(finalTask.id == finalTask_file.final_task_id).filter(finalTask.id == finalTask_lecturer.final_task_id).\
            all()
        if datas is not None:
            res = []
            for data in datas:
                temp = {
                    'final_task_id': data.finalTask.id,
                    'student_name': data.finalTask.student_name,
                    'student_nim': data.finalTask.student_nim,
                    'student_type': data.finalTask.student_type,
                    'title': data.finalTask.title,
                    'lecturer_nip': data.finalTask_lecturer.lecturer_nip,
                    'lecturer_position': data.finalTask_lecturer.lecturer_position,
                    'file_path': data.finalTask_file.file_path,
                    'starting_date': data.finalTask.starting_date,
                    'graduation_date': data.finalTask.graduation_date,
                }
                res.append(temp)
            ret = {
                'status': 200,
                'message': 'This is the registered finalTask that managed by lecturer ',
                'results': res
            }
            return ret
        else:
            ret = {
                'status': 400,
                'message': 'nip is not registered'
            }
            return ret
    except Exception as e:
        ret = {
            'status': 400,
            'message': e.args,
        }
        return ret
    finally:
        sess.close()


def get_all_final_task():
    try:
        final_task = sess.query(finalTask, finalTask_file, finalTask_lecturer).\
            filter(finalTask.id == finalTask_file.final_task_id).\
            filter(finalTask.id == finalTask_lecturer.final_task_id).all()
        res = []
        for data in final_task:
            temp = {
                'final_task_id': data.finalTask.id,
                'student_name': data.finalTask.student_name,
                'student_nim': data.finalTask.student_nim,
                'student_type': data.finalTask.student_type,
                'title': data.finalTask.title,
                'lecturer_nip': data.finalTask_lecturer.lecturer_nip,
                'lecturer_position': data.finalTask_lecturer.lecturer_position,
                'file_path': data.finalTask_file.file_path,
                'starting_date': data.finalTask.starting_date,
                'graduation_date': data.finalTask.graduation_date,
            }
            res.append(temp)
        ret = {
            'status': 200,
            'message': 'these are the registered final tasks',
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


def edit_final_task(id, request):
    try:
        selected_final_task = sess.query(finalTask).filter(finalTask.id == id)
        if selected_final_task.first() is not None:
            data_finalTask = {}
            data_finalTask['student_name'] = request['student_name']
            data_finalTask['student_nim'] = request['student_nim']
            data_finalTask['student_type'] = request['student_type']
            data_finalTask['title'] = request['title']
            data_finalTask['starting_date'] = request['starting_date']
            data_finalTask['graduation_date'] = request['graduation_date']

            data_finalTaskLecturer = {}
            data_finalTaskLecturer['lecturer_nip'] = request['lecturer_nip']
            data_finalTaskLecturer['lecturer_position'] = request['lecturer_position']

            # data_finalTaskFile = {}
            # data_finalTaskLecturer['file_path'] = request['file_path']

            # for k in request.keys():
            #     param = k
            #     data_finalTask[k] = request[param]

            editFinalTask = selected_final_task.update(data_finalTask, synchronize_session=False)
            editFinalTaskLecturer = edit_final_task_lecturer(id, data_finalTaskLecturer)
            # editFinalTaskFile = edit_final_task_lecturer(id, data_finalTaskFile)

            sess.commit()
            if ((editFinalTask == 1) and (editFinalTaskLecturer['status'] == 200)):
                # and (editFinalTaskFile.status == 200)):
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
                'status': 400,
                'message': "Final Task is not registered"
            }
            return ret
    except Exception as e:
        sess.rolback()
        ret = {
            'status': 500,
            'message': e.args,
        }
        return ret
    finally:
        sess.close()


def edit_final_task_lecturer(id, request):
    try:
        selected_final_task_lecturer = sess.query(finalTask_lecturer).filter(finalTask_lecturer.final_task_id == id)
        if selected_final_task_lecturer.first() is not None:
            # data_finalTask = {}
            # for k in request.keys():
            #     param = k
            #     data_finalTask[k] = request[param]
            # edit = selected_final_task_lecturer.update(data_finalTask, synchronize_session=False)
            edit = selected_final_task_lecturer.update(request, synchronize_session=False)
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
                'status': 400,
                'message': "Final Task is not registered"
            }
            return ret
    except Exception as e:
        sess.rollback()
        ret = {
            'status': 500,
            'message': e.args,
        }
        return ret
    finally:
        sess.close()


def edit_final_task_file(id, request):
    try:
        selected_final_task_file = sess.query(finalTask_file).filter(finalTask_file.final_task_id == id)
        if selected_final_task_file.first() is not None:
            data_finalTask = {}
            for k in request.keys():
                param = k
                data_finalTask[k] = request[param]
            edit = selected_final_task_file.update(data_finalTask, synchronize_session=False)
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
                'status': 500,
                'message': "Final Task is not registered"
            }
            return ret
    except Exception as e:
        sess.rollback()
        ret = {
            'status': 500,
            'message': e.args,
        }
        return ret
    finally:
        sess.close()


def deleteTask(id):
    try:
        selected_final_task = sess.query(finalTask).filter(finalTask.id == id).first()
        if selected_final_task is not None:
            sess.delete(selected_final_task)
            sess.commit()
            ret = {
                'status': 200,
                'message': 'Data deleted!'
            }
            return ret
        else:
            ret = {
                'status': 200,
                'message': "Final Task is not registered"
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


def deleteTask_lecturer(id):
    try:
        selected_final_task_lecturer = sess.query(finalTask_lecturer).filter(finalTask_lecturer.final_task_id == id).first()
        if selected_final_task_lecturer is not None:
            sess.delete(selected_final_task_lecturer)
            sess.commit()
            ret = {
                'status': 200,
                'message': 'Data deleted!'
            }
            return ret
        else:
            ret = {
                'status': 200,
                'message': "Final Task Lecturer is not registered"
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


def deleteTask_file(id):
    try:
        selected_final_task_file = sess.query(finalTask_file).filter(finalTask_file.final_task_id == id).first()
        if selected_final_task_file is not None:
            sess.delete(selected_final_task_file)
            sess.commit()

            ret = {
                'status': 200,
                'message': 'Data deleted!'
            }
            return ret
        else:
            ret = {
                'status': 200,
                'message': "Final Task File is not registered"
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


def count_final_task():
    return sess.query(finalTask).count()
