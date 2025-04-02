dia = int(input("Digite o dia:\n"))
mes = int(input("Digite o mês:\n"))
ano = int(input("Digite o ano:\n"))

if mes < 1 or mes > 12:
    print("Data digitada está inválida!")
else:

    if mes == 2:

        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):

            if dia < 1 or dia > 29:
                print("Data digitada está inválida!")
            else:
                print(
                    f"\nData no formato atual: {dia}/{mes}/{ano}.\nData no novo formato: {ano}-{mes}-{dia}.")

        else:
            if dia < 1 or dia > 28:
                print("Data está inválida!")
            else:
                print(
                    f"\nData no formato atual: {dia}/{mes}/{ano}.\nData no novo formato: {ano}-{mes}-{dia}.")

    elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia < 1 or dia > 31:
            print("A data digitada está inválida!")
        else:
            print(
                f"\nData no formato atual: {dia}/{mes}/{ano}.\nData no novo formato: {ano}-{mes}-{dia}.")

    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia < 1 or dia > 30:
            print("Data está inválida!")
        else:
            print(
                f"\nData no formato atual: {dia}/{mes}/{ano}.\nData no novo formato: {ano}-{mes}-{dia}.")
