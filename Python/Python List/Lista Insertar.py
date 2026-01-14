class Ano:
    #Listas se definen = []
    listadoMes = []

    def rellenarLista(self,lista,mesA,mesB,mesC,mesD):
        lista = [mesA,mesB,mesC,mesD]
        return lista

    def agregarValorALista(self,lista,valor):
        #append agrega el valor al final de la lista
        lista.append(valor)
        return lista

    def insertarALista(self,lista,indice,valor):
        lista.insert(indice,valor)
        return lista

instanciaAno = Ano
mes1 = input("Indique el 1er mes que desea agregar: ")
mes2 = input("Indique el 2do mes que desea agregar: ")
mes3 = input("Indique el 3er mes que desea agregar: ")
mes4 = input("Indique el 4to mes que desea agregar: ")
#indices inician en 0
#instanciaAno.listadoMes = [mes1,mes2,mes3,mes4]
instanciaAno.listadoMes = instanciaAno.rellenarLista(instanciaAno,instanciaAno.listadoMes,mes1,mes2,mes3,mes4)
print(instanciaAno.listadoMes)
valorAAgregar = input("Favor ingrese el siguiente mes a agregar: ")
print(instanciaAno.agregarValorALista(instanciaAno,instanciaAno.listadoMes,valorAAgregar))
valorAAgregar2 = input("Favor ingrese el siguiente mes a agregar: ")
indiceDeNuevoValor = int(input("Indique el indice donde desea agregar el nuevo elemento a la lista: "))
instanciaAno.insertarALista(instanciaAno,instanciaAno.listadoMes,indiceDeNuevoValor,valorAAgregar2)
print("El elemento: " + valorAAgregar2 + " va a ser agregado en el indice: ", indiceDeNuevoValor, "por lo tanto la lista ahora es:" )
print(instanciaAno.listadoMes)