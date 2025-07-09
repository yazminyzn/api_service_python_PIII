'''
Flask [Python]
Ejercicios de práctica

Autor: Ing.Jesús Matías González
Version: 2.0

Descripcion:
Se utiliza Flask para crear un WebServer que levanta los datos de
las personas registradas.

Ingresar a la siguiente URL para ver los endpoints disponibles
http://127.0.0.1:5000/
'''

import traceback
from flask import Flask, request, jsonify, Response

import utils
import persona

app = Flask(__name__)

# Configuración de la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///personas.db"
persona.db.init_app(app)


@app.route("/")
def index():
    try:
        result = "<h1>Bienvenido!! Jesús González</h1>"
        result += "<h2>Endpoints disponibles:</h2>"
        result += "<h2>Ejercicio Nº1:</h2>"
        result += "<h3>[GET] /personas?limit=[]&offset=[] --> Mostrar el listado de personas (limit y offset son opcionales)</h3>"
        result += "<h2>Ejercicio Nº2:</h2>"
        result += "<h3>[POST] /registro --> Ingresar una nueva persona por JSON</h3>"
        result += "<h2>Ejercicio Nº3:</h2>"
        result += "<h3>[GET] /comparativa --> Mostrar un gráfico con las edades de todas las personas</h3>"
        return result
    except:
        return jsonify({'trace': traceback.format_exc()})


@app.route("/personas")
def personas():
    try:
        limit_str = request.args.get('limit')
        offset_str = request.args.get('offset')

        limit = int(limit_str) if limit_str and limit_str.isdigit() else 0
        offset = int(offset_str) if offset_str and offset_str.isdigit() else 0

        result = persona.report(limit=limit, offset=offset)
        return jsonify(result)
    except:
        return jsonify({'trace': traceback.format_exc()})


@app.route("/registro", methods=['POST'])
def registro():
    try:
        data = request.get_json()
        name = data.get('name')
        age = data.get('age')

        if not name or not isinstance(age, int):
            return jsonify({'error': 'Nombre o edad inválidos'}), 400

        persona.insert(name, age)
        return Response(status=200)
    except:
        return jsonify({'trace': traceback.format_exc()})


@app.route("/comparativa")
def comparativa():
    try:
        x, y = persona.dashboard()
        image_html = utils.graficar(x, y)
        return Response(image_html.getvalue(), mimetype='image/png')
    except:
        return jsonify({'trace': traceback.format_exc()})


@app.before_first_request
def before_first_request_func():
    persona.db.create_all()
    print("Base de datos generada")


if __name__ == '__main__':
    print('JMRG@Server start!')
    app.run(host="127.0.0.1", port=5000)
