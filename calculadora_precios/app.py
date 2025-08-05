from flask import Flask, render_template, request
import math

app = Flask(__name__)

def obtener_ganancia_porcentual(precio_usd):
    if precio_usd < 5:
        return 0.60
    elif 5 <= precio_usd < 15:
        return 0.55
    elif 15 <= precio_usd < 35:
        return 0.50
    elif 35 <= precio_usd < 70:
        return 0.40
    else:
        return 0.30

@app.route('/', methods=['GET', 'POST'])
def index():
    resultados = []
    total_ganancia = 0

    if request.method == 'POST':
        envio_usd = float(request.form['envio_usd'])
        impuesto_ars = float(request.form['impuesto_ars'])
        dolar_ars = float(request.form['dolar_ars'])

        productos = []
        for i in range(len(request.form.getlist('nombre'))):
            nombre = request.form.getlist('nombre')[i]
            precio_usd = float(request.form.getlist('precio_usd')[i])
            productos.append({'nombre': nombre, 'precio_usd': precio_usd})

        total_precio_usd = sum(p['precio_usd'] for p in productos)

        for producto in productos:
            proporcion = producto['precio_usd'] / total_precio_usd
            envio_ars = (envio_usd * dolar_ars) * proporcion
            impuesto_proporcional_ars = impuesto_ars * proporcion
            precio_ars = producto['precio_usd'] * dolar_ars
            costo_total = precio_ars + envio_ars + impuesto_proporcional_ars
            ganancia_pct = obtener_ganancia_porcentual(producto['precio_usd'])
            ganancia_monetaria = costo_total * ganancia_pct
            precio_final = costo_total + ganancia_monetaria
            total_ganancia += ganancia_monetaria

            resultados.append({
                'nombre': producto['nombre'],
                'precio_usd': producto['precio_usd'],
                'costo_sin_ganancia': round(costo_total, 2),
                'ganancia_pct': int(ganancia_pct * 100),
                'ganancia_ars': round(ganancia_monetaria, 2),
                'precio_final': round(precio_final, 2)
            })

    return render_template('index.html', resultados=resultados, total_ganancia=round(total_ganancia, 2))

if __name__ == '__main__':
    app.run(debug=True)
