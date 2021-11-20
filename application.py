from flask import Flask, render_template
application = Flask(__name__)
@application.route('/')

def index():
    return render_template('index.html')

'''
To test locally:
export FLASK_APP="application.py"
flask run
command shift R to reload static files
'''