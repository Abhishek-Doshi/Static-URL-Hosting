from flask import Flask
from config import CONFIG

app = Flask(__name__)

@app.route('/')
def index():
    return "This page is hosted and can be accessed via a static URL."

app.run(debug=True, port=CONFIG["PORT"])