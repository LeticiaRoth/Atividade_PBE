nota = float (input("Digite a nota:"))
if nota < 0 or nota > 10:
    print(f"Nota inválida")

elif nota >= 9:
    print(f"A")

elif nota >= 7:
    print(f"B")

elif nota >= 5:
    print(f"C")

elif nota >= 3:
    print(f"D")

else:
    print(f"E")