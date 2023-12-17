from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

# Ruta para mostrar los datos de la base de datos
@app.route('/')
def show_data():
    return render_template('fibramovil.html')

@app.route('/indice')
def show():
    return render_template('index.html')


if __name__ == '__main__':
    # Crea las tablas en la base de datos antes de ejecutar la aplicación
    app.run(debug=True)
    