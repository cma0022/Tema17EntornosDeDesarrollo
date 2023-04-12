from optimizar import optimizar

# La cobertura de código no es del 100% debido a que uno de los método
# utiliza un input

# Método tipo test. Crea un objeto de la clase optimizar, añade 5 
# numeros al array y se comprueba la longitud de este
def test_anhadir_array():
    op = optimizar([])
    op.anhadir_array(5)
    op.anhadir_array(7)
    op.anhadir_array(3)
    op.anhadir_array(5)
    op.anhadir_array(2)
    assert len(op.array) == 5

# Método tipo test. Crea un objeto de la clase optimizar con 5 valores
#  en el array y se comprueba que la media de estos valores sea 4
def test_sumar_mostrar():
    op = optimizar([6, 4, 2, 8, 0])
    assert op.sumar_mostrar() == 4



