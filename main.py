from flask import Flask
from auth.app import auth_blueprint
from academic.app import academic_blueprint
from finalTask.app import final_task_blueprint

app = Flask(__name__)
app.secret_key = "GB981UA7YT91"
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['FILE_UPLOAD'] = '/datas/files/finalTasks'
app.register_blueprint(auth_blueprint)
app.register_blueprint(academic_blueprint)
app.register_blueprint(final_task_blueprint)
app.run(debug=True)
