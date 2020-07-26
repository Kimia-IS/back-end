from flask import request, jsonify, Blueprint, send_file
from academic.models import get_academic_byLecturer, academic, academic_lecturer
from achievement.models import get_achievement_byLecturer, achievement
from auth.models import getByID, admin, lecturer, do_export
from experience.models import get_experience_byLecturer, experience
from finalTask.models import get_finalTask_byLecturer, finalTask, finalTask_lecturer, finalTask_file
from publication.models import get_publication_byLecturer, journal, journalCorrespondingAuthor, patent, other_publication
from research.models import get_research_byLecturer, research, research_file
from organization.models import get_organization_byLecturer, organization
from socres.models import get_socres_byLecturer, socres
import pandas as pd
import bcrypt
from flask_excel import make_response_from_tables
import pyexcel.ext.xls

general_blueprint = Blueprint('general_blueprint', __name__)


@general_blueprint.route('/upload/<cat>', methods=['POST'])
def upload_bulk(cat):
    file = request.files.get('bulk_file')
    # if file is not None:
    #     print(file)
    #     return "ADA FILE"
    bulk = pd.read_csv(file)
    success = 0
    total = 0
    res = []
    for data in bulk.itertuples():
        res.append(data[1].split(';')[0])
        if cat == 'courses':
            academic(course_id=data[1].split(';')[0], course_name=data[1].split(';')[1],
                     total_classes=data[1].split(';')[2]).save()
        elif cat == 'academicLecturer':
            academic_lecturer(course_id=data[1].split(';')[0], course_class=data[1].split(';')[1], lecturer_nip=data[1].split(';')[2],
                              lecturer_credit=data[1].split(';')[3], total_credit=data[1].split(';')[4]).save()
        elif cat == 'account':
            temp_role = int(data[1].split(';')[1])
            if (temp_role == 4) or (temp_role == 5) or (temp_role == 6):
                cat_role = 'lecturer'
            elif (temp_role == 1) or (temp_role == 2) or (temp_role == 3):
                cat_role = 'admin'
            if cat_role == 'admin':
                admin(name=data[1].split(';')[0], role=data[1].split(';')[1], auth_id=data[1].split(';')[2],
                      password=bcrypt.hashpw(data[1].split(';')[3].encode('utf-8'), bcrypt.gensalt()), email=data[1].split(';')[4]).save()
            elif cat_role == 'lecturer':
                lecturer(name=data[1].split(';')[0], role=data[1].split(';')[1], nip=data[1].split(';')[2],
                         password=bcrypt.hashpw(data[1].split(';')[3].encode('utf-8'), bcrypt.gensalt()), email=data[1].split(';')[4]).save()
            # else:
            #     return jsonify({'status': 400, 'message': 'No role'})
        total = total + 1
    ret = {
        'status': 200,
        'message': str(total) + " rows executed",
    }
    return jsonify(ret)


@general_blueprint.route('/download', methods=['GET'])
def download_file():
    try:
        filepath = request.args.get('filepath')
        return send_file(filepath, as_attachment=True)
    except Exception as e:
        return str(e)


@general_blueprint.route('/profile/<param>', methods=['GET'])
def get_profile(param):
    tables = ['academic', 'achievement', 'profile', 'experience', 'finalTask', 'organization', 'journal', 'patent', 'otherpub', 'research', 'socres']
    category = param.split(':')[0]
    id = param.split(':')[1]
    res = []

    if category == 'lecturer':
        # return get_finalTask_byLecturer(id)
        for data in tables:
            hasil = search_profile(data, id)
            if hasil != "not found":
                res[data] = hasil
                #res.append(hasil)
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
    # elif cat == 'journal' or cat == 'patent' or cat == 'otherpub':
    elif cat == 'journal':
        res = get_publication_byLecturer('journal', id)
    elif cat == 'patent':
        res = get_publication_byLecturer('patent', id)
    elif cat == 'otherpub':
        res = get_publication_byLecturer('other', id)
    elif cat == 'research':
        res = get_research_byLecturer(id)
    elif cat == 'organization':
        res = get_organization_byLecturer(id)
    elif cat == 'socres':
        res = get_socres_byLecturer(id)
    else:
        res = {
            'message': 'not'
        }
    if "not" not in res['message']:
        # content = {
        #     cat: res['results']
        # }
        # return content
        return res
    else:
        return "not found"


@general_blueprint.route('/export', methods=['GET'])
def export_db():
    if request.args.get('model') is None:
        res = {
            'status': 400,
            'message': 'You have to specify model name'
        }
        return jsonify(res)
    sess = do_export()
    model = request.args.get('model')
    if model == 'admin':
        return make_response_from_tables(sess, [admin], 'xlsx', file_name='data')
    elif model == 'lecturer':
        return make_response_from_tables(sess, [lecturer], 'xlsx', file_name='data')
    elif model == 'academic_lecturer':
        return make_response_from_tables(sess, [academic_lecturer], 'xlsx', file_name='data')
    elif model == 'achievement':
        return make_response_from_tables(sess, [achievement], 'xlsx', file_name='data')
    elif model == 'academic':
        return make_response_from_tables(sess, [academic], 'xlsx', file_name='data')
    elif model == 'experience':
        return make_response_from_tables(sess, [experience], 'xlsx', file_name='data')
    elif model == 'finalTask':
        return make_response_from_tables(sess, [finalTask, finalTask_lecturer, finalTask_file], 'xlsx', file_name='data')
    elif model == 'organization':
        return make_response_from_tables(sess, [organization], 'xlsx', file_name='data')
    elif model == 'publication':
        return make_response_from_tables(sess, [journal, journalCorrespondingAuthor, patent, other_publication], 'xlsx', file_name='data')
    elif model == 'research':
        return make_response_from_tables(sess, [research, research_file], 'xlsx', file_name='data')
    elif model == 'socres':
        return make_response_from_tables(sess, [socres], 'xlsx', file_name='data')
