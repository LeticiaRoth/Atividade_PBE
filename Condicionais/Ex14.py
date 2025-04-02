data = input("Digite uma data no formato dd/mm/yyyy: ")

if len(data) == 10 and data[2] == '/' and data[5] == '/':
    dia, mes, ano = data.split('/')

    nova_data = f"{ano}/{mes}/{dia}"
    print("A data no formato yyyy/mm/dd é:", nova_data)
else:
    print("Formato de data inválido. Por favor, insira no formato dd/mm/yyyy.")