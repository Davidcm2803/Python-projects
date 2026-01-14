class programa:
    usuario = input("Introduzca su usuario: ")
    contrasena = input("Introduzca su contraseña: ")

    while usuario != "u":
        print("usuario incorrecto")
        usuario = input("Ingrese su usuario: ")
    else:
        print("Siga con la contraseña")
    while contrasena !="p":
        print("Contraseña o usuario incorrecto")
        contrasena = input("Ingrese su contraseña: ")
    else:
        print("Bienvenido al sistema")
        
    print("Agregue sus datos personales")
    cedula = input("Ingrese su numero de cedula: ")
    nombre = input("Ingrese su nombre completo: ")
    direccion = input("Ingrese su dirección: ")
    celular = input("Ingrese su numero de celular: ")
    correo = input("Ingrese su correo electrónico: ")

    print("Calculo de cuota del nuevo préstamo")
    monto = float(input("Monto total del préstamo: "))
    plazo = float(input("Plazo en meses: "))

    print("Requisitos de la empresa")
    mayorde20 = int(input("¿Cuántos años tiene?:"))
    puntajesic = int(input("¿Cuál es su puntaje del CIC?: "))
    colaborador = int(input("¿El usuario es colaborador de la empresa? 1 para si o 2 para no: "))


    listacreditos = []
    listatarjetas = []

    def principal(self):

        print("El resumen de datos del cliente es el siguiente")
        print(self.calculocapacidaddepago(self))
        print("Nombre completo es: ", self.nombre, "\nNúmero de cédula: ", self.cedula, "\nDirección: ", self.direccion, "\nnúmero de celular: ", self.celular, "\ncorreo electronico: ", self.correo)
        print(self.calculocuota(self))
        print("El valor total de las cuotas de los créditos es ", sum(self.listacreditos))
        print("Valores individuales de las cuotas de los créditos", self.listacreditos)
        print("El valor total de las cuotas de las tarjetas es ", sum(self.listatarjetas))
        print("Valores individuales de las cuotas de las tarjetas ", self.listatarjetas)
        print(self.politicas(self))

        return print("Gracias por usar el software")


    def calculocuota(self):
        tasa = 0.12
        cuota = (self.monto * tasa) / (1 -(1/((1+tasa) ** self.plazo)))
        cuotast = str(cuota)
        return print("La cuota del nuevo prestamo es ", cuotast)

    def tienecreditos(self):
        print("Datos para calculo del monto total de las cuotas de sus créditos")
        tienecredito = input ("¿Tiene algun credito?  si o no: ")
        totalcuotacredito = 0
        if tienecredito == "si":
            continuar = True

            while continuar == True:
                cuotacredito = float(input("Ingrese la cuota de su credito: "))
                self.listacreditos.append(cuotacredito)
                totalcuotacredito = totalcuotacredito + cuotacredito
                deseacontinuar = input ("¿Tiene más creditos? si o no: ")
                if deseacontinuar == "no":
                    continuar = False
            else:
                print("Seguimos con las tarjetas de credito")
        return totalcuotacredito

    def tienetarjetas(self):
        print("Datos para el calculo del monto total de las cuotas de sus tarjetas de crédito")
        tienetarjeta = input ("¿Tiene alguna tarjeta de credito?  si o no: ")
        totalcuotatarjeta = 0
        if tienetarjeta == "si":
            continuar = True

            while continuar == True:
                cuotatarjeta = float (input("Ingrese la cuota de su tarjeta de credito: "))
                self.listatarjetas.append(cuotatarjeta)
                totalcuotatarjeta = totalcuotatarjeta + cuotatarjeta
                deseacontinuar = input ("¿Tiene más tarjetas? si o no: ")
                if deseacontinuar == "no":
                    continuar = False
            else:
                print("Gracias por ingresar todos los datos")

        return totalcuotatarjeta

    def calculocapacidaddepago(self):
        print("Vamos a calcular su capacidad de pago")
        salariobruto = float(input("Ingrese su salario bruto: "))
        salarioliquido = float(input("Ingrese su salario líquido: "))
        calculocapacidaddepago = (((salariobruto) - (self.tienecreditos(self) + self.tienetarjetas(self)))/(salarioliquido))*100
        return print("La capacidad de pago es ", calculocapacidaddepago, "porciento.")

    def politicas(self):
        nota = 100
        lista2 = [0, 0, 0]
        if self.mayorde20 <= 20:
            lista2[0] = 1
        if self.puntajesic != 1:
            lista2[1] = 1
        if self.colaborador == 2:
            lista2[2]= 1
        for numero in lista2:
            if numero == 1:
                nota = nota - 10

        return print("Su nota segun las politicas de la empresa es de: ", nota)

credito = programa
print(credito.principal(credito))