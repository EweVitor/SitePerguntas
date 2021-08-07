from flask import Flask, render_template, request,  Blueprint
from flask.wrappers import Request
from sqlalchemy.sql.schema import Table
from config import db
from model.usuario import Usuario   
TEMPLATE = './view'
STATIC = './static'

usuario_blueprint = Blueprint('usuario',__name__, template_folder=TEMPLATE, static_folder=STATIC)


@usuario_blueprint.route('/cadastro', methods=["POST"]) 
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
    
    
    login = usuario
    return render_template('index.html', login = login)

@usuario_blueprint.route('/listaUsuario')    
def listaUsuario():
    usuarios = Usuario.query.all()
    return render_template('listaUsu.html', usuarios = usuarios)