from flask import Flask
from dotenv import load_dotenv
from flask import render_template, request, redirect
from . import db
import os
import validators

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')
conn = db.get_db_connection(DATABASE_URL)

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


@app.post('/urls')
def urls_post():
    url = request.form.get('url')
    if validators.url(url):
        db.insert_url(url, conn)

    return redirect('/urls', code=302)


if __name__ == '__main__':
    app.run()
