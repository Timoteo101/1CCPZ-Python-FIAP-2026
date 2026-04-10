from numpy.ma.core import true_divide

idade = 20

maior_idade = idade >= 18
print(maior_idade, type(maior_idade))



print()

verif_email = True
verif_senha = False

login = verif_email and verif_senha
print(login)

if not login:
    print("Fernando burão")

print()


nota_final = 2

if nota_final < 4:
    print("Reprovado")

elif nota_final < 6:
    print("Recuperação")

else:
    print("Aprovado")

print("Fim")

