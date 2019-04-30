def girar(lista):
    lista2= []
    word= ''
    for i in lista:
        for w in range(len(i)-1,-1,-1):
            word= word+i[w]
            if w==0:
                lista2.append(word)
                word= ''
    print(lista2)
            
def calcular(lista):
    longer= ''
    largo= 0
    for i in lista:
        if len(i)> largo:
            longer= i
            largo= len(i)
    print("La palabra más larga ingresada es", longer)

def agregarpalabra(lista):
    print("Ingrese la palabra deseada")
    word= input("Palabra: ")
    lista.append(word)
    print(word, "fue agregado a la lista.")
    return lista
    
def show_menu():
    print("#"*40)
    print("Escoja una opción:")
    print("1) Agregar una palabra.")
    print("2) Calcular la palabra más larga.")
    print("3) Girar las palabras de la lista.")
    print("4) Ver la lista.")
    print("5) Salir.")
               
def main(lista): #Nota: No es práctico que main() pida un parámetro.
    show_menu()
    opcion= int(input("Opción: "))
    if opcion==1:
        agregarpalabra(lista)
        return main(lista)
    elif opcion==2:
        calcular(lista)
        return main(lista)
    elif opcion==3:
        girar(lista)
        return main(lista)
    elif opcion==4:
        print(lista)
        return main(lista)
    elif opcion==5:
        print("Hasta luego! :)")
    else:
        print("Opción no válida.")
        return main(lista)

if __name__== '__main__':
        lista= []
        main(lista)
    
