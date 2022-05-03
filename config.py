import os.path  # para controle de variáveis
basedir = os.path.abspath(os.path.dirname(__file__))  # para capturar o diretorio absoluto

DEBUG = True # p acompanhar os erros que possam acontecer

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'banco.db') # diretorio fisico no formato sqlite
SQLALCHEMY_TRACK_MODIFICATIONS = True # p poder fazer modificações no bd
