from tokenize import Name
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,SubmitField
from wtforms.validators import InputRequired, Email, Regexp

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'verydifficultsecretkey'

# activity 4
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[InputRequired()])
    uoft_email = EmailField('What is your UofT Email address?',validators=[Email()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        old_email = session.get('email')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        if old_email is not None and old_email != form.name.data:
            flash('Looks like you have changed your email!')
        session['name'] = form.name.data
        session['email'] = form.uoft_email.data
        form.name.data = ''
        form.uoft_email.data = ''
        return redirect(url_for('index'))
    return render_template('index.html',form=form,name=session.get('name'), email=session.get('email'))

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
