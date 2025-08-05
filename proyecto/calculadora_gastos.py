def calcular_precio_final(precio_producto, costo_envio_total, impuestos_total, cantidad_productos):
    """
    Calcula el precio final de venta de un producto considerando envío, impuestos y margen de ganancia.
    
    Args:
        precio_producto: Precio original del producto
        costo_envio_total: Costo total del envío
        impuestos_total: Total de impuestos
        cantidad_productos: Cantidad de productos
        
    Returns:
        float: Precio final de venta por unidad
    """
    # Distribuir el costo de envío e impuestos entre todos los productos
    costo_envio_por_producto = costo_envio_total / cantidad_productos
    impuestos_por_producto = impuestos_total / cantidad_productos
    
    # Calcular el costo total por producto
    costo_total = precio_producto + costo_envio_por_producto + impuestos_por_producto
    
    # Aplicar el margen de ganancia del 70%
    precio_venta = costo_total * 1.7
    
    return precio_venta

def main():
    print("=== CALCULADORA DE PRECIOS PARA PRODUCTOS IMPORTADOS ===")
    
    try:
        # Obtener información general del envío
        cantidad_productos = int(input("Ingrese la cantidad total de productos: "))
        costo_envio_total = float(input("Ingrese el costo total del envío: $"))
        impuestos_total = float(input("Ingrese el total de impuestos de importación: $"))
        
        # Lista para almacenar información de productos
        productos = []
        
        # Ingresar datos de cada producto
        for i in range(cantidad_productos):
            print(f"\n--- Producto {i+1} ---")
            nombre = input("Nombre del producto: ")
            precio = float(input(f"Precio original de {nombre}: $"))
            
            precio_final = calcular_precio_final(precio, costo_envio_total, impuestos_total, cantidad_productos)
            
            productos.append({
                "nombre": nombre,
                "precio_original": precio,
                "precio_final": precio_final
            })
        
        # Mostrar resumen
        print("\n=== RESUMEN DE PRECIOS ===")
        for producto in productos:
            print(f"{producto['nombre']}:")
            print(f"  Precio original: ${producto['precio_original']:.2f}")
            print(f"  Precio de venta recomendado: ${producto['precio_final']:.2f}")
            print(f"  Ganancia: ${(producto['precio_final'] - producto['precio_original']):.2f}")
            print()
            
        print("Nota: El precio de venta incluye costo de envío, impuestos y un 70% de ganancia.")
        
    except ValueError:
        print("Error: Por favor ingrese valores numéricos válidos.")
    except ZeroDivisionError:
        print("Error: La cantidad de productos no puede ser cero.")

if __name__ == "__main__":
    main()