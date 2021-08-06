from flask import Flask, render_template, request
from flask.wrappers import Request
from config import db
from usuario import Usuario


TEMPLATE = './template'
STATIC = './static'


app = Flask(__name__, template_folder=TEMPLATE, static_folder=STATIC)

#configurações de db

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./dados.db'

db.init_app(app)

with app.app_context():
   db.create_all()

#configurações de rotas
@app.route('/')
def olaMundo():
    return render_template('cadastro.html') 

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/cadastro', methods=["POST"]) 
def cadastro():

    nome = request.form.get('nome')
    email = request.form.get('email')

    usuarios = Usuario.query.all()
    for u in usuarios:
        if u.email == email:
            return 'usuario ja existe'

    usuario = Usuario(nome, email) 
    db.session.add(usuario)
    db.session.commit()
        
    return 'ususario cadastrado'

@app.route('/listaUsuario')    
def listaUsuario():
    usuarios = Usuario.query.all()
    return render_template('listaUsu.html', usuarios = usuarios)

#app.run(host='0.0.0.0' ,port=5000)


