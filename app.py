from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100))
    date = db.Column(db.String(10))
    time = db.Column(db.String(5))

class ReservationForm(FlaskForm):
    name = StringField('名前', validators=[DataRequired()])
    email = StringField('メールアドレス', validators=[DataRequired()])
    date = StringField('予約日', validators=[DataRequired()])
    time = StringField('予約時間', validators=[DataRequired()])
    submit = SubmitField('予約する')

@app.route('/', methods=['GET', 'POST'])
def form():
    form = ReservationForm()
    if form.validate_on_submit():
        new_reservation = Reservation(
            name=form.name.data,
            email=form.email.data,
            date=form.date.data,
            time=form.time.data
        )
        db.session.add(new_reservation)
        db.session.commit()
        return redirect(url_for('confirm', id=new_reservation.id))
    return render_template('form.html', form=form)

@app.route('/submit', methods=['POST'])
def submit():
    form = ReservationForm()
    if form.validate_on_submit():
        new_reservation = Reservation(
            name=form.name.data,
            email=form.email.data,
            date=form.date.data,
            time=form.time.data
        )
        db.session.add(new_reservation)
        db.session.commit()
        return redirect(url_for('confirm', id=new_reservation.id))
    return redirect(url_for('form'))

@app.route('/confirm/<int:id>')
def confirm(id):
    reservation = Reservation.query.get_or_404(id)
    return render_template('confirm.html', reservation=reservation)

@app.route('/reservations/<int:page>', methods=['GET'])
def reservations(page=1):
    per_page = 10  # 1ページあたりの項目数
    pagination = Reservation.query.paginate(page=page, per_page=per_page, error_out=False)
    reservations = pagination.items
    return render_template('reservations.html', reservations=reservations, pagination=pagination)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
