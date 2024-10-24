

abcdario = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

def cesar(cadena, pasos):
    resCadena = ""
    pasosReales = pasos % 27

    for letra in cadena:
        indice = abcdario.index(letra)
        nuevoIndice = indice + pasosReales
        if (nuevoIndice > len(abcdario)):
            nuevoIndice = nuevoIndice - len(abcdario)
            resCadena += abcdario[nuevoIndice]
        else:
            resCadena += abcdario[nuevoIndice]



    return resCadena






