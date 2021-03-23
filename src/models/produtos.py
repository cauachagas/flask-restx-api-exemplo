from flask_restx import fields

from src.server.instancia import servidor

produto = servidor.api.model('Produto', {
    'id': fields.Integer(readonly=True, description='O ID do registro'),
    'nome': fields.String(required=True, min_length=3, max_legth=100, description='O nome do produto'),
    'preco': fields.Float(required=True, description='O preço do produto')
})