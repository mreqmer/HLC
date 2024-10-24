from Ejercicio02 import calcula_cinematica

#comprueba cuando el res es velocidad
def test_cinematica():
    assert calcula_cinematica ("D=32", "T=4") == "V=8"
#comprueba cuando el res es desplazamiento
def test_cinematica2():
    assert calcula_cinematica ("V=2", "T=3") == "D=6"
#comprueba cuando el res es tiempo
def test_cinematica3():
   assert calcula_cinematica("D=4", "V=2") == "T=2"
#comprueba cuando el res es velocidad, pero la T y la D estan invertidos
def test_cinematica4():
    assert calcula_cinematica ("T=4", "D=8") == "V=2"
#comprueba cuando el res es desplazamiento, pero con la T y la V invertidas
def test_cinematica5():
    assert calcula_cinematica ("T=4", "V=8") == "D=32"
#comprueba cuando el res es tiempo, pero la D y la V están invertidas
def test_cinematica6():
   assert calcula_cinematica("V=8", "D=32") == "T=4"
#parametro invalido
def test_cinematica7():
    assert calcula_cinematica("a", "b") == "parametro invalido"
# parametro invalido
def test_cinematica8():
    assert calcula_cinematica("a", "b") == "parametro invalido"
# parametro invalido
def test_cinematica9():
    assert calcula_cinematica("V=8", "b") == "parametro invalido"
#comprueba cuando tiempo es divisor y es 0
def test_cinematica10():
    assert calcula_cinematica ("D=4", "T=0") == "No se puede dividir entre 0"
#comprueba cuando velocidad es divisor y es 0
def test_cinematica11():
    assert calcula_cinematica ("D=4", "V=0") == "No se puede dividir entre 0"
#comprueba cuando algún parametro no es valido pero no hace saltar una excepcion
def test_cinematica12():
    assert calcula_cinematica ("D/4", "V=2") == "parametro invalido"
#comprueba cuando algún parametro no es valido pero no hace saltar una excepcion
def test_cinematica13():
    assert calcula_cinematica ("SADSA=4", "V=2") == "parametro invalido"
#comprueba cuando se le mete algun parametro en minuscula
def test_cinematica14():
    assert calcula_cinematica ("d=32", "T=4") == "parametro invalido"