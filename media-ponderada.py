n1 = float(input("Digite a primeira nota (peso2): "))
n2 = float(input("Digite a segunda nota (peso 4): "))
n3 = float(input("Digite a terceira nota (peso 8): "))

media_ponderada = (n1 * 2 + n2 * 4 + n3 * 8) / (2 + 4 + 8)

print(f'A média ponderada é: {media_ponderada:.2f}')