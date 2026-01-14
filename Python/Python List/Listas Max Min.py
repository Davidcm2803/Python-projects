class Ano:
    #Listas se definen = []
    listadoMes = []

    def rellenarLista(self,mesA,mesB,mesC,mesD):
        self.listadoMes = [mesA,mesB,mesC,mesD]
        return self.listadoMes

    def valorMaxLista(self,lista):
        return max(lista)

    def valorMinLista(self,lista):
        return min(lista)



instanciaAno = Ano
mes1 = input("Indique el 1er mes que desea agregar: ")
mes2 = input("Indique el 2do mes que desea agregar: ")
mes3 = input("Indique el 3er mes que desea agregar: ")
mes4 = input("Indique el 4to mes que desea agregar: ")
#indices inician en 0
#instanciaAno.listadoMes = [mes1,mes2,mes3,mes4]
instanciaAno.rellenarLista(instanciaAno,mes1,mes2,mes3,mes4)
print(instanciaAno.listadoMes)
print("El valor maximo de la lista es: ", instanciaAno.valorMaxLista(instanciaAno,instanciaAno.listadoMes))
print("El valor minimo de la lista es: ", instanciaAno.valorMinLista(instanciaAno,instanciaAno.listadoMes))
