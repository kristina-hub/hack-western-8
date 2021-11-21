from flask import Flask, render_template, request, url_for, redirect
application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/query', methods=['GET', 'POST'])
def query():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('query.html')

@application.route('/stocks', methods=['GET', 'POST'])
def stocks():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('stocks.html')


if __name__ == '__main__':
    application.run(debug=True)
'''
To test locally:
export FLASK_APP="application.py"
flask run
command shift R to reload static files
'''