from flask import request, jsonify, Blueprint, send_file
from academic.models import get_academic_byLecturer
from achievement.models import get_achievement_byLecturer
from auth.models import getByID
from experience.models import get_experience_byLecturer
from finalTask.models import get_finalTask_byLecturer
from publication.models import get_publication_byLecturer
from research.models import get_research_byLecturer
from organization.models import get_organization_byLecturer
from db_config import sess
import os

general_blueprint = Blueprint('general_blueprint', __name__)


@general_blueprint.route('/profile/<param>', methods=['GET'])
def get_profile(param):
    tables = ['academic', 'achievement', 'profile', 'experience', 'organization', 'publication', 'research', 'socres']
    category = param.split(':')[0]
    id = param.split(':')[1]
    res = []

    if category == 'lecturer':
        # return get_finalTask_byLecturer(id)
        for data in tables:
            hasil = search_profile(data, id)
            if hasil != "not found":
                res.append(hasil)
    elif category == 'admin':
        hasil = getByID(category, id)
        if "not" not in hasil['message']:
            res.append(hasil['results'])
        else:
            res.append('data not found for given ID')

    ret = {
        'status': 200,
        'message': 'Here are the results for id '+id,
        'results': res
    }
    return jsonify(ret)


def search_profile(cat, id):
    if cat == 'academic':
        res = get_academic_byLecturer(id)
    elif cat == 'achievement':
        res = get_achievement_byLecturer(id)
    elif cat == 'profile':
        res = getByID('lecturer', id)
    elif cat == 'experience':
        res = get_experience_byLecturer(id)
    elif cat == 'finalTask':
        res = get_finalTask_byLecturer(id)
    elif cat == 'journal' or cat == 'patent' or cat == 'otherpub':
        res = get_publication_byLecturer(cat, id)
    elif cat == 'research':
        res = get_research_byLecturer(id)
    elif cat == 'organization':
        res = get_organization_byLecturer(id)
    else:
        res = {
            'message': 'not'
        }
    if "not" not in res['message']:
        print(res)
        return res['results']
    else:
        return "not found"
# @general_blueprint.route('/datas/files', methods=['GET'])
# def show_file():
#     print(masuk)
#     path = request.args.get('path')
#     print(path)
#     if (path):
#         return send_file(path)