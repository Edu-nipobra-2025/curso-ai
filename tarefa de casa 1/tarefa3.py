def idade(idadeUser):

    return idadeUser


idadeUser = int(input("Dê sua idade: \n"))

if idadeUser < 18:
    print("Você é menor de idade.")
elif idadeUser >= 18:
 print("Você é maior de idade.")