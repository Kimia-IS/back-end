from db_config import db, sess
from flask import request, jsonify, Blueprint
from datetime import date

announcement_blueprint = Blueprint('announcement_blueprint', __name__)


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


@announcement_blueprint.route('/announcements/<cat>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def process_announcements(cat):
    try:
        # check request method
        # if request method = POST
        if request.method == 'GET':

            # build new announcement object
            announcement_object = announcement()

            # call the getAll method from announcement object
            ret = announcement_object.getAll()
            return jsonify(ret)

        # if request method = POST
        elif request.method == 'POST':

            # get data from json request
            title = request.json['title']
            content = request.json['content']
            author = request.json['author']
            if cat == 'academic':
                module = 1
            elif cat == 'achievement':
                module = 2
            elif cat == 'experience':
                module = 3
            elif cat == 'finalTask':
                module = 4
            elif cat == 'publication':
                module = 5
            elif cat == 'research':
                module = 6
            elif cat == 'socres':
                module = 7
            else:
                ret = {
                    'status': 200,
                    'message': 'module not found'
                }
                return jsonify(ret)
            created_at = date.today()

            # build new announcement object with initial value
            new_announcement = announcement(title=title, content=content, author=author, module=module,
                                            created_at=created_at)

            # call the save method from announcement object
            ret = new_announcement.save()
            return jsonify(ret)

        # if request method = PUT
        elif request.method == 'PUT':

            # get id from query
            id = request.args.get('id')

            # build new announcement object
            announcement_object = announcement()

            # call the edit method from announcement object
            ret = announcement_object.edit(id, request.form)
            return jsonify(ret)

        # if request method = DELETE
        elif request.method == 'DELETE':
            # get id from query
            id = request.args.get('id')

            # build new announcement object
            announcement_object = announcement()

            # call the delete method from announcement object
            ret = announcement_object.delete(id)
            return jsonify(ret)

        # if request method is unknown
        else:
            return jsonify({'status': 500, 'message': 'Sorry, your request method is not recognized!'})
    except Exception as e:
        res = {
            'message': e.args
        }
        return res