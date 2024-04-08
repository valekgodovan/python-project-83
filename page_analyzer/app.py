from flask import Flask, url_for
from dotenv import load_dotenv
from flask import render_template, request, redirect, flash, url_for, get_flashed_messages
from . import db
import os
import validators
import datetime

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
    messages = get_flashed_messages(with_categories=True)
    return render_template(
        'urls.html',
        messages=messages,
    )


@app.route('/urls/<int:id>')
def urls_id(id):
    id, name, date = db.get_row_from_id_db(id, conn)
    messages = get_flashed_messages(with_categories=True)
    return render_template(
        'urls_id.html',
        id=id,
        name=name,
        date=date.date(),
        messages=messages,
    )


@app.post('/urls')
def urls_post():
    url = request.form.get('url')
    if not validators.url(url):
        flash('Некорректный URL', 'danger')
        return redirect(url_for('urls'), code=302)
    if validators.url(url) and not db.is_url_in_db(url, conn):
        db.insert_url(url, conn)
        flash('Страница успешно добавлена', 'success')
        id, name, date = db.get_row_from_name_db(url, conn)
        return redirect(url_for('urls_id', id=id), code=302)
    return redirect('/urls', code=302)

if __name__ == '__main__':
    app.run()
