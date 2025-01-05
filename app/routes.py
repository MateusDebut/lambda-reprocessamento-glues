from flask import jsonify

def configure_routes(app):
    @app.route('/clientes', methods=['GET'])
    def clientes():
        return jsonify({"message": "Olá, mundo!"}), 200
