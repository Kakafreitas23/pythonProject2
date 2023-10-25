class User:
    def __init__(self,first_name,last_name,age,height,login_attempts):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.height=height
        self.login_attempts=login_attempts
    def describe_user(self):
        print(f"O Usuário tem o nome {self.first_name} de sobrenome {self.last_name},"
              f"possui a idade {self.age} anos "f"e altura de {self.height} ")

    def greet_user(self):
        print(f"Olá {self.first_name},seja bem vindo a Empresa!")

    def increment_login_attempts(self,valor):
        self.login_attempts+=valor
        print(f"o login é {self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts=0
        print(f"o reset do valor é {self.login_attempts}")

usuario=User("Alberto","Gomez",34,1.89,0)
usuario_2=User("Miguel","Luiz",21,1.73,0)
usuario_3=User("Bruno","Carvalho",50,1.80,0)
usuario.describe_user()
usuario.greet_user()
usuario.increment_login_attempts(1)
usuario.reset_login_attempts()
print("\n")
usuario_2.describe_user()
usuario_2.greet_user()
usuario_2.increment_login_attempts(1)
usuario_2.reset_login_attempts()
print("\n")
usuario_3.describe_user()
usuario_3.greet_user()
usuario_3.increment_login_attempts(1)
usuario_3.reset_login_attempts()