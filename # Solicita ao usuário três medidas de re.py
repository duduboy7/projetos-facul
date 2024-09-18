# Solicita ao usuário três medidas de retas
a = float(input("Digite o comprimento da primeira reta: "))
b = float(input("Digite o comprimento da segunda reta: "))
c = float(input("Digite o comprimento da terceira reta: "))

# Verifica se as retas podem formar um triângulo
if a + b > c and a + c > b and b + c > a:
    print("As retas podem formar um triângulo.")
else:
    print("As retas NÃO podem formar um triângulo.")