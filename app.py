from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class SquareDB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)
    square = db.Column(db.Integer)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        number = int(request.form['number_input'])
        squaredb = SquareDB.query.filter_by(number=number).first()
        if squaredb:
            square = squaredb.square  
        else:
            square = number * number
            squaredb = SquareDB(number=number, square=square)
            db.session.add(squaredb)
            db.session.commit()
        return redirect(url_for('final', s_id=squaredb.id))
    return render_template('home.html')

@app.route('/final/<int:s_id>')
def final(s_id):
    squaredb = SquareDB.query.get(s_id)
    return render_template('final.html', res=squaredb)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
