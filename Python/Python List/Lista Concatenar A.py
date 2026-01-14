class Ano:
    #Listas se definen = []
    listadoMesA = []

    def rellenarLista(self,mesA,mesB,mesC,mesD):
        self.listadoMesA = [mesA, mesB, mesC, mesD]
        return self.listadoMesA

instanciaAno = Ano
mes1 = input("Indique el 1er mes que desea agregar: ")
mes2 = input("Indique el 2do mes que desea agregar: ")
mes3 = input("Indique el 3er mes que desea agregar: ")
mes4 = input("Indique el 4to mes que desea agregar: ")
#indices inician en 0
#instanciaAno.listadoMes = [mes1,mes2,mes3,mes4]
instanciaAno.rellenarLista(instanciaAno,mes1,mes2,mes3,mes4)
print(instanciaAno.listadoMesA)
listaMesB = ["Abril", "Marzo", "Junio", "Agosto"]
listaMesAB = instanciaAno.listadoMesA + listaMesB
#Len nos dice el tamano de la lista
print("La lista resultante final es: ", listaMesAB)