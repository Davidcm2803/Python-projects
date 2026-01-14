#sintaxis clases:
#class + *nombre de la clase* + :
class Calculadora:
    #definicion de variables
    #sintaxis de variables
    #*nombre de variable* + = + *tipo de objeto o valor a usar*
    varA = 0
    varB = 0
    #definicion de funciones
    #sintaxis de funciones:
    #def + *nombre de funcion* + (self) + :
    def sumar(self):
        self.varA = 1500 #int(input("Ingrese el valor de A"))
        self.varB = 20
        resultado = self.varA + self.varB
        return resultado

    def resta(self):
        self.varA = 30
        self.varB = 20
        resultado = self.varA - self.varB
        return resultado

    def multiplica(self):
        self.varA = 30
        self.varB = 20
        resultado = self.varA * self.varB
        return resultado

    def dividir(self):
        self.varA = 100000
        self.varB = 2
        resultado = self.varA / self.varB
        return resultado

    def contarDigitos(self,valorCalculado):
        palabra = ""
        if (0 <= valorCalculado <= 9):
            palabra = "Un digito"
        elif (10 <= valorCalculado <= 99):
            palabra = "Dos digitos"
        elif (100 <= valorCalculado <= 999):
            palabra = "Tres digitos"
        elif (1000 <= valorCalculado <= 9999):
            palabra = "Cuatro digitos"
        else:
            palabra = "Cinco digitos o mas"

        return palabra

    def restarIteracion(self,resultadoFinal):
        restador = 0
        #listaNumeros = [1,2,3,4,5]
        # define for
        # sintaxis: for + *nombre de variable a usar en cada iteracion* + in + *contenedor o lista*:
        for numero in range(1,6):
            # codigo que se ejecuta siempre y cuando la condicion del while sea verdadera.
            # calculo de valor que resta al resultado final
            restador = restador + 10
            # calculo de resultado final:
            resultadoFinal = resultadoFinal - restador
            print(resultadoFinal)
        return resultadoFinal

#definicion de Objetos
#sintaxis de objetos/instanciacion
#*nombre de objeto a dar vida* + = + clase a instanciar.
casio = Calculadora
#sintaxis print
#print + (*lo que desea imprimir*)
print("El resultado de realizar una suma es:", casio.sumar(casio), ", y tiene:", casio.contarDigitos(casio,casio.sumar(casio)))
print("El resultado de realizar una resta es:",casio.resta(casio), ", y tiene:", casio.contarDigitos(casio,casio.resta(casio)))
print("El resultado de realizar una multiplicacion es:",casio.multiplica(casio), ", y tiene:", casio.contarDigitos(casio,casio.multiplica(casio)))
print("El resultado de realizar una division es:",casio.dividir(casio), ", y tiene:", casio.contarDigitos(casio,casio.dividir(casio)))
print("El resultado final al iterar 5 veces es:", casio.restarIteracion(casio,casio.sumar(casio)))
print("El resultado final al iterar 5 veces es:", casio.restarIteracion(casio,casio.resta(casio)))
print("El resultado final al iterar 5 veces es:", casio.restarIteracion(casio,casio.multiplica(casio)))
print("El resultado final al iterar 5 veces es:", casio.restarIteracion(casio,casio.dividir(casio)))