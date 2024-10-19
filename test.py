# Solicitar dados do usuário
nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Critérios de peso e altura para ingresso no exército
peso_minimo = 50  # exemplo de peso mínimo
altura_minima = 1.60  # exemplo de altura mínima

# Verificando se atende aos requisitos
if peso < peso_minimo:
    resultado = "Você não atende ao peso mínimo para entrar no exército."
elif altura < altura_minima:
    resultado = "Você não atende à altura mínima para entrar no exército."
else:
    resultado = "Você atende aos requisitos para entrar no exército!"

# Exibir resultado
print(f"{nome}, {resultado}")
