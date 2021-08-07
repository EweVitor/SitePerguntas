from flask import Flask, render_template, request
from flask.wrappers import Request
from config import db
from model.usuario import Usuario
from controlador.usuario import usuario_blueprint

TEMPLATE = './view'
STATIC = './static'


app = Flask(__name__, static_url_path='', template_folder=TEMPLATE, static_folder=STATIC)
app.register_blueprint(usuario_blueprint)
#configurações de db

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./dados.db'

db.init_app(app)

with app.app_context():
   db.create_all()

#configurações de rotas
@app.route('/')
def olaMundo():
    return render_template('login.html') 

@app.route('/index')
def index():
    return render_template('index.html')

#app.run(host='0.0.0.0' ,port=5000)


