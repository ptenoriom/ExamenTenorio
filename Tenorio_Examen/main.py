from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1')
def ejercicio1():
    return render_template('ejercicio1.html')

@app.route('/procesar_ejercicio1', methods=['POST'])
def procesar_ejercicio1():
    nombre = request.form.get('nombre')
    edad = int(request.form.get('edad'))
    cantidad_tarros = int(request.form.get('cantidad_tarros'))

    precio_tarro = 9000
    total_sin_descuento = cantidad_tarros * precio_tarro

    if 18 <= edad <= 30:
        descuento = 0.15
    elif edad > 30:
        descuento = 0.25
    else:
        descuento = 0

    total_con_descuento = total_sin_descuento * (1 - descuento)

    resultados = {
        'nombre': nombre,
        'total_sin_descuento': total_sin_descuento,
        'total_con_descuento': total_con_descuento
    }

    return render_template('ejercicio1.html', resultados=resultados)

@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')

@app.route('/procesar_ejercicio2', methods=['POST'])
def procesar_ejercicio2():
    nombre = request.form.get('nombre')
    contrasena = request.form.get('contrasena')

    usuarios = {
        'juan': 'admin',
        'pepe': 'user'
    }

    mensaje = ""

    if nombre in usuarios and usuarios[nombre] == contrasena:
        if nombre == 'juan':
            mensaje = "Bienvenido administrador juan"
        elif nombre == 'pepe':
            mensaje = "Bienvenido usuario pepe"
    else:
        mensaje = "Usuario o contraseña incorrectos"

    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
