from optimizar import optimizar

def test_anhadir_array():
    op = optimizar([])
    op.anhadir_array(5)
    op.anhadir_array(7)
    op.anhadir_array(3)
    op.anhadir_array(5)
    op.anhadir_array(2)
    assert len(op.array) == 5

def test_sumar_mostrar():
    op = optimizar([6, 4, 2, 8, 0])
    assert op.sumar_mostrar() == 4



