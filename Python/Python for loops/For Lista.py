class Carro:
    marcaCarro = "Ford"
    modeloCarro = "Corolla"
    #sintaxis listas
    #*nombre de la lista* + = + [*elementos de la lista separados por comas*]
    netflix = ["Totoro","007","Red","Encanto"]

    def revisarModelo(self):
        #sintaxis:
        #for + *variable que representa cada item de la lista a revisar/checkear* + in + *nombre de lista* + :
        #for pelicula in netflix:
        for letra in self.modeloCarro:
            print("La letra actual es: " + letra)
        return self.modeloCarro

    def revisarPeliculas(self):
        for pelicula in self.netflix:
            print("La pelicula actual es: " + pelicula)
        return self.netflix

toyota = Carro
print(toyota.revisarPeliculas(toyota))
