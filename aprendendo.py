# 10.1 – Aprendendo Python: Abra um arquivo em branco em seu editor de texto e
# escreva algumas linhas que sintetizem o que você aprendeu sobre Python até
# agora. Comece cada linha com a expressão Em Python podemos.... Salve o
# arquivo como learning_python.txt no mesmo diretório em que estão seus
# exercícios deste capítulo. Escreva um programa que leia o arquivo e mostre o
# que você escreveu, três vezes. Exiba o conteúdo uma vez lendo o arquivo todo,
# uma vez percorrendo o objeto arquivo com um laço e outra armazenando as
# linhas em uma lista e então trabalhando com ela fora do bloco with.
# 10.2 – Aprendendo C: Você pode usar o método replace() para substituir
# qualquer palavra por uma palavra diferente em uma string. Eis um exemplo
# rápido que mostra como substituir a palavra 'dog' por 'cat' em uma frase:
# >>> message = "I really like dogs."
# >>> message.replace('dog', 'cat') 'I really like cats.'
# Leia cada linha do arquivo learning_python.txt que você acabou de criar e
# substitua a palavra Python pelo nome de outra linguagem, por exemplo, C.
# Mostre cada linha modificada na tela.
p=open("exemplo.txt","r")
print(p.read())

