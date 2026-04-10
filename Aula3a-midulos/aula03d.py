#imagina.. um sistema que recolha a escolha do usario
# escolha o usuari
# se...
#0 -> sair do programa
#1 -> entar no programa
#-> erro!

escolha_usuario = 1

match escolha_usuario:
    case 0:
        print("sair do programa")
    case 1:
        print("entar do programa")
    case _:
        print("erro!!")