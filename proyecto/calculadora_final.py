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

def calcular_precios(productos, envio_usd, impuesto_ars, dolar_ars):
    total_precio_usd = sum(p['precio_usd'] for p in productos)

    for producto in productos:
        # Proporción del producto respecto al total en USD
        proporcion = producto['precio_usd'] / total_precio_usd

        # Costo proporcional de envío e impuesto
        envio_ars = (envio_usd * dolar_ars) * proporcion
        impuesto_proporcional_ars = impuesto_ars * proporcion

        # Precio en ARS
        precio_ars = producto['precio_usd'] * dolar_ars
        costo_total = precio_ars + envio_ars + impuesto_proporcional_ars

        # Ganancia
        ganancia_porcentual = obtener_ganancia_porcentual(producto['precio_usd'])
        precio_final = costo_total * (1 + ganancia_porcentual)

        producto['ganancia'] = ganancia_porcentual * 100
        producto['precio_final'] = precio_final

    return productos

# --- Entradas generales ---
envio_usd = float(input("Costo total de envío (USD): "))
impuesto_ars = float(input("Impuesto total en pesos argentinos (ARS): "))
dolar_ars = float(input("Cotización del dólar (USD a ARS): "))

# --- Ingreso de productos ---
productos = []

while True:
    nombre = input("Nombre del producto (o 'fin' para terminar): ")
    if nombre.lower() == 'fin':
        break
    precio_usd = float(input(f"Precio en USD de '{nombre}': "))
    productos.append({"nombre": nombre, "precio_usd": precio_usd})

# --- Cálculo ---
productos_calculados = calcular_precios(productos, envio_usd, impuesto_ars, dolar_ars)

# --- Resultados ---
print("\n--- Resultados por producto ---")
for p in productos_calculados:
    print(f"Producto: {p['nombre']}")
    print(f"  Precio USD: {p['precio_usd']}")
    print(f"  Ganancia aplicada: {p['ganancia']}%")
    print(f"  Precio final de venta: ${p['precio_final']:.2f} ARS\n")
