import requests

def obtener_precio_dolar():
    """
    Consulta el precio del dólar oficial actual desde una API.
    """
    try:
        respuesta = requests.get("https://api.bluelytics.com.ar/v2/latest")
        data = respuesta.json()
        # Usamos el dólar blue (también podés cambiarlo a 'oficial' si querés)
        return data["blue"]["value_sell"]
    except Exception as e:
        print("No se pudo obtener el precio del dólar:", e)
        return None

def calcular_precios_en_pesos(lista_dolares, impuesto_en_pesos, dolar_actual):
    """
    Calcula el precio total en pesos: (precio + envío) * dólar + impuesto
    """
    precios_en_pesos = [(d * dolar_actual) + impuesto_en_pesos for d in lista_dolares]
    return precios_en_pesos

def convertir_entrada_a_lista(entrada):
    return [float(num.strip()) for num in entrada.split(',') if num.strip()]

if __name__ == "__main__":
    entrada = input("Ingrese precios en dólares separados por coma (ej: 25, 40, 60): ")
    numeros_dolares = convertir_entrada_a_lista(entrada)

    impuesto = float(input("Ingrese el impuesto fijo en pesos argentinos: "))

    dolar = obtener_precio_dolar()

    if dolar:
        resultado_en_pesos = calcular_precios_en_pesos(numeros_dolares, impuesto, dolar)

        print(f"\nPrecio actual del dólar: ${dolar:.2f} ARS")
        print(f"Impuesto fijo aplicado: ${impuesto:.2f} ARS")
        print(f"Precios en dólares: {numeros_dolares}")
        print(f"Precios totales en pesos argentinos: {resultado_en_pesos}")
