import os

mi_diccionario = {}
sw = True

def fnt_agregar(diccionario, Titulo, Genero, año):
    if Titulo == '' or Genero == '' or año == '':
        print('Debe diligenciar toda la información solicitada')
    else:
        if Titulo in diccionario:
            print(f'La pelicula "{Titulo}" ya existe en la agenda')
        else:
            diccionario[Titulo] = {'Titulo': Titulo, 'Genero': Genero,'Año': año}
            print(f'\nLa pelicula {Titulo} ha sido registrada con éxito')

def fnt_selector(op):
    if op == '1':
        os.system('cls')
        Titulo = input('Titulo:  ')
        Genero = input('Genero:  ')
        año = input('Año: ')
        fnt_agregar(mi_diccionario, Titulo, Genero, año)
    elif op == '2':
        os.system('cls')
        buscar = input('Buscar por Titulo o Genero: ')
        resultado_busqueda = buscar_pelicula(mi_diccionario, buscar)
        if resultado_busqueda:
            print(f'\nResultado de la búsqueda para "{buscar}": {resultado_busqueda}')
        else:
            print(f'\nNo se encontró ninguna coincidencia para "{buscar}"')
        input('\n\nPresione ENTER para continuar...')
        

def buscar_pelicula(Peliculas1, nombre_o_genero):
    for titulo, info in Peliculas1.items():
        if nombre_o_genero.lower() in info['Titulo'].lower() or nombre_o_genero.lower() in info ['Genero'].lower():
            return info
    return None

while sw:
    os.system('cls')
    opcion = input('1. Registrar Titulo\n2. Buscar Peliculas\n3. Mostrar Peliculas\n4. Salir\n- >  ')
    if opcion == '1':
        fnt_selector(opcion)
    elif opcion == '2':
        os.system('cls')
        fnt_selector(opcion)
    elif opcion == '3':
        os.system('cls')
        print('\nCantidad de registros: ',len(mi_diccionario),'\n')
        for clave, valor in mi_diccionario.items():
            print(f"{clave}: {valor}")
        input('\n\nPresione ENTER para continuar...')
    elif opcion == '4':
        sw = False
