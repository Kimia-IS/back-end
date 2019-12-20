from db_config import db, sess


class announcement(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    author = db.Column(db.String(255), unique=False)
    content = db.Column(db.String(50000), unique=True)
    module = db.Column(db.Integer, unique=False)
    created_at = db.Column(db.Date, unique=False)

    def getAll(self):
        try:
            announcements = sess.query(announcement).all()
            res = []
            for data in announcements:
                temp = {
                    'id': data.id,
                    'title': data.title,
                    'author': data.author,
                    'module': data.module,
                    'content': data.content,
                    'created_at': data.created_at
                }
                res.append(temp)
            ret = {
                'status': 200,
                'message': 'This are the published announcements!',
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
            sess.add(self)
            sess.commit()
            new_announcement = {
                'id': self.id,
                'title': self.title,
                'author': self.author,
                'module': self.module
            }
            ret = {
                'status': 200,
                'message': 'Announcement Published!',
                'new_lecturer': new_announcement
            }
            return ret
        except Exception as e:
            ret = {
                'status': 200,
                'message': e.args,
            }
            return ret

    def edit(self, id, request):
        try:
            selected_announcement = sess.query(announcement).filter(announcement.id == id).first()
            if selected_announcement is not None:
                data = {}
                for k in request.keys():
                    param = k
                    data[k] = request[param]
                check = sess.query(announcement).filter(announcement.id == id).update(data, synchronize_session=False)
                sess.commit()
                if check == 1:
                    ret = {
                        'status': 200,
                        'message': 'Data updated!'
                    }
                else:
                    ret = {
                        'status': 500,
                        'message': "Something's wrong with our server. Please try again later!"
                    }
                return ret
            else:
                ret = {
                    'status': False,
                    'message': "Announcement is not found"
                }
                return ret
        except Exception as e:
            ret = {
                'status': False,
                'message': e.args
            }
            return ret

    def delete(self, id):
        try:
            selected_announcement = sess.query(announcement).filter(announcement.id == id).first()
            if selected_announcement is not None:
                sess.delete(selected_announcement)
                sess.commit()
                ret = {
                    'status': 200,
                    'message': 'Data deleted!'
                }
                return ret
            else:
                ret = {
                    'status': 200,
                    'message': "Announcement is not found"
                }
                return ret
        except Exception as e:
            ret = {
                'status': 200,
                'message': e.args
            }
            return ret
