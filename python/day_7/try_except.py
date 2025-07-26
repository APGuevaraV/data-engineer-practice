try:
    fichero = open('productos_n.txt', 'r')
    if fichero:
        print('Archivo abierto correctamente')
except FileNotFoundError:
    print('Fichero no encontrado')
