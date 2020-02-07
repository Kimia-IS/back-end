from flask import request, jsonify, Blueprint, send_file
from academic.models import get_byLecturer
from achievement.models import get_achievement_byID
from auth.models import getByID
from experience.models import get_experience_byID
from finalTask.models import get_finalTask_byID
from publication.models import get_publication_byID
from research.models import get_research_byID
from db_config import sess
import os

general_blueprint = Blueprint('general_blueprint', __name__)


@general_blueprint.route('/profile/<param>', methods=['GET'])
def get_profile(param):
    tables = ['lecture', 'class', '']
    category = param.split(':')[0]
    id = param.split(':')[1]
    res = []
    if "not" not in get_byLecturer(id)['message']:
        res.append(get_byLecturer(id)['results'])
    else:
        res.append(get_byLecturer(id)['message'])
    ret = {
        'status': 200,
        'message': 'Here are the results for id '+id,
        'results': res
    }
    return jsonify(ret)

# @general_blueprint.route('/datas/files', methods=['GET'])
# def show_file():
#     print(masuk)
#     path = request.args.get('path')
#     print(path)
#     if (path):
#         return send_file(path)