#Limpiar correo que ingreso con espacios en blanco al inicio y al final
correo_con_espacios = "   usuario.prueba@gmail.com   "
correo_limpio = correo_con_espacios.strip() #Quitar espacios en blanco al inicio y al final (strip)

print("Correo limpio:", correo_limpio)
