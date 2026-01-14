class Carro:
    marcaCarro = "Ford"
    modeloCarro = "Corolla"

    def revisarModelo(self):
        #sintaxis:
        #for + *variable que representa cada item de la lista a revisar/checkear* + in + *nombre de lista* + :
        #for pelicula in netflix:
        for letra in self.modeloCarro:
            print("La letra actual es: " + letra)
        return "Finalizando for"

toyota = Carro
print(toyota.revisarModelo(toyota))
