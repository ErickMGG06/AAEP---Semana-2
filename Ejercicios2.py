cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
votoTotal = 0
voto = int

while voto != 0:
    
    print("Ingrese su voto: ")
    voto = int(input())
    votoTotal += 1
    match voto:
        case 1: 
            print("\nVoto contado\n")
            cont1 += 1 
        case 2: 
            print("\nVoto contado\n") 
            cont2 += 1
        case 3: 
            print("\nVoto contado\n") 
            cont3 += 1
        case 4: 
            print("\nVoto contado\n") 
            cont4 += 1
print(f"El cantidato 1 tiene: {cont1} con un {(cont1/votoTotal)*100}%")
print(f"El cantidato 2 tiene: {cont2} con un {(cont2/votoTotal)*100}%")
print(f"El cantidato 3 tiene: {cont3} con un {(cont3/votoTotal)*100}%")
print(f"El cantidato 4 tiene: {cont4} con un {(cont4/votoTotal)*100}%")



