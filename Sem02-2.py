print("raton", "gato", "perro", sep=" ")
print("raton", "gato", "perro", sep=" ")

print("Ingrese la edad:")
edad = int(input())     # int.parse(Console.ReadLine())
print(f"En 10 años tendra {edad+10}")

edad = int(input("Ingrese la edad:\n"))
print(f"En 10 años tendra {edad+10}")

#Metodos o Funciones 
def Imprimir(texto):
    print(texto)

def Suma10edad(edad):
    return edad + 10

Imprimir("Hola")
print(Suma10edad(20))