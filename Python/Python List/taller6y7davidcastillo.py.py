class super:
    articulo=input("que articulo desea comprar?: ")
    while True:
        try:
            valorarticulo=int(input("cuanto vale el articulo?: "))
            break
        except ValueError:
            print("Intenta un numero entero, intente de nuevo")
    while True:
        try:
            cantidadarticulo=int(input("cuantos articulos desea agregar?: "))
            break
        except ValueError:
            print("Intenta un numero entero, intente de nuevo")
    lista=[articulo,valorarticulo,cantidadarticulo]
    while True:
        continuar=int(input("presione 0 si desea agregar un articulo, presione 1 para continuar o 2 para terminar: "))
        if continuar==0:
            articulonuevo=(input("que otro articulo desea comprar?: "))
            nuevoarticulo=(int(input("cuanto vale este otro articulo?: ")))
            nuevacantidad=(int(input("cuantos articulos desea agregar?: ")))
            listas=[articulonuevo,nuevoarticulo,nuevacantidad]
            resultado=valorarticulo*cantidadarticulo
            resultados=nuevoarticulo*nuevacantidad
            resultadototal=resultado+resultados
            print:(resultadototal)
            descuento=int(input("cuanto descuento desea agregar para esta compra?: "))
            porcentaje =(descuento / 100)
            descuentofinal = (resultadototal * porcentaje)
            preciofinal = resultadototal-descuentofinal
            print("El precio de los productos con descuento es de:",preciofinal)
        elif continuar == 2:
            print("De nuevo el precio total es de:",preciofinal)
            break
        else:
            resultado=valorarticulo*cantidadarticulo
            preciofinal=resultado
            print:(resultado)
            descuento=int(input("cuanto descuento desea agregar para esta compra?: "))
            porcentaje =(descuento / 100)
            descuentofinal = (resultado * porcentaje)
            preciofinal = resultado-descuentofinal
            print("El precio con descuento es de:",preciofinal)
            break





