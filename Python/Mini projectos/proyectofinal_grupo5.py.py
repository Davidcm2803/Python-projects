class programa:
    print("Bienvenido a nuestro sistema")
    usuario = input("\n Por favor ingrese su usuario: ")

    while usuario != "u":
        print("\n El usuario es incorrecto, ingrese el usuario nuevamente ")
        usuario = input("\n Por favor ingrese su usuario correctamente: ")

    print("\nUsuario confirmado. Ingrese la contraseña")
    contrasena = input("\nPor favor ingrese su contraseña: ")
    while contrasena != "c":
        print("\n La contraseña es incorrecta, Por favor ingrese su contraseña: ")
        contrasena = input("\n Por favor ingrese su contraseña correctamente: ")

    print("\nContraseña confirmada!, bienvenido estimado", usuario, "puede empezar a trabajar")

    print("\nAgregue los datos personales del cliente")
    cedula = input("\n Por favor ingrese la cédula del cliente: ")
    nombre = input("\n Por favor ingrese el nombre completo del cliente: ")
    direccion = input("\n Por favor ingrese la dirección del cliente: ")
    celular = input("\n Por favor ingrese el número de celular del cliente: ")
    correo = input("\n Por favor ingrese la correo del cliente: ")

    print("\nIntroduzca los siguientes datos necesarios para el calculo de cuota del nuevo préstamo")
    while True:
        try:
            monto = float(input("\n Por favor ingrese el monto del crédito: "))
            break
        except ValueError:
            print("\n Se permiten numeros enteros o con decimales, por favor intente de nuevo.")

    while True:
        try:
            plazo = float(input("\n Por favor ingrese el plazo en meses del crédito: "))
            break
        except ValueError:
            print("\n Se permiten numeros enteros, por favor intente de nuevo.")


    print("\nIntroduzca los siguientes datos requisitos de la empresa")
    while True:
        try:
            mayorde20 = float(input("\n ¿Cuál es la edad del cliente?: "))
            break
        except ValueError:
            print("\n Se permiten numeros enteros o con decimales, por favor intente de nuevo")

    while True:
        try:
            puntajesic = float(input("\n ¿Cuál es el puntaje del SIC del cliente?: "))
            break
        except ValueError:
            print("\n Se permiten numeros enteros, por favor intente de nuevo.")

    while True:
        try:
            colaborador = float(input("\n ¿El usuario es colaborador de la empresa? \n 1.Sí:  \n 2.No: "))
            while 1 != colaborador != 2:
                colaborador = float(input("\n Formato incorrecto. Por favor introduzca. \n 1.Sí:  \n 2.No: "))
            else:
                break
        except ValueError:
            print("\n Formato incorrecto. Por favor introduzca. \n 1.Sí \n 2.No")

    listacreditos = []
    listatarjetas = []

    def principal(self):

        print(self.calculocapacidaddepago(self))
        print("Nombre completo es: ", self.nombre, "\nNúmero de cédula: ", self.cedula, "\nDirección: ", self.direccion, "\nnúmero de celular: ", self.celular, "\ncorreo electronico: ", self.correo)
        print("\nLa cuota del préstamo solicitado por un monto de", self.monto, " colones a un plazo de ", self.plazo, " meses es de: ", self.calculocuota(self))
        print("\nEl valor total de las cuotas de los créditos es ", sum(self.listacreditos))
        print("Valores individuales de las cuotas de los créditos", self.listacreditos)
        print("\nEl valor total de las cuotas de las tarjetas es ", sum(self.listatarjetas))
        print("Valores individuales de las cuotas de las tarjetas ", self.listatarjetas)
        print(self.politicas(self))

        return print("\n Gracias por usar el software!")


    def calculocuota(self):
        tasa = 0.13
        cuota = (self.monto * tasa) / (1 -(1/((1+tasa) ** self.plazo)))
        cuotast = cuota
        return round(cuotast, 2 )

    def tienecreditos(self):
        print("\nDatos para calculo del monto total de las cuotas de sus créditos.")
        tienecredito = input(str("\n ¿El cliente posee algún crédito?, eliga una opción. \n 1.Sí: \n 2.No: "))
        totalcuotacredito = 0
        while "1" != tienecredito != "2":
            tienecredito = input(str("\n Formato incorrecto. Por favor introduzca. \n 1.Sí:  \n 2.No: "))

        else:
            if tienecredito == "1":
                continuar = True

                while continuar == True:

                    while True:
                        try:
                            cuotacredito = float(input("\n Ingrese la cuota del credito: "))
                            break
                        except ValueError:
                            print("\n Se permiten numeros enteros o con decimales, por favor intente de nuevo")
                    self.listacreditos.append(cuotacredito)
                    totalcuotacredito = totalcuotacredito + cuotacredito

                    deseacontinuar = input(str("\n ¿El cliente posee más créditos?, eliga una opción. \n 1.Sí:  \n 2.No: "))

                    while "1" != deseacontinuar != "2":
                        deseacontinuar = input(str("\n Formato incorrecto. Por favor introduzca. \n 1.Sí:  \n 2.No: "))

                    else:

                        if deseacontinuar == "2":
                            continuar = False
                else:
                    print("\n Gracias por ingresar todos los datos del cliente.")
        return totalcuotacredito

    def tienetarjetas(self):
        print("\nDatos para el calculo del monto total de las cuotas de sus tarjetas de crédito.")
        tienetarjeta = input(str("\n ¿El cliente posee alguna tarjeta de crédito?, eliga una opción. \n 1.Sí:  \n 2.No: "))
        totalcuotatarjeta = 0
        while "1" != tienetarjeta != "2":
            tienetarjeta = input(str("\n Formato incorrecto. Por favor introduzca. \n 1.Sí: \n 2.No: "))

        else:
            if tienetarjeta == "1":
                continuar = True

                while continuar == True:

                    while True:
                        try:
                            cuotatarjeta = float(input("\n Ingrese la cuota de su tarjeta de credito "))
                            break
                        except ValueError:
                            print("\n Se permiten numeros enteros o con decimales, por favor intente de nuevo")

                    self.listatarjetas.append(cuotatarjeta)
                    totalcuotatarjeta = totalcuotatarjeta + cuotatarjeta

                    deseacontinuar = input(str("\n ¿El cliente posee más tarjetas de crédito?, eliga una opción. \n 1.Sí:  \n 2.No: "))

                    while "1" != deseacontinuar != "2":
                        deseacontinuar = input(str("\n Formato incorrecto. Por favor introduzca. \n 1.Sí:  \n 2.No: "))

                    else:

                        if deseacontinuar == "2":
                            continuar = False
                else:
                    print("\nGracias por ingresar todos los datos del cliente.")

        return totalcuotatarjeta

    def calculocapacidaddepago(self):
        print("\nPor favor ingrese la siguiente información para el calculo de la capacidad de pago del cliente: ")
        while True:
            try:
                salariobruto = float(input("\n Ingrese su salario bruto: "))
                break
            except ValueError:
                print("\n Se permiten numeros enteros o con decimales, por favor intente de nuevo.")
        while True:
            try:
                salarioliquido = float(input("\n Ingrese su salario líquido: "))
                break
            except ValueError:
                print("\n Se permiten numero enteros o con decimales, intente de nuevo.")

        calculocapacidaddepago = (    ( (salariobruto)-(self.tienetarjetas(self) + self.tienecreditos(self)  + self.calculocuota(self))) / ((salarioliquido)) * 100 )
        return print("\n La capacidad de pago es ", round(calculocapacidaddepago, 2 ), "porciento.")

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

        return print("\nSu nota segun las politicas de la empresa es de: ", nota)

credito = programa
print(credito.principal(credito))
