from flask import request, jsonify, Blueprint
from achivement.models import achievement, get_all_achievements,edit_achievement,delete_achievement
import os

achievement_blueprint = Blueprint('achievement_blueprint', __name__)
# Allowed file extension
ALLOWED_EXTENSIONS = {'docx', 'pdf'}


@achievement_blueprint.route('/achievements', methods=['GET','POST','PUT','DELETE'])
def process_achievements():
    if request.method == 'GET':
        return jsonify(get_all_achievements())
    elif request.method == 'DELETE':

        # get id from the query string
        id = request.args.get('id')
        return jsonify(delete_achievement(id))
    else:
        res = {
            'status': 500,
            'message': 'Sorry, your request method is not recognized!'
        }
        return jsonify(res)