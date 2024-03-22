from flask import Flask
from dotenv import load_dotenv
from flask import render_template
import os

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route('/')
def index():
    name = "Vasya"
    return render_template(
        'index.html',
        name=name,
    )
