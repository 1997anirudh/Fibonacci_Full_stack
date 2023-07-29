from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    square = None
    if request.method == 'POST':
        number = int(request.form['number_input'])
        square = number * number
    return render_template('home.html', square=square)

if __name__ == '__main__':
    app.run()
