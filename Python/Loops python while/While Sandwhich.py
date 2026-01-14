class Persona:

    #variables
    tieneHambre = True

    #funcion
    def comer(self):
        frase = ""
        cereal = 10
        sandwhich = 15
        while (self.tieneHambre==True):
            cereal = cereal - 2
            sandwhich = sandwhich - 1
            print("Comiendo...")
            if (cereal == 0 or sandwhich == 0):
                self.tieneHambre = False
        frase = "Se agoto alguno de los dos productos"
        return frase

jorge = Persona
print(jorge.comer(jorge))