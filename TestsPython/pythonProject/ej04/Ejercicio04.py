def kaprekar(numero):
    vueltas = 0
    limite = 7
    objetivo = 6174
    aux = numero


    """
    este bucle funciona para las pruebas con numeros no iguales y numeros de 4 digitos
    falta implementar los numeros más pequeños de 4 dígitos y condicionales que no permitan números no válidos
    """
    while( int(aux) != objetivo and vueltas <= limite):
        numAsc = ordenaAsc(str(aux))
        numDes = ordenaDes(str(aux))
        aux = int(numDes) - int(numAsc)
        vueltas = vueltas + 1



    """
    Esto es para el primer test del kaprekar
        numAsc = ordenaAsc(str(aux))
        numDes = ordenaDes(str(aux))
        aux = int(numDes) - int(numAsc)
        if(int(aux) == objetivo):
            vueltas = vueltas + 1
    """
    """Esto es para los demás tests antes de la implementación del bucle, en los que sabíamos cuantas veces se repetia
        numAsc = ordenaAsc(str(aux))
        numDes = ordenaDes(str(aux))
        aux = int(numDes) - int(numAsc)
        numAsc = ordenaAsc(str(aux))
        numDes = ordenaDes(str(aux))
        aux = int(numDes) - int(numAsc)
        numAsc = ordenaAsc(str(aux))
        numDes = ordenaDes(str(aux))
        aux = int(numDes) - int(numAsc)
        if(int(aux) == objetivo):
            vueltas = vueltas + 1
    
    """




    return vueltas


def ordenaAsc(numero):
    numeroLista = sorted(str(numero))
    numeroAsc = ''.join(numeroLista)

    return numeroAsc

def ordenaDes(numero):
    numeroLista = sorted(str(numero), reverse=True)
    numeroDes = ''.join(numeroLista)

    return numeroDes