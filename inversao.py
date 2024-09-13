def inverter_string(s):
    lista_chars = list(s)
    
    inicio = 0
    fim = len(lista_chars) - 1
    while inicio < fim:
        lista_chars[inicio], lista_chars[fim] = lista_chars[fim], lista_chars[inicio]
        inicio += 1
        fim -= 1
    return ''.join(lista_chars)

entrada = input("digite a palavra (string) que deseja inverter: ")
print("palavra invertida:", inverter_string(entrada))
