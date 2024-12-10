from flask import Flask, render_template
import random

# Create the Flask app
app = Flask(__name__)

# Route for the homepage
@app.route('/')
def root():
    return render_template('index.html')  # Renders the 'index.html' template

# Route for the testing page
@app.route('/download')
def notroot():
    return render_template('download.html')  # Renders the 'testing.html' template


# Run the Flask app
if __name__ == '__main__':
    # Set the app to be accessible on the network
    app.run(host='0.0.0.0', port=8000, debug=True)
