

# Escreva um método chamado roll_die() que exiba um número aleatório entre
# 1 e o número de lados do dado. Crie um dado de seis dados e lance-o dez
# vezes.
# Crie um dado de dez lados e outro de vinte lados. Lance cada dado dez
# vezes.
# import random
# class die:
#     def __init__(self,sides):
#         self.sides=6
# #     def rool_die(self,numero):
# import random
# class die:
#     def __init__(self,sides,aleatorio):
#         self.sides=6
#         self.aleatorio=aleatorio
#
#     def rool_dice(self,aleatorio,lados):
#         self.aleatorio=randint(1,6)
#         self.lados=self.sides
#         print(f"O numeros escolhido foi {self.aleatorio}")
#
import random
numeros=[1,6]
cont=0
class die():
    def __init__(self,lados,aleatorio):
       self.lados=lados
       self.aleatorio=aleatorio
    def rool_die(self):
        for aleatorio in numeros:
           
            print(f"O  numero de lados é {self.lados} e os numeros são{self.aleatorio}")
x=die(6,random.randrange(1,10))
x.rool_die()

















