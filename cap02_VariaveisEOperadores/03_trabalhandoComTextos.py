from os import system
system("cls")
nomeCompleto = input("Informe o seu nome completo:")
print("1. Quantidade de caracteres do nome: ", len(nomeCompleto))
print("2. Nome em maiúsculo: ", nomeCompleto.upper())
print("3. Nome em minúsculo: ", nomeCompleto.lower())
print("4. Primeira letra maiúscula: ", nomeCompleto.capitalize())
espaco = nomeCompleto.find(" ")
print("5. Primeiro nome: ", nomeCompleto[0:espaco])
print("6. Nome sem espaços: ", nomeCompleto.replace(" ", ""))
print("7. Possui somente letras? (precisamos tirar os espaços)",
      nomeCompleto.replace(" ", "").isalpha())
print("8. É alfanumérico? tem letras OU números (precisamos tirar os espaços)",
      nomeCompleto.replace(" ", "").isalnum())
print("Quebrar o texto a cada espaço em branco: ", nomeCompleto.split(" "))
print("10. Para centralizar o nome com o caracter *")
print(nomeCompleto.center(80, "*"))
