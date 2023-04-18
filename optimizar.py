class optimizar:

    # Creación de una varible tipo array
    array = []

    # Constructor con parámetro
    def __init__(self,array):
        self.array = array

    # Método que imprime "introduzca un numero", escanea 
    # por teclado y devuelvo el num introducido
    def input_numero(self) -> int:
        print("Introduzca un numero:")
        n = int(input())
        return n
    
    # Método para añadir un num que pasan por parametro al 
    # array y enviar un mensaje de aviso
    def anhadir_array(self, n):
        self.array.append(n)
        print(f"Numero {n} introducido en el array.")

    # Método para sumar los números del array, hacer su media, 
    # imprimirlo por pantalla y devolverlo
    def media_mostrar(self) -> int:
        suma = 0
        for n in self.array:
            suma = suma + n
        media = suma/len(self.array)
        print(f"La media es {suma}")
        return media
