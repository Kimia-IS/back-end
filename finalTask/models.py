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
            db.add(self)
            db.commit()
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
            ret = {
                'status': 200,
                'message': e.args,
            }
            return ret


class finalTask_lecturer(db.Model):
    __tablename__ = 'final_task_lecturer'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    final_task_id = db.Column(db.Integer, nullable=False)
    lecturer_nip = db.Column(db.String(255), nullable=False)
    lecturer_position = db.Column(db.String(255), nullable=False)

    def save(self):
        try:
            db.add(self)
            db.commit()
            new_final_task_lecturer = {
                'id': self.id,
                'final_task_id': self.final_task_id,
                'lecturer_nip': self.lecturer_nip,
                'lecturer_position': self.lecturer_position,
            }
            ret = {
                'status': 200,
                'message': 'New Final Task Lecturer Registered',
                'results': new_final_task_lecturer
            }
            return ret
        except Exception as e:
            ret = {
                'status': 200,
                'message': e.args,
            }
            return ret


class finalTask_file(db.Model):
    __tablename__ = 'final_task_file'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    final_task_id = db.Column(db.Integer, nullable=False)
    file_path = db.Column(db.String(255), nullable=False)