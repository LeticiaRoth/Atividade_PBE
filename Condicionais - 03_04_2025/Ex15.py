import re

senha = input("Digite sua senha:")

if len(senha) < 8:
    print("A senha deve conter no mínimo 8 caracteres")

elif not re.search(r"[A-Z]", senha):
    print("A senha  deve conter pelo menos uma letra maiúscula")

elif not re.search(r"[a-z]", senha):
    print("A senha deve conter pelo menos uma letra minúscula")

elif not re.search(r"\d", senha):
    print("A senha deve conter pelo menos um número")

elif not re.search(r"[^A-Za-z0-9]", senha):
    print("A senha deve ter pelo menos um caractere especial")

else:
    print("Senha salva!")
