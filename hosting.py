from flask import Flask, render_template
import random

# Create the Flask app
app = Flask(__name__)

# Route for the homepage
@app.route('/')
def root():
    return render_template('index.html')  # Renders the 'index.html' template

# Route for the testing page
@app.route('/testing')
def notroot():
    return render_template('testing.html')  # Renders the 'testing.html' template

# Route for generating random data
@app.route('/data')
def data():
    num = random.randrange(10000000)  # Generate a random number
    return render_template('data.html', sendesInn=num)  # Pass the number to the template

# Run the Flask app
if __name__ == '__main__':
    # Set the app to be accessible on the network
    app.run(host='0.0.0.0', port=8000, debug=True)
