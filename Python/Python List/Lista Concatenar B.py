class Ano:
    #Listas se definen = []
    listadoMesA = []
    listadoMesB = []

    def rellenarLista(self,lista):
        mes1 = input("Indique el 1er mes que desea agregar: ")
        mes2 = input("Indique el 2do mes que desea agregar: ")
        mes3 = input("Indique el 3er mes que desea agregar: ")
        mes4 = input("Indique el 4to mes que desea agregar: ")
        lista = [mes1,mes2,mes3,mes4]
        return lista

instanciaAno = Ano
print(instanciaAno.rellenarLista(instanciaAno,instanciaAno.listadoMesA))
print(instanciaAno.rellenarLista(instanciaAno,instanciaAno.listadoMesB))
#Len nos dice el tamano de la lista
print("La lista concatenada es: ", instanciaAno.listadoMesA + instanciaAno.listadoMesB)