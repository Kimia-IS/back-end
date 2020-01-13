from flask import request, jsonify, Blueprint
from finalTask.models import finalTask, finalTask_lecturer, finalTask_file, get_all_final_task
from announcement import announcement
import os

final_task_blueprint = Blueprint('final_task_blueprint', __name__)


@final_task_blueprint.route('/finalTask', methods=['GET', 'POST'])
def process_final_task():
    if request.method == 'GET':
        return jsonify(get_all_final_task())
    elif request.method == 'POST':
        try:
            if request.files:
                file = request.files['final_task_file']
                if not os.path.exists('datas/files/finalTasks'):
                    os.makedirs('datas/files/finalTasks')
                file.save(os.path.join('datas/files/finalTasks', file.filename))
                return "SAVED"
            else:
                return "KOSONG"
        except Exception as e:
            ret = {
                'status': 200,
                'message': e.args,
            }
            return ret