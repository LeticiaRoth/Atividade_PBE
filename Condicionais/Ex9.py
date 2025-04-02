total = int(input("Digite o total da compra:"))

if total < 100:
    calculo = total * 0.5
    print(f"O total com desconto é igual {total - calculo}")
elif total >=  100 and total < 500:
    calculo = total * 0.10
    print(f"O total com desconto é igual {total - calculo}")
else:
    calculo = total * 0.15
    print(f"O total com desconto é igual {total - calculo}")