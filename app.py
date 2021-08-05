from flask import Flask 

TEMPLATE = './template'
STATIC = './static'

app = Flask(__name__, template_folder=TEMPLATE, static_folder=STATIC)
@app.route('/')
def olaMundo():
    return 'ola mundo'


#app.run(host='0.0.0.0' ,port=5000)


