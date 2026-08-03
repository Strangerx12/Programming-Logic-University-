# Obtener el precio de un producto utilizando el método get() en un diccionario
inventario_tienda = {"manzana": 1.50, "pera": 2.00, "uva": 3.25}
precio_manzana = inventario_tienda.get("manzana") # En caso de que no exista la clave "manzana" se retornará None

print("Precio de la manzana:", precio_manzana)
