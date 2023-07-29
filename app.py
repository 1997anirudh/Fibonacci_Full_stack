from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class FibDB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer,unique=True)
    fibonacci = db.Column(db.String)

# def calculate_fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)

def calculate_fibonacci_series(n):
    fibonacci_series = [0, 1]
    while len(fibonacci_series) < n:
        next_fibonacci = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_fibonacci)
    return ", ".join(str(num) for num in fibonacci_series)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        number = int(request.form['number_input'])
        fibdb = FibDB.query.filter_by(number=number).first()
        if fibdb:
            fibonacci = fibdb.fibonacci
        else:
            fibonacci = calculate_fibonacci_series(number)
            fibdb = FibDB(number=number, fibonacci=fibonacci)
            db.session.add(fibdb)
            db.session.commit()
        return redirect(url_for('final', f_id=fibdb.id))
    return render_template('home.html')

@app.route('/final/<int:f_id>')
def final(f_id):
    fibdb = FibDB.query.get(f_id)
    return render_template('final.html', res=fibdb)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
