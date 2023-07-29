from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        number = int(request.form['number_input'])
        square = number * number
        return redirect(url_for('final', square=square))
    return render_template('home.html')

@app.route('/final/<int:square>')
def final(square):
    return render_template('final.html', square=square)

if __name__ == '__main__':
    app.run()
