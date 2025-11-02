nome = input("Qual o seu nome? ")
peso = float(input(f"Qual o seu peso {nome}? [Kg] "))
altura = float(input("Qual a sua altura? [m] "))
imc = peso / (altura ** 2)
print(f"Seu IMC é {imc:.2f}")
if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc < 24.9:
    print("Peso normal")
elif imc > 25 and imc < 29.9:
    print("Sobrepeso")
            