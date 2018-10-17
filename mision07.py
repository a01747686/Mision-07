#Autor: Samantha Martínez Franco   A01747686
#Descripcion: uso de ciclos while para resolver operaciones y menus


#función que da resultado de divisiones por medio de resta
def dividir(divisor,dividendo):
    dividendoPrimero=dividendo
    cociente = 0
    while dividendo >= divisor:
        dividendo = dividendo - divisor
        cociente = cociente + 1
    print(dividendoPrimero, "/", divisor, "=", cociente, ", sobran ", dividendo)


#función que encuentra mayor de números
def encontrarMayor():
    mayor=0
    print("Teclea una serie de números para encontrar el mayor")
    numero = int(input("Teclea un número [-1 para salir]: "))
    if numero == -1:
        print("No hay valor mayor")
    else:

        while numero!=-1:
            if numero>=mayor:
                mayor=numero
            numero = int(input("Teclea un número [-1 para salir]: "))
        print("El mayor es: ", mayor)



#función principal
def main():   #sirve como menú
    opcion = int(input('''Mision 07. Ciclos while    
    Autor: Samantha Martínez Franco 
    Matrícula: A01747686
    1. Calcular divisiones
    2. Encontrar el mayor
    3. Salir
    Teclea tu opción:'''))
    print("")
    while opcion != 3:
        if opcion == 1 :
            dividendo = int(input("Dividendo: "))
            divisor = int(input("Divisor: "))
            if dividendo <= 0 or divisor <= 0:
                print("ERROR, Por favor escribe números positivos")
                dividendo = int(input("Dividendo: "))
                divisor = int(input("Divisor: "))
            dividir(divisor, dividendo)

        elif opcion == 2:
            encontrarMayor()
        else:
            print("ERROR, teclea 1, 2 o 3")
        opcion = int(input('''Mision 07. Ciclos while 
            Autor: Samantha Martínez Franco 
            Matrícula: A01747686
            1. Calcular divisiones
            2. Encontrar el mayor
            3. Salir
            Teclea tu opción:'''))
    print("Gracias por usar este programa, regresa pronto")


#llama función principal
main()