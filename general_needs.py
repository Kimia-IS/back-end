from flask import request, jsonify, Blueprint, send_file
from academic.models import get_academic_byLecturer, academic, academic_lecturer
from achievement.models import get_achievement_byLecturer, achievement
from auth.models import getByID, admin, lecturer
from experience.models import get_experience_byLecturer, experience
from finalTask.models import get_finalTask_byLecturer, finalTask
from publication.models import get_publication_byLecturer, journal, patent, other_publication
from research.models import get_research_byLecturer, research
from organization.models import get_organization_byLecturer, organization
from socres.models import get_socres_byLecturer, socres
import pandas as pd
import os

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
        elif cat == 'admin':
            admin(name=data[1].split(';')[0], role=data[1].split(';')[1], auth_id=data[1].split(';')[2],
                  password=data[1].split(';')[3], email=data[1].split(';')[4]).save()
        elif cat == 'lecturer':
            lecturer(name=data[1].split(';')[0], role=data[1].split(';')[1], nip=data[1].split(';')[2],
                     password=data[1].split(';')[3], email=data[1].split(';')[4]).save()
        total = total + 1
    ret = {
        'status': 200,
        'message': str(total) + " rows executed",
    }
    return jsonify(ret)


@general_blueprint.route('/download', methods=['POST'])
def download_file():
    try:
        filepath = request.form['filepath']
        return send_file(filepath, as_attachment=True)
    except Exception as e:
        return str(e)


@general_blueprint.route('/profile/<param>', methods=['GET'])
def get_profile(param):
    tables = ['academic', 'achievement', 'profile', 'experience', 'finalTask', 'organization', 'journal', 'patent', 'otherpub', 'research', 'socres']
    category = param.split(':')[0]
    id = param.split(':')[1]
    res = {}
    print('masuk')
    print('param = ', param)
    print('category =', category)
    print('id =', id)

    if category == 'lecturer':
        # return get_finalTask_byLecturer(id)
        for data in tables:
            hasil = search_profile(data, id)
            print('hasil =', hasil)
            if hasil != "not found":
                res[data] = hasil
                #res.append(hasil)
    elif category == 'admin':
        hasil = getByID(category, id)
        if "not" not in hasil['message']:
            res.append(hasil['results'])
        else:
            res.append('data not found for given ID')
    print('res =', res)
    ret = {
        'status': 200,
        'message': 'Here are the results for id '+id,
        'results': res
    }
    return jsonify(ret)


def search_profile(cat, id):
    print('search_profile, cat=', cat, ' id=', id)
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
    print('res search_profile =', res)
    if "not" not in res['message']:
        print(res)
        # content = {
        #     cat: res['results']
        # }
        # return content
        return res
    else:
        return "not found"
# @general_blueprint.route('/datas/files', methods=['GET'])
# def show_file():
#     print(masuk)
#     path = request.args.get('path')
#     print(path)
#     if (path):
#         return send_file(path)