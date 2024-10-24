from Ejercicio01 import cesar

def test_Cesar():
    assert cesar("a", 2) == "c"
    assert cesar("ab", 2) == "cd"
    assert cesar("y", 5) == "d"


