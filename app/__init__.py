from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # recebe a inicialização da class flask
app.config.from_object('config')  # p carregar o arquivo de configuração

db = SQLAlchemy(app)  # instancia a classe do sql, passando p construtor o flask

migrate = Migrate(app, db)

manager = Manager(app)  # gerencia comandos do bd
manager.add_command('db', MigrateCommand)  # p poder usar o bd
from app.controllers import default  # vem no final pq é necessario carregar as configurações acima
