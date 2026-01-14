class Vivero:
    #variables
    cantidadDePlantas = 0

    #funciones
    def contarPlantas(self):
        frase = ""
        #sintaxis While
        #while + (*Condicion que mientras sea True, va a continuar repitiendo el ciclo.*) + :
        while (self.cantidadDePlantas < 10):
            #Encontro una nueva planta para contar, por lo tanto agregamos 1 al inventario
            self.cantidadDePlantas = self.cantidadDePlantas + 1
            if (self.cantidadDePlantas == 5):
                print("La 5ta mata se la comieron gatos")
                continue
            print("Planta actual:", self.cantidadDePlantas)
        frase = "He contado 9 plantas hoy, seguire manana..."
        return frase

#instancia
LaBonita = Vivero
print(LaBonita.contarPlantas(LaBonita))




