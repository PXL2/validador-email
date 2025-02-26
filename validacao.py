import re

def validar_email(email):
    validacao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(validacao, email):
        return True
    else:
        return False

email = ""
if validar_email(email):
    print("E-mail válido")
else:
    print("E-mail inválido")