from sqlalchemy import ForeignKey
from db_config import db, sess


class organization(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    lecturer_nip = db.Column(db.String(255), ForeignKey("lecturer.nip"), unique=False)
    organization_name = db.Column(db.String(255), unique=False)
    position = db.Column(db.String(255), unique=False)
    year = db.Column(db.String(5), unique=False)
    filepath = db.Column(db.String(255), unique=True)

    def save(self):
        try:
            check_organization = sess.query(organization).filter(organization.lecturer_nip == self.lecturer_nip).filter(organization.organization_name==self.organization_name).\
                filter(organization.year == self.year).first()
            if check_organization is None:
                sess.add(self)
                sess.commit()
                new_organization = {
                    'id': self.id,
                    'lecturer_nip': self.lecturer_nip,
                    'organization_name': self.organization_name,
                    'position': self.position,
                    'year': self.year,
                    'filepath': self.filepath
                }
                ret = {
                    'status': 200,
                    'message': 'New organization Registered',
                    'results': new_organization
                }
            else:
                ret = {
                    'status': 200,
                    'message': 'Your organization already registered before, please try again another organization!'
                }
            return ret
        except Exception as e:
            ret ={
                'status': 200,
                'message': e.args
            }
            return ret


def get_all_organizations():
    try:
        organizations = sess.query(organization).all()
        res = []
        for data in organizations:
            temp = {
                'id': data.id,
                'lecturer_nip': data.lecturer_nip,
                'organization_name': data.organization_name,
                'position': data.position,
                'year': data.year,
                'filepath': data.filepath
            }
            res.append(temp)
        ret = {
            'status': 200,
            'message': 'These are the registered organizations',
            'results': res
        }
        return ret
    except Exception as e:
        ret = {
            'status': 200,
            'message': e.args,
        }
        return ret


def get_organization_byID(id):
    try:
        data = sess.query(organization).filter(organization.id == id).first()
        selected_organization = {
            'id': data.id,
            'lecturer_nip': data.lecturer_nip,
            'organization_name': data.organization_name,
            'position': data.position,
            'year': data.year,
            'filepath': data.filepath
        }
        ret = {
            'status': 200,
            'message': 'This is the '+data.lecturer_nip+' organization',
            'results': selected_organization
        }
        return ret
    except Exception as e:
        ret = {
            'status': 200,
            'message': e.args,
        }
        return ret


def edit_organization(id, request):
    try:
        selected_organization = sess.query(organization).filter(organization.id == id).first()
        if selected_organization is not None:
            data = {}
            for k in request.keys():
                param = k
                data[k] = request[param]
            edit = sess.query(organization).filter(organization.id == id).update(data, synchronize_session=False)
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
                'message': "organization is not registered"
            }
            return ret
    except Exception as e:
        ret = {
            'status': 200,
            'message': e.args,
        }
        return ret


def delete_organization(id):
    try:
        selected_organization = sess.query(organization).filter(organization.id == id).first()
        if selected_organization is not None:
            sess.delete(selected_organization)
            sess.commit()
            ret = {
                'status': 200,
                'message': 'Data deleted!'
            }
            return ret
        else:
            ret = {
                'status': 200,
                'message': "organization is not registered"
            }
            return ret
    except Exception as e:
        ret = {
            'status': 200,
            'message': e.args
        }
        return ret


def get_organization_byLecturer(nip):
    try:
        data = sess.query(organization).filter(organization.lecturer_nip == nip).first()
        if data is not None:
            res = {
                'id': data.id,
                'lecturer_nip': data.lecturer_nip,
                'organization_name': data.organization_name,
                'position': data.position,
                'year': data.year,
                'filepath': data.filepath
            }
            ret = {
                'status': 200,
                'message': "This is the registered Lecturer's Organization",
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