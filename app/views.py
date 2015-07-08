from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/<id>')
def post(id):
    return render_template("post.html", id=id)
