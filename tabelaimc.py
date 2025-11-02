nome = input("Qual o seu nome? ")
peso = float(input(f"Qual o seu peso {nome}? [Kg] "))
altura = float(input("Qual a sua altura? [m] "))
imc = peso / (altura ** 2)
print(f"Seu IMC é {imc:.2f}")
if imc < 18.5:
    print("Abaixo do peso ")
elif imc < 25:
    print("Peso ideal ")
elif imc < 30:
    print("Sobrepeso")
elif imc < 40:
    print("Obesidade ")
else:
    print("Obesidade mórbida ")
            