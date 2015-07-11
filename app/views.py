from flask import render_template, redirect, flash, url_for
from app import app
from .forms import SuggestionForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/contact', methods=('GET', 'POST'))
def contact():
    form = SuggestionForm()
    if form.validate_on_submit():
        flash('귀중한 의견 감사합니다!')
        return redirect(url_for('index'))
    return render_template('contact.html', form=form)

@app.route('/<id>')
def post(id):
    return render_template("post.html", id=id)
