# 9.2 – Três restaurantes: Comece com a classe do Exercício 9.1. Crie três
# instâncias diferentes da classe e chame describe_restaurant() para cada
# instância.
class restaurante:

    def __init__(self, nome ,tipo):
        self.nome=nome
        self.tipo=tipo

    def descreve_restaurant(self):
        print(f"O restaurante de nome {self.nome} e o tipo de culinária é {self.tipo}")

    def restaurant_aberto(self):
        print("O restaurante está aberto")
restaurant=restaurante("Restaurante do Omar","Brasileira")
restaurant_2=restaurante("Restaurante do Gomez","Portuguesa")
restaurant_3=restaurante("Restaurante do Osaka","Japonesa")
restaurant.descreve_restaurant()
restaurant.restaurant_aberto()
print("\n")
restaurant_2.descreve_restaurant()
restaurant_2.restaurant_aberto()
print("\n")
restaurant_3.descreve_restaurant()
restaurant_3.restaurant_aberto()