
def calcula_cinematica(valor1, valor2):
    #resultado que se retorna en la funcion
    res = 'parametro invalido'
    #maneja excepciones relacionadas los valores introducido
    try:
        numero1 = obtiene_numero(valor1)
        numero2 = obtiene_numero(valor2)
        letra1 = obtiene_letra(valor1)
        letra2 = obtiene_letra(valor2)
    except Exception as e:
        return res
    #maneja excepciones relacionadas con que un divisor sea 0
    try:

        #dependiendo de que letra se haya introducido se hace una operacion distinta, tambien comprueba que se pongan
        #en orden los dividendos y divisores

        #v=d/t
        if (letra1 == 'D' and letra2 == 'T') or (letra1 == 'T' and letra2 == 'D'):
            if letra1 == 'D':
                calculo = int(numero1) / int(numero2)

            else:
                calculo = int(numero2) / int(numero1)
            calculo = int(calculo)
            res = 'V=' + str(calculo)
        #d=v*t
        elif (letra1 == 'V' and letra2 == 'T') or (letra1 == 'T' and letra2 == 'V') :
            calculo = int(numero1) * int(numero2)
            calculo = int(calculo)
            res = 'D=' + str(calculo)
        #t=d/v
        elif (letra1 == 'D' and letra2 == 'V') or (letra1 == 'V' and letra2 == 'D') :
            if letra1 == 'D':
                calculo = int(numero1) / int(numero2)
            else:
                calculo = int(numero2) / int(numero1)
            calculo = int(calculo)
            res = 'T=' + str(calculo)

    except Exception as e:
        return "No se puede dividir entre 0"

    return res

#saca la letra de una cadena con formato A=0
def obtiene_letra(valor):
        res = valor.split('=', 1)
        letra = res[0]
        return str(letra)

#saca el numero de una cadena con formato A=0
def obtiene_numero(valor):
    res = valor.split('=', 1)
    numero = res[1]
    return int(numero)