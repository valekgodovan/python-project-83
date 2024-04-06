from flask import Flask, url_for
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


@app.route('/urls/<int:id>')
def urls_id(id):
    return render_template(
        'urls_id.html',
        id=id,
    )


@app.post('/urls')
def urls_post():
    url = request.form.get('url')
    print(db.is_url_in_db(url, conn))
    if validators.url(url) and not db.is_url_in_db(url, conn):
        db.insert_url(url, conn)
    id = 2

    return redirect(url_for('urls_id', id=id), code=302)


if __name__ == '__main__':
    app.run()
