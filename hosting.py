from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/testing')
def notroot():
    return render_template('testing.html')

@app.route('/data')
def data():
    num = random.randrange(10000000)
    return render_template('data.html', sendesInn = num)

if __name__ == '__main__':
    app.run(debug=True)