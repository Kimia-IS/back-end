from flask import Flask
from auth.app import auth_blueprint
from academic.app import academic_blueprint
from finalTask.app import final_task_blueprint
from achievement.app import achievement_blueprint
from experience.app import experience_bluprint

app = Flask(__name__)
app.secret_key = "GB981UA7YT91"
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(auth_blueprint)
app.register_blueprint(academic_blueprint)
app.register_blueprint(final_task_blueprint)
app.register_blueprint(achievement_blueprint)
app.register_blueprint(experience_bluprint)
app.run(debug = True, host = '0.0.0.0')
