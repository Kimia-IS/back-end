from flask import request, jsonify, Blueprint
from academic.models import academic
import json

academic_blueprint = Blueprint('academic_blueprint', __name__)


@academic_blueprint.route('/academic', methods=['GET'])
def getCourses():
    courses = academic()
    hasil = courses.get()
    return json.dumps(hasil)