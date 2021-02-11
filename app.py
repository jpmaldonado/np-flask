from flask import Flask
from config import Config
from main import main

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(main)

app.run(debug=True)    