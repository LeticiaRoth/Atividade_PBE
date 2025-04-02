import re

cpf = input("Digite o seu CPF:\n")
padrao = r"\d{3}\.\d{3}\.\d{3}\-\d{2}"
val = re.match(padrao, cpf)

if val:
    primeiro_verificador = ((int(cpf[0]) * 10) + (int(cpf[1]) * 9) + (int(cpf[2]) * 8) + (int(cpf[4]) * 7) + (int(cpf[5]) * 6) + (int(cpf[6]) * 5) + (int(cpf[8]) * 4) + (int(cpf[9]) * 3) + (int(cpf[10]) * 2)) % 11
    segundo_verificador = ((int(cpf[0]) * 11) + (int(cpf[1]) * 10) + (int(cpf[2]) * 9) + (int(cpf[4]) * 8) + (int(cpf[5]) * 7) + (int(cpf[6]) * 6) + (int(cpf[8]) * 5) + (int(cpf[9]) * 4) + (int(cpf[10]) * 3) + (int(cpf[12]) * 2)) % 11

    if primeiro_verificador >= 2:
        digito1 = 11 - primeiro_verificador
    else:
        digito1 = 0
    if segundo_verificador >= 2:
        digito2 = 11 - segundo_verificador
    else:
        digito2 = 0

    if int(cpf[12]) == digito1 and int(cpf[13]) == digito2:
        print("O CPF é válido")
    else:
        print("O CPF é inválido")
else:
    print("O CPF não foi digitado corretamente")
