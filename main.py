from flask import Flask
from flask_cors import CORS
from auth.app import auth_blueprint
from academic.app import academic_blueprint
from finalTask.app import final_task_blueprint
from achievement.app import achievement_blueprint
from experience.app import experience_blueprint
from publication.app import publication_blueprint
from research.app import research_blueprint
from socres.app import socres_blueprint
from organization.app import organization_blueprint
from announcement import announcement_blueprint
from general_needs import general_blueprint
import datetime
from db_config import db
# from flask_jwt_extended import JWTManager				# 1

app = Flask(__name__)
app.secret_key = "GB981UA7YT91"
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'	# 2
# jwt = JWTManager(app)									# 3
app.register_blueprint(auth_blueprint)
app.register_blueprint(academic_blueprint)
app.register_blueprint(final_task_blueprint)
app.register_blueprint(achievement_blueprint)
app.register_blueprint(experience_blueprint)
app.register_blueprint(publication_blueprint)
app.register_blueprint(research_blueprint)
app.register_blueprint(socres_blueprint)
app.register_blueprint(organization_blueprint)
app.register_blueprint(announcement_blueprint)
app.register_blueprint(general_blueprint)
app.permanent_session_lifetime = datetime.timedelta(minutes=60)
CORS(app)

app.run(debug = True) # host = '0.0.0.0' for local Docker running