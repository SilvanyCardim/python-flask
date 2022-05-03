from app import db

class Pessoa(db.Model): # será convertida em tabel
	__tablename__ = 'pessoas'

	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String(50), nullable=False) # p que seja item obrigatorio
	idade = db.Column(db.Integer)
	sexo = db.Column(db.String(1)) # p M ou F
	salario = db.Column(db.Float)  # p receber centavos

	def __init__(self, nome='Anônimo', idade=18, sexo='M', salario=1039):  #p diminuir possibilidades de erro,
		# foi definido um valor default, caso nao seja passado um valor durante a construção
		self.nome = nome
		self.idade = idade
		self.sexo = sexo
		self.salario = salario

	def __repr__(self):  #self é parametro obrigatorio
		return '<Pessoa %r>' % self.nome   # nome substitui o %r ao ser exibido
