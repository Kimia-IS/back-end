from flask import request, jsonify, Blueprint
from finalTask.models import finalTask, finalTask_lecturer, finalTask_file, get_all_final_task, count_final_task
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

                # get expected id from existing data to store it into task lecturer & file
                temp_id = count_final_task()+1

                # get data from json request
                student_name = request.form['student_name']
                student_nim = request.form['student_nim']
                student_type = request.form['student_type']
                title = request.form['title']
                starting_date = request.form['starting_date']
                graduation_date = request.form['graduation_date']
                lecturer_nip = request.form['lecturer_nip']
                lecturer_position = request.form['lecturer_position']

                # get file data into a list
                files = request.files.getlist('final_task_file')

                # build new final task object
                new_final_task = finalTask(student_name=student_name, student_nim=student_nim, student_type=student_type,
                                           title=title, starting_date=starting_date, graduation_date=graduation_date)
                # call save method from final task object
                res = [new_final_task.save()]

                # build new final task lecturer object
                new_final_task_lecturer = finalTask_lecturer(final_task_id=temp_id, lecturer_nip=lecturer_nip,
                                                             lecturer_position=lecturer_position)
                # call save method from final task lecturer object
                res.append(new_final_task_lecturer.save())

                # loop over the file list
                filepath = []
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

                    # append the path to filepath list
                    filepath.append('datas/files/finalTasks/'+file.filename)

                # build new final task file object
                new_final_task_file = finalTask_file(final_task_id=temp_id, file_path=str(filepath))
                # call save method from final task file object
                res.append(new_final_task_file.save())

                return jsonify(res)
            else:
                return "KOSONG"
        except Exception as e:
            ret = {
                'status': 200,
                'message': e.args,
            }
            return ret