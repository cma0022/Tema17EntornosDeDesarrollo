class optimizar:

    array=[]

    def __init__(self,array):
        self.array = array

    def input_numero(self) -> int:
        print("Introduzca un numero:")
        n = int(input())
        return n

    def anhadir_array(self, n):
        self.array.append(n)
        print(f"Numero {n} introducido en el array.")

    def uso_metodo(self):
        for _ in range (3):
            self.introducir_numero()

    def sumar_mostrar(self) -> int:
        suma = 0
        for n in self.array:
            suma = suma + n
        media = suma/len(self.array)
        print(f"La media es {suma}")
        return media