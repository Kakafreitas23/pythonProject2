
#4.12 – Mais laços: Todas as versões de foods.py nesta seção evitaram usar
#laços for para fazer exibições a fim de economizar espaço. Escolha uma
#versão de foods.py e escreva dois laços for para exibir cada lista de comidas.

pizzas=["Alho","Calabresa","Frango","Peperoni","Portuguesa"]
friend_pizzas=pizzas[0:]
pizzas.append("Muçarela")
friend_pizzas.append("Bacon")

print("Minhas Pizzas favoritas são : {}".format(pizzas))
for p in pizzas:
    print(p)

print("As Pizzas favoritas do meu amigo são : {} ".format(friend_pizzas))


for f in friend_pizzas:
    print(f)


my_foods = ['pizza', 'falafel', 'carrot cake']
your_favorite_food=['pizza', 'falafel', 'carrot cake', 'cannoli']

for m in my_foods:
    print(m)


for y in your_favorite_food:
    print(y)