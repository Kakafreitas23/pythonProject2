class restaurante():
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

    def descreve_restaurant(self):
        print(f"O restaurante de nome {self.nome} e o tipo de culinária é {self.tipo}")

    def restaurant_aberto(self):
        print("O restaurante está aberto")

class IceCreamStand(restaurante):
    def __init__(self,flavors):
        self.flavors=flavors

    def sabores(self):
        print(f"Os sorvetes são de sabores {self.flavors}")

ice_cream_Stand=IceCreamStand("Chocolate,Morango e Flocos")
ice_cream_Stand.sabores()
restaurant = restaurante("Restaurante do Omar", "Brasileira")
restaurant.descreve_restaurant()
restaurant.restaurant_aberto()
