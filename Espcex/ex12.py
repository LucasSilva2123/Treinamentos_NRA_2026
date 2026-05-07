nome = str(input("Qual é o seu nome completo? ")).strip()
palavra = nome.split()
palavracorrigida = " ".join(palavra)
print("O seu nome apenas com letras maiúsculas é: {}".format(palavracorrigida.upper()))
print("O seu nome apenas com letras minúsculas é: {}".format(palavracorrigida.lower()))
print("O seu nome tem {} letras.".format(len(nome.replace(" ",""))))
print("O seu primeiro nome tem {} letras.".format(len(nome.split()[0])))


