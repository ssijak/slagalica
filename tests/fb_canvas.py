import os

from flask import Flask, render_template

try:
    from simplejson import dumps
except:
    from json import dumps

import flask_canvas

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

app = Flask('canvas_example', template_folder=tmpl_dir)
app.config.update({
    'DEBUG': True,
    'CANVAS_CLIENT_ID': '709161332427214',
    'CANVAS_CLIENT_SECRET': '6426c672e75b0c6378421b92ff82ba2c',
    'CANVAS_REDIRECT_URI': 'https://apps.facebook.com/testflaskapp',
    'CANVAS_SCOPE': 'email',
    'CANVAS_ERROR_URI': '/error'
})
flask_canvas.install(app)

@app.route('/', methods=['GET'])
def home():
    return 'hallo'

@app.canvas_route('/canvas/', methods=['POST'])
def canvas(canvas_user):
    user = canvas_user.request('/me')
    return render_template('index.html', user=user)

@app.route('/error', methods=['GET'])
def error():
    return 'why you no accept?'

if __name__ == '__main__':
    app.run()