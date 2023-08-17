# Fazendo importações

from flask import Flask
from flask_restful import Resource, Api

# Instanciando o Flask

app = Flask(__name__)
api = Api(app)


# Criando a classe Hoteis
class Hoteis(Resource):
    def get(self):
        return {'hoteis': 'Meus Hoteis'}


# Adicionando a rota
api.add_resource(Hoteis, "/hoteis")
if __name__ == "__main__":
    app.run(debug=True)