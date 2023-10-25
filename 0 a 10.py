# Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e
# continue pedindo até que o usuário informe um valor válido.
numero_escolhido=int(input("Digite um número entre 0 e 10 : "))
while numero_escolhido:
    if numero_escolhido<0:
        print("Invalido")
        numero_escolhido = int(input("Digite um número entre 0 e 10 : "))
    else:
        print("Valido")
        break


