# Admin: Um administrador é um tipo especial de usuário. Escreva uma
# classe chamada Admin que herde da classe User escrita no Exercício 9.3
# (página 226), ou no Exercício 9.5 (página 232). Adicione um atributo
# privileges que armazene uma lista de strings como "can add post", "can
# delete post" "can ban user", e assim por diante. Escreva um método chamado
# show_privileges() que liste o conjunto de privilégios de um administrador. Crie
# uma instância de Admin e chame seu método.
from usuarios import User
class Admin (User):
    def __init__(self,privileges):
        self.privileges=[privileges]
    def show_privileges(self):
        print(f"O conjunto de privilégios são {self.privileges}")
admin=Admin("can add post,""can delete post,""can ban user")
admin.show_privileges()