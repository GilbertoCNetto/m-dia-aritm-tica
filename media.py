n1 = float(input("Digite sua primeira nota:"))
n2 = float(input("Digite sua segunda nota:"))
m = (n1 + n2) / 2
if m >= 6:
    print(f"Sua média foi de {m}, você esta aprovado!! ")
elif m >= 4:
    print(f"Sua média foi de {m}, você esta de recuperação")
else:
    print(f"Sua média foi de {m}, você esta reprovado")
