import os
from sqlite3 import Time
from turtle import clear
import time
from typing import List
clear= lambda:os.system("cls")

class hotel:
    #valor por noche por persona
    valordia=55000
    CamaQueen=10000
    CamaKing=7000
    metodosdepago=["\n Sinpe Movil: 88644028 \n Cuenta Bancaria: 1181819282832138 \n Presencialmente \n"]
    print("\n Bienvenido a nuestro sistema")
    time.sleep(0.3)
    usuario = input("\n Por favor ingrese su usuario: ")

    while usuario != "Jorge2022":
        print("\n El usuario es incorrecto, ingrese el usuario nuevamente ")
        usuario = input("\n Por favor ingrese su usuario correctamente: ")
    time.sleep(0.5)
    print("\nUsuario confirmado. Ingrese la contraseña")
    time.sleep(0.3)
    contrasena = input("\nPor favor ingrese su contraseña: ")
    while contrasena != "Killua":
        print("\n La contraseña es incorrecta, Por favor ingrese su contraseña: ")
        contrasena = input("\n Por favor ingrese su contraseña correctamente: ")
    time.sleep(1)    
    print("\nContraseña confirmada!")
    time.sleep(0.3)
    print("Bienvenido estimado" ,usuario, "puede empezar a reservar!!")
    time.sleep(5)

    def menu(self):
        clear()
        time.sleep(1)
        print("                 MENÚ \n1. Informacíon \n2. Reservar \n3. Salir \n")
        opcion=int(input("\n Seleccione el numero de la gestion que desea realizar: "))
        if opcion==1:
            self.informacion(self)
        
        elif opcion==2:
            self.reserva(self)
        elif opcion==3:
            print("gracias por usar el codigo")
        else:
            print("Intenta un número valido")
            time.sleep(2)
            self.menu(self)
        clear()          
    def informacion(self):
        time.sleep(1.5)
        clear()
        print("                 INFORMACIÓN \n \n El costo por noche tiene un valor de",self.valordia,"colones""\n A continuacion un listado con el descuento por personas\n 2 personas: 5%\n 3 personas: 10%\n 4 personas: 13%\n 5 o más personas: 15%\n")
        opcion=int(input("Si desea regresar al menu principal presione 1 o si desea salir presione 2: "))
        if opcion==1:
            self.menu(self)
        else:
            print("Gracias por usar el codigo")

    def reserva(self):
        time.sleep(1)
        clear()
        print("                 RESERVA \n")
        while True:
            try:
                self.personas=int(input("Para cuantas personas le gustaría reservar?:"))
                break
            except ValueError:
                print("\n Se permiten solamente numeros enteros")
        while True:
            try:
                self.dias=int(input("Cuantas noches quiere reservar?: "))
                break
            except ValueError:
                print("\n Se permiten solamente numeros enteros")
        while True:
            try:
                self.cuartos=int(input("Cuantas cuartos desea tener?: "))
                break
            except ValueError:
                print("\n Se permiten solamente numeros enteros")       
        self.Preciosindescuento=self.dias*self.valordia
        print("\n Total personas=",self.personas,"\n Total Dias=",self.dias,"\n Total cuartos=",self.cuartos,"\n")
        if (self.personas==2):
            self.descuento = (self.Preciosindescuento*0.05)
            self.totalpago=(self.Preciosindescuento-self.descuento)
        elif (self.personas==3):
            self.descuento = (self.Preciosindescuento*0.10)
            self.totalpago=(self.Preciosindescuento-self.descuento)
        elif (self.personas==4):
            self.descuento = (self.Preciosindescuento*0.13)
            self.totalpago=(self.Preciosindescuento-self.descuento)
        else:
            self.descuento = (self.Preciosindescuento*0.15)
            self.totalpago=(self.Preciosindescuento-self.descuento)
        opcion=int(input("Si desea más información acerca de los EXTRAS presione 1 o si desea pagar presione 2: "))
        if opcion==1:
            self.extras(self)
        elif opcion==2:
            self.pagosinextra(self)
        time.sleep(3)

    def extras(self):
        time.sleep(1)
        clear()
        print("                EXTRAS \n \n 1. Cama Queen Size tiene un costo de 10000 cada \n 2. King Size tiene un costo de 7000 cada una \n Camas individuales no tienen precio adicional")
        self.camas=int(input("\n Seleccione el número de la cama que quiere agregar o pulse 3 para pagar sin extras: "))
        if self.camas == 1:
            time.sleep(1)
            clear()
            print("                SELECCIÓN CAMAS \n")
            self.cantidadcamas=int(input("Cuantas Camas Queen desea?: "))
            self.mascamas=int(input("Seleccione 1 si desea agregar más camas, pulse 2 para agregar camas King o 3 para pagar: "))
            if self.mascamas == 1:
                self.mc=int(input("Cuantas Camas Queen desea agregar?: "))
                self.mq=self.mc*self.CamaQueen
                self.camasq=self.CamaQueen*self.mc
                self.totalextra=self.mq+self.camasq
                self.Pagototal=self.totalpago+self.totalextra
                clear()
                time.sleep(2)
                print("                MÉTODOS DE PAGO")
                for x in self.metodosdepago:
                    print(x)
                print("Estimado",self.usuario,"el monto a pagar en total seria",self.Pagototal,"colones")
                print("Te esperamos pronto en nuestras instalaciones!")
                time.sleep(10)
            elif self.mascamas == 2:
                time.sleep(1)
                self.mc=int(input("Cuantas Camas King desea?: "))
                self.camask=self.CamaKing*self.mc
                self.camasq=self.CamaQueen*self.cantidadcamas
                self.totalextra=self.camasq+self.camask
                self.Pagototal=self.totalpago+self.totalextra
                clear()
                time.sleep(2)
                print("                MÉTODOS DE PAGO")
                for x in self.metodosdepago:
                    print(x)
                print("Estimado",self.usuario,"el monto a pagar en total seria",self.Pagototal,"colones")
                print("Te esperamos pronto en nuestras instalaciones!")
                time.sleep(10)
            else:
                time.sleep(1)
                self.camasq=self.CamaQueen*self.cantidadcamas
                self.Pagototal=self.totalpago+self.camasq
                clear()
                time.sleep(2)
                print("                MÉTODOS DE PAGO")
                for x in self.metodosdepago:
                    print(x)
                print("Estimado",self.usuario,"el monto a pagar en total seria",self.Pagototal,"colones")
                print("Te esperamos pronto en nuestras instalaciones!")
                time.sleep(10)
            
        elif self.camas==2:
            time.sleep(2)
            clear()
            print("                SELECCIÓN CAMAS \n")
            self.cantidadcamas=int(input("Cuantas Camas King desea?: "))
            self.mascamas=int(input("Seleccione 1 si desea agregar más camas, pulse 2 para agregar camas Queen o 3 para pagar: "))
            if self.mascamas == 1:
                self.mc=int(input("Cuantas Camas King desea agregar?: "))
                self.mk=self.mc*self.CamaKing
                self.camask=self.CamaKing*self.cantidadcamas
                self.totalextra=self.mk+self.camask
                self.Pagototal=self.totalpago+self.totalextra
                clear()
                time.sleep(2)
                print("                MÉTODOS DE PAGO")
                for x in self.metodosdepago:
                    print(x)
                print("Estimado",self.usuario,"el monto a pagar en total seria",self.Pagototal,"colones")
                print("Te esperamos pronto en nuestras instalaciones!")
                time.sleep(10)
            elif self.mascamas == 2:
                self.mc=int(input("Cuantas Camas Queen desea?: "))
                self.camasq=self.CamaQueen*self.mc
                self.camask=self.CamaKing*self.cantidadcamas
                self.totalextra=self.camasq+self.camask
                self.Pagototal=self.totalpago+self.totalextra
                clear()
                time.sleep(2)
                print("                MÉTODOS DE PAGO")
                for x in self.metodosdepago:
                    print(x)
                print("Estimado",self.usuario,"el monto a pagar en total seria",self.Pagototal,"colones")
                print("Te esperamos pronto en nuestras instalaciones!")
                time.sleep(10)
            else:
                self.camask=self.CamaKing*self.cantidadcamas
                self.Pagototal=self.totalpago+self.camask
                clear()
                time.sleep(2)
                print("                MÉTODOS DE PAGO")
                for x in self.metodosdepago:
                    print(x)
                print("Estimado",self.usuario,"el monto a pagar en total seria",self.Pagototal,"colones")
                print("Te esperamos pronto en nuestras instalaciones!")
                time.sleep(10)
        elif self.camas == 3:
            self.pagosinextra(self)

    def pagosinextra(self):
        clear()
        time.sleep(2)
        print("                MÉTODOS DE PAGO")
        for x in self.metodosdepago:
            print(x)
        print("Estimado",self.usuario,"el monto a pagar en total seria",self.totalpago,"colones")
        print("Te esperamos pronto en nuestras instalaciones!")
        time.sleep(10)

Riu=hotel
print(Riu.menu(Riu))