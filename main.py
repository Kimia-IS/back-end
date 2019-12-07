from flask import Flask
from auth.app import auth_blueprint

app = Flask(__name__)
app.register_blueprint(auth_blueprint)
app.run(debug=True)