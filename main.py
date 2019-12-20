from flask import Flask
from auth.app import auth_blueprint
from academic.app import academic_blueprint

app = Flask(__name__)
app.secret_key = "GB981UA7YT91"
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(auth_blueprint)
app.register_blueprint(academic_blueprint)
app.run(debug=True)
