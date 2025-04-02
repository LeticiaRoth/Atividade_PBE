idade = int (input("Digite sua idade:"))

if idade >= 18 and idade < 70:
    print(f"Voto obrigatório")

elif idade == 16 or idade == 17 or idade >70:
    print("Voto opcional")

else:
    print("Não tem voto")