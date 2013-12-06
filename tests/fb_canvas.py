from os.path import abspath

from sys import path
path.append(abspath('.'))

from flask import Flask
try:
    from simplejson import dumps
except:
    from json import dumps

import flask_canvas

app = Flask('canvas_example')
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
    return '<p>%s</p><p>%s</p>' % (
        dumps(canvas_user),
        dumps(canvas_user.request('/me')))

@app.route('/error', methods=['GET'])
def error():
    return 'why you no accept?'

if __name__ == '__main__':
    app.run()