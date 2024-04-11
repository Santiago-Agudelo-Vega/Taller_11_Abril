import os

mi_diccionario = {}
sw = True

def fnt_agregar(diccionario, Nombre, Contacto):
    if Nombre == '' or Contacto == '':
        print('Debe diligenciar toda la información solicitada')
    else:
        if Contacto in diccionario:
            print(f'El contacto {Contacto} ya existe en la agenda')
        else:
            diccionario[Contacto] = {'Nombre': Nombre, 'Contacto': Contacto}
            print(f'\nEl contacto {Nombre} ha sido registrado con éxito')

def fnt_selector(op):
    if op == '1':
        os.system('cls')
        Nombre = input('Nombre:  ')
        Contacto = input('Contacto:  ')
        fnt_agregar(mi_diccionario, Nombre, Contacto)
    elif op == '2':
        os.system('cls')
        buscar = input('Buscar por Nombre o Contacto: ')
        resultado_busqueda = buscar_contacto(mi_diccionario, buscar)
        if resultado_busqueda:
            print(f'\nResultado de la búsqueda para "{buscar}": {resultado_busqueda}')
        else:
            print(f'\nNo se encontró ninguna coincidencia para "{buscar}"')
        input('\n\nPresione ENTER para continuar...')
        

def buscar_contacto(agendatelefonica, nombre_o_contacto):
    for contacto, info in agendatelefonica.items():
        if nombre_o_contacto.lower() in info['Nombre'].lower() or nombre_o_contacto.lower() in contacto.lower():
            return info
    return None

while sw:
    os.system('cls')
    opcion = input('1. Registrar contactos\n2. Buscar contacto\n3. Mostrar Contactos\n4. Salir\n- >  ')
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
