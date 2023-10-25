class Carro():
    def __init__(self,modelo,ano,preco):
        self.modelo=modelo
        self.ano=ano
        self.preco=preco

    def carro_definiçoes(self):
        print(f"O carro escolhido foi do {self.modelo},o ano foi {self.ano} e o preço foi de {self.preco} reais")

class bateria(Carro):
    def __init__(self,voltagem,marca,ano):
        self.voltagem=voltagem
        self.marca=marca
        self.ano=ano
    def carro_bateria(self):
        print(f"A voltagem da bateria é {self.voltagem}V a marca da bateria é {self.marca} e o ano da bateria é {self.ano}")

carros=Carro("SUV",2022,100000)
carros.carro_definiçoes()
baterias=bateria(12,"moura".title(),2021)
baterias.carro_bateria()
