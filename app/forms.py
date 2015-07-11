from flask_wtf import Form
from flask_wtf.html5 import EmailField
from wtforms import TextAreaField
from wtforms.validators import InputRequired

class SuggestionForm(Form):
    email = EmailField("이메일 주소", validators=[InputRequired()])
    body = TextAreaField("건의 내용", validators=[InputRequired()])
