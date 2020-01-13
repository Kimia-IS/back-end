from flask import request, jsonify, Blueprint
from finalTask.models import finalTask, finalTask_lecturer, finalTask_file, get_all_final_task
from announcement import announcement
import os

final_task_blueprint = Blueprint('final_task_blueprint', __name__)
# Allowed file extension
ALLOWED_EXTENSIONS = {'docx', 'pdf'}


# function to check the file extension
def allowed_file(filename):
    # Return boolean based on the ALLOWED_EXTENSION list
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@final_task_blueprint.route('/finalTask', methods=['GET', 'POST'])
def process_final_task():
    # Check request method
    # if request method == GET
    if request.method == 'GET':

        # return get_all_final_task method from final task module
        return jsonify(get_all_final_task())

    # if request method == POST
    elif request.method == 'POST':
        try:

            # if request file exist
            if request.files:

                # get file data into a list
                files = request.files.getlist('final_task_file')

                # loop over the file list
                for file in files:

                    # if the extension not allowed
                    if not allowed_file(file.filename):
                        ret = {
                            'status': 200,
                            'message': 'File Extension must be PDF or DOCX!'
                        }
                        return jsonify(ret)

                    # check the directory to save the file
                    if not os.path.exists('datas/files/finalTasks'):

                        # make a directory if it doesn't exist
                        os.makedirs('datas/files/finalTasks')

                    # save file to /datas/files/finalTasks
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
