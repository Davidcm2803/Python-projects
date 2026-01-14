import time     #Anade funciones de tiempo que hacen el resultado un poco mas comodo de ver

#Listas que almacenan los datos utilizados durante la ejecucion del codigo
usuarios = [['trador', 'admin@casapresidencial.com', '8969-4201', 'Casa presidencial']]
usuario_actual = []
desayunos = [['1', "Gallo pinto", 2200], ['2', "Orden de huevos", 900], ['3', "Tostadas", 900], ['4', "Sandwich de carne", 2000], ['5', "Sandwich de pollo", 2200]]
entradas = [['1', "Mozarella sticks", 3000], ['2', "Sopa pequeña", 1200], ['3', "Empanadas de carne", 1500]]
almuerzos = [['1', "Casado", 2500], ['2', "Sopa", 2000], ['3', "Pizza personal", 2800], ['4', "Sopa azteca", 2900], ['5', "Nachos", 2300], ['6', "Hot dog", 1100],
             ['7', "Burrito", 1500], ['8', "Quesadilla", 1400], ['9', "Hamburguesa", 1300], ['10', "Hamburguesa con queso", 1450], ['11', "Hamburguesa doble", 2200],
             ['12', "Hamburguesa triple", 3150], ['13',"Hamburguesa de pollo", 1800], ['14', "Empanada de carne", 1225], ['15', "Empanada de pollo", 1500],
             ['16', "Empanada de chicharron", 1700], ['17', "Taco", 850], ['18', "Super taco", 1475], ['19', "Chalupa", 2500]]
bebidas = [['1', "Refresco pequeño natural", 1000], ['2', "Refresco grande natural", 1800], ['3', "Refresco gaseosa pequeño", 1100], ['4', "Refresco gaseosa grande", 2000]]
postres = [['1', "Cheesecake", 2000], ['2', "Arroz con leche", 1500], ['3', "Helado", 1200]]
ordenes = []

##############################################################################################################

def menuPrincipal():
    print('Bienvenido a el sistema de pedidos de Fresh Express!')
    time.sleep(1)
    print('1. Ordenar en linea \n2. Menu \n3. Reportes \n4. Configuracion \n5. Salir')
    opcion = int(input('Digite el numero de opcion: '))
    if opcion == 1:
        ordenar()
    elif opcion == 2:
        menu()
    elif opcion == 3:
        reportes()
    elif opcion == 4:
        modificarCliente()
    elif opcion == 5:
        usuario_actual.clear()
        inicio()
    else:
        menuPrincipal()


def iniciarSesion():
    usuario_actual.clear()
    usuario = input('Digite su nombre de usuario: ')
    contra = input('Digite su contrasena: ')
    for i in usuarios:
        if i[0] == usuario:
            if i[1] == contra:
                print('Ingresando al sistema...')
                time.sleep(2)
                usuario_actual.append(i[0])
                menuPrincipal()
    print('Nombre de usuario o contrasena incorrectos!')
    inicio()

def crearCuenta():
    nuevoUsuario=[]
    nombre = str(input('Digite su nombre de usuario: '))
    for i in usuarios:
        if i[0] == nombre:
            print('Nombre de usuario ya en uso!')
            crearCuenta()
    contra = input('Digite su contrasena: ')
    nombreCompleto = str(input('Digite su nombre completo: '))
    correo = input('Digite su correo electronico: ')
    cel = input('Digite su numero de telefono: ')
    direccion = input('Digite su direccion de entrega: ')
    nuevoUsuario.append(nombre)
    nuevoUsuario.append(contra)
    nuevoUsuario.append(nombreCompleto)
    nuevoUsuario.append(correo)
    nuevoUsuario.append(cel)
    nuevoUsuario.append(direccion)
    usuarios.append(nuevoUsuario)
    print('Usuario creado con exito!')
    time.sleep(1)
    inicio()

def modificarCliente():
    cliente = input('Digite su nombre de usuario: ')
    contra = input('Digite su contrasena: ')
    for i in usuarios:
        if i[0] == cliente:
            if i[1] == contra:
                print('1. Editar usuario \n2. Editar contrasena \n3. Editar nombre \n4. Editar correo \n5. Editar celular \n6. Editar direccion \n7. Eliminar cuenta')
                opcion = int(input("Que desea editar: "))
                if opcion == 1:
                    nuevoUs = input('Digite el nuevo usuario del cliente: ')
                    for e in usuarios:
                        if e[0] == cliente:
                            e[0] = nuevoUs
                            menuPrincipal()
                elif opcion == 2:
                    nuevaContra = input('Digite la nueva contrasena del cliente: ')
                    for e in usuarios:
                        if e[0] == cliente:
                            e[1] = nuevaContra
                            menuPrincipal()
                elif opcion == 3:
                    nuevoNombre = input('Digite el nuevo nombre del cliente: ')
                    for e in usuarios:
                        if e[0] == cliente:
                            e[2] = nuevoNombre
                            menuPrincipal()
                elif opcion == 4:
                    nuevoCorreo = input('Digite el nuevo correo del cliente: ')
                    for e in usuarios:
                        if e[0] == cliente:
                            e[3] = nuevoCorreo
                            menuPrincipal()
                elif opcion == 5:
                    nuevoCel = input('Digite el nuevo celular del cliente: ')
                    for e in usuarios:
                        if e[0] == cliente:
                            e[4] = nuevoCel
                            menuPrincipal()
                elif opcion == 6:
                    nuevaDireccion = input('Digite la nueva direccion del cliente: ')
                    for e in usuarios:
                        if e[0] == cliente:
                            e[5] = nuevaDireccion
                            menuPrincipal()
                elif opcion == 7:
                    eliminarCliente()
                else:
                    modificarCliente()
                menuPrincipal()
    print('Usuario equivocado')
    inicio()

def eliminarCliente():
    x = input('Seguro que desea eliminar su cuenta? SI/NO:  ')
    if x == 'si' or x == 'SI' or x == 'Si' or x == 'sI':
        for i in usuarios:
            if i[1] == usuario_actual:
                usuarios.remove(i)
                print('Su cuenta ha sido eliminada con exito!')
                time.sleep(1)
                print('Volviendo al menu principal...')
                time.sleep(1)
                inicio()
    elif x == 'no' or x == 'NO' or x == 'No' or x == 'nO':
        menuPrincipal()


#Funcion que muestra las opciones para ingresar al sistema
def inicio():
    print('Bienvenido al Sistema de Fresh Express!')
    time.sleep(1.2)
    print('1. Iniciar Sesion \n2. Crear Cuenta \n3. Salir')
    x = int(input('Digite el numero de opcion para continuar en el sistema: '))
    if x == 1:
        iniciarSesion()
    elif x == 2:
        crearCuenta()
    elif x == 3:
        exit()
    else:
        print('Digite una opcion valida!')
        time.sleep(0.6)
        inicio()

def menu():
    print('1. Desayunos \n2. Entradas \n3. Almuerzos \n4. Bebidas \n5. Postres \n6. Volver')
    x = int(input('Digite el numero de opcion para continuar: '))
    if x == 1:
        for i in desayunos:
            print(i[0], ' -- ', i[1])
            time.sleep(0.3)
        time.sleep(2)
        menu()
    elif x == 2:
        for i in entradas:
            print(i[0], ' -- ', i[1])
            time.sleep(0.3)
        time.sleep(2)
        menu()
    elif x == 3:
        for i in almuerzos:
            print(i[0], ' -- ', i[1])
            time.sleep(0.3)
        time.sleep(2)
        menu()
    elif x == 4:
        for i in bebidas:
            print(i[0], ' -- ', i[1])
            time.sleep(0.3)
        time.sleep(2)
        menu()
    elif x == 5:
        for i in postres:
            print(i[0], ' -- ', i[1])
            time.sleep(0.3)
        time.sleep(2)
        menu()
    else:
        menuPrincipal()

def ordenar():
    nuevaOrden = []
    totalAPagar = 0
    t = 0
    while t != 1:
        print("Que platillo desea ordenar?")
        print('1. Desayunos \n2. Entradas \n3. Almuerzos \n4. Bebidas \n5. Postres \n6. Terminar orden \n7. Volver')
        x = int(input('Digite el numero de opcion para continuar: '))
        if x == 1:
            for i in desayunos:
                print(i[0], '...', i[1], '---', i[2])
                time.sleep(0.3)
            platillo = input('Digite el codigo del platillo para añadirlo: ')
            for a in desayunos:
                if platillo == a[0]:
                    nuevaOrden.append(a[1])
                    nuevaOrden.append(a[2])
                    totalAPagar += -a[2]
                    print("Platillo agregado al carrito")
                    time.sleep(1)
        if x == 2:
            for i in entradas:
                print(i[0], '...', i[1], '---', i[2])
                time.sleep(0.3)
            platillo = input('Digite el codigo del platillo para añadirlo: ')
            for a in entradas:
                if platillo == a[0]:
                    nuevaOrden.append(a[1])
                    nuevaOrden.append(a[2])
                    totalAPagar += a[2]
                    print("Platillo agregado al carrito")
                    time.sleep(1)
        if x == 3:
            for i in almuerzos:
                print(i[0], '...', i[1], '---', i[2])
                time.sleep(0.3)
            platillo = input('Digite el codigo del platillo para añadirlo: ')
            for a in almuerzos:
                if platillo == a[0]:
                    nuevaOrden.append(a[1])
                    nuevaOrden.append(a[2])
                    totalAPagar += a[2]
                    print("Platillo agregado al carrito")
                    time.sleep(1)
        if x == 4:
            for i in bebidas:
                print(i[0], '...', i[1], '---', i[2])
                time.sleep(0.3)
            platillo = input('Digite el codigo del platillo para añadirlo: ')
            for a in bebidas:
                if platillo == a[0]:
                    nuevaOrden.append(a[1])
                    nuevaOrden.append(a[2])
                    totalAPagar += a[2]
                    print("Platillo agregado al carrito")
                    time.sleep(1)
        if x == 5:
            for i in postres:
                print(i[0], '...', i[1], '---', i[2])
                time.sleep(0.3)
            platillo = input('Digite el codigo del platillo para añadirlo: ')
            for a in postres:
                if platillo == a[0]:
                    nuevaOrden.append(a[1])
                    nuevaOrden.append(a[2])
                    totalAPagar += a[2]
                    print("Platillo agregado al carrito")
                    time.sleep(1)
        if x == 6:
            for i in usuarios:
                if i[0] == usuario_actual[0]:
                    nuevaOrden.append(totalAPagar)
                    nuevaOrden.append(i[0])
                    nuevaOrden.append(i[2])
                    nuevaOrden.append(i[3])
                    nuevaOrden.append(i[4])
                    nuevaOrden.append(i[5])
                    for a in nuevaOrden:
                        print(a)
                        time.sleep(0.3)
                    print("TOTAL A PAGAR: ", totalAPagar)
                    print("---GRACIAS POR COMPRAR EN FRESH EXPRESS---")
                    time.sleep(1)
                    print("Esperamos su proximo pedido con ansias!")
                    time.sleep(2)
                    ordenes.append(nuevaOrden)

            menuPrincipal()
        if x == 7:
            menuPrincipal()

def reportes():
    contador = 1
    print("Buscando ordenes pasadas realizadas por: ", usuario_actual[0])
    time.sleep(2)
    if usuario_actual[0] == "admin":
        print("Usuario administrador")
        time.sleep(1)
        print("Cargando el historial de pedidos general...")
        time.sleep(2)
        print("Orden #", contador)
        contador += 1
        for pedidos in ordenes:
            for k in pedidos:
                print(k)
            print("############################################")
            time.sleep(1.5)
        menuPrincipal()
    for i in ordenes:
        for e in i:
            if e == usuario_actual[0]:
                print("Orden #", contador)
                contador += 1
                for a in i:
                    print(a)
                print("############################################")
                time.sleep(1.5)
    menuPrincipal()
inicio()