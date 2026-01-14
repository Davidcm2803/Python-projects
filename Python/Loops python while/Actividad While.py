
#define variables
contadorWhile = 0
resultado = 100
restador = 0
#define while
#sintaxis: while + (logica a comprobar) +:
while(contadorWhile<5):
    # codigo que se ejecuta siempre y cuando la condicion del while sea verdadera.
    #calculo de valor que resta al resultado final
    restador = restador + 10
    #iterador:
    contadorWhile = contadorWhile + 1
    #calculo de resultado final:
    resultado = resultado - restador
    print(resultado)