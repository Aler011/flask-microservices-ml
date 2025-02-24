*Pasos para ejecutar e instalar:*

pip install Flask

pip install numpy

pip install pandas

python app.py

Configurar metodo POST con postman por ejemplo en http://127.0.0.1:5000/funcionDiscretizacion

En la pestaña de "Body" seleccionar "raw" y poner JSON y en el cuerpo pegar:

{
    "array": [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],
    "bins": 3  
}


Probar con "send" para enviar la peticion.
