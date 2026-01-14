class Vivero:
    #variables
    cantidadDePlantas = 0
    tipoDePlanta = ""

    #funciones
    def contarPlantas(self):
        frase = ""
        #sintaxis While
        #while + (*Condicion que mientras sea True, va a continuar repitiendo el ciclo.*) + :
        while (self.cantidadDePlantas < 10):
            #Encontro una nueva planta para contar, por lo tanto agregamos 1 al inventario
            self.cantidadDePlantas = self.cantidadDePlantas + 1
        frase = "He contado 10 plantas hoy, seguire manana..."
        return frase

    def limpiarMalaHierba(self):
        frase = ""
        #inicializo cantidad de mala hierba
        cantidadDeMalaHierba = 15
        #defino el while
        while (self.tipoDePlanta=="Mala Hierba"):
            #Logica para eliminar la mala hierba
            cantidadDeMalaHierba = cantidadDeMalaHierba - 1
            #flag/bandera de que ya no hay mala hierba y por lo tanto salir del ciclo.
            if (cantidadDeMalaHierba == 0):
                self.tipoDePlanta = "Buena Hierba"
            else:
                print("Limpieza en proceso...")
        frase = "Limpieza finalizada"
        return frase

#instancia
LaBonita = Vivero
LaBonita.tipoDePlanta = "Mala Hierba"
print(LaBonita.limpiarMalaHierba(LaBonita))


