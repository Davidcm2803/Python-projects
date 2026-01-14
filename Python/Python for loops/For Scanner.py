class Carro:

    def revisarModelo(self, modelo):
        #sintaxis:
        #for + *variable que representa cada item de la lista a revisar/checkear* + in + *nombre de lista* + :
        #for pelicula in netflix:
        for letra in modelo:
            print("La letra actual es: " + letra)
        return modelo

    def revisarPeliculas(self, streaming, pelicularABuscar):
        for pelicula in streaming:
            print("La pelicula actual es: " + pelicula)
            if (pelicula == pelicularABuscar):
                print("Pelicula encontrada")
            #else:
            #   print("No hizo match la pelicula que busca en este momento")
        return streaming

toyota = Carro
print(toyota.revisarModelo(toyota,"Fortuner"))
print(toyota.revisarModelo(toyota,"4Runner"))
print(toyota.revisarModelo(toyota,"Land Cruiser"))
disney = ["Moana", "MCU", "SW"]
netflix = ["Squid Game", "Evangelion", "Pepa pig"]
peliculaA = "Moana"
peliculaB = "Evangelion"
print(toyota.revisarPeliculas(toyota,disney,peliculaA))
print(toyota.revisarPeliculas(toyota,netflix,peliculaB))
