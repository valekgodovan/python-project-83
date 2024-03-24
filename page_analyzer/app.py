from flask import Flask
from dotenv import load_dotenv
from flask import render_template
import os
import psycopg2

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')
conn = psycopg2.connect(DATABASE_URL)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route('/')
def index():
    return render_template(
        'index.html',
    )

@app.route('/urls')
def urls():
    return render_template(
        'urls.html',
    )