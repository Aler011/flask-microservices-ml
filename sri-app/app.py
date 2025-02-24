from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
from sklearn.preprocessing import KBinsDiscretizer

app = Flask(__name__)

# Ruta para manejar las peticiones POST
@app.route('/funcionDiscretizacion', methods=['POST'])
def funcion_discretizacion():
    # Obtener los datos JSON de la petición
    datos = request.get_json()

    # Verificar si los datos están presentes
    if not datos:
        return jsonify({"error": "No se proporcionaron datos"}), 400

    # Extraer el array y el número de intervalos del JSON
    array = datos.get('array')
    bins = datos.get('bins')

    # Verificar si los datos son válidos
    if not array or not bins:
        return jsonify({"error": "Faltan parámetros: 'array' o 'bins'"}), 400

    # Convertir el array a un numpy array
    data = np.array(array).astype(float).reshape(-1, 1)

    # Crear el objeto discretizador con estrategia 'uniform'
    discretizer = KBinsDiscretizer(n_bins=bins, encode='ordinal', strategy='uniform')

    # Aplicar la discretización
    data_disc = discretizer.fit_transform(data)

    # Convertir los datos a DataFrame para una presentación más clara
    df = pd.DataFrame({
        'Valor Original': data.flatten(),
        'Intervalo': data_disc.flatten()
    })

    # Convertir el DataFrame a un diccionario para la respuesta JSON
    resultado = df.to_dict(orient='records')

    # Devolver la respuesta en formato JSON
    return jsonify(resultado)

if __name__ == '__main__':
    # Ejecutar la aplicación en el puerto 5000
    app.run(debug=True)