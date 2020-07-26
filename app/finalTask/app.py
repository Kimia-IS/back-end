from flask import request, jsonify, Blueprint
from finalTask.models import finalTask, finalTask_lecturer, finalTask_file, get_all_final_task, edit_final_task, edit_final_task_file, edit_final_task_lecturer, deleteTask, deleteTask_file, deleteTask_lecturer, \
    get_finalTask_byID
import os

final_task_blueprint = Blueprint('final_task_blueprint', __name__)
# Allowed file extension
ALLOWED_EXTENSIONS = {'docx', 'pdf', 'jpg', 'jpeg'}

global saved_id
# function to check the file extension
def allowed_file(filename):
    # Return boolean based on the ALLOWED_EXTENSION list
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@final_task_blueprint.route('/finalTask', methods=['GET', 'POST', 'PUT', 'DELETE'])
def process_final_task():
    # Check request method
    # if request method == GET
    if request.method == 'GET':
        if request.args.get('id'):
            return jsonify(get_finalTask_byID(request.args.get('id')))
        # return get_all_final_task method from final task module
        return jsonify(get_all_final_task())

    # if request method == POST
    elif request.method == 'POST':
        try:
            # get data from json request
            student_name = request.form['student_name']
            student_nim = request.form['student_nim']
            student_type = request.form['student_type']
            title = request.form['title']
            starting_date = request.form['starting_date']
            graduation_date = request.form['graduation_date']
            lecturer_nip = request.form['lecturer_nip']
            lecturer_position = request.form['lecturer_position']

            # build new final task object
            new_final_task = finalTask(student_name=student_name, student_nim=student_nim, student_type=student_type,
                                       title=title, starting_date=starting_date, graduation_date=graduation_date)
            # call save method from final task object
            res = new_final_task.save()
            saved_id = res['results']['id']
            new_final_task_lecturer = finalTask_lecturer(final_task_id=saved_id, lecturer_nip=lecturer_nip,
                                                         lecturer_position=lecturer_position)
            new_final_task_lecturer.save()

            files = request.files.getlist('final_task_file')
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

                filename = lecturer_nip + '_' + file.filename.replace(' ', '_')

                # save file to /datas/files/finalTasks
                file.save(os.path.join('datas/files/finalTasks', filename))

                # append the path to filepath list
                filepath.append('datas/files/finalTasks/' + filename)

            # build new final task file object
            new_final_task_file = finalTask_file(final_task_id=saved_id, file_path=str(filepath))
            new_final_task_file.save()

            return jsonify(res)
        except Exception as e:
            ret = {
                'status': 500,
                'message': e.args,
            }
            return ret

    # if method == PUT
    elif request.method == 'PUT':

        # get id from query string
        id = request.args.get('id')

        # get result from edit_final_task method
        res = edit_final_task(id, request.form)
        return jsonify(res)

    # if method == DELETE
    elif request.method == 'DELETE':
        # get id from query string
        id = request.args.get('id')

        # get result from deleteTask method
        res = deleteTask(id)
        return jsonify(res)


@final_task_blueprint.route('/finalTask/<category>', methods=['PUT', 'DELETE'])
def edit_final_task_additional(category):

    # get id and category from query string
    id = request.args.get('id')

    if request.method == 'PUT':
        # check the category from path
        # if category == lecturer
        if category == 'lecturer':
            # get result from edit
            res = edit_final_task_lecturer(id, request.form)

        # if category == file
        elif category == 'file':
            # get result from edit
            res = edit_final_task_file(id, request.form)
        else:
            res = {
                'status': 200,
                'message': 'Wrong path!'
            }
    elif request.method == 'DELETE':
        # check the category from path
        # if category == lecturer
        if category == 'lecturer':
            # get result from delete
            res = deleteTask_lecturer(id)

        # if category == file
        elif category == 'file':
            # get result from delete
            res = deleteTask_file(id)

        else:
            res = {
                'status': 200,
                'message': 'Wrong path!'
            }
    else:
        res = {
            'status': 500,
            'message': 'Sorry, your request method is not recognized!'
        }
    return jsonify(res)
