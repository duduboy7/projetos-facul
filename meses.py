# Dicionário que mapeia números para nomes dos meses
meses = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

# Lê o valor inteiro da entrada
numero_mes = int(input().strip())

# Imprime o nome do mês correspondente
if 1 <= numero_mes <= 12:
    print(meses[numero_mes])
else:
    print("Número inválido")