print("NANA's PIZZA")
print("_____ MENU _____")
print(" ")

print("******** SABORES PIZZA ********")
print(" CALABRESA, MILHO COM BACON, FRANGO COM CATUPIRY ")

print("******** PIZZAS - TAMANHO ********")
print(" PIZZA PEQUENA     R$ 19,90 ")
print(" PIZZA MÉDIA       R$ 29,90 ")
print(" PIZZA GRANDE      R$ 39,90 ")

print("******** REFRIGERANTES ********")
print(" COCA-COLA         R$ 9,50 ")
print(" GUARANÁ           R$ 8,50 ")
print(" SUCO             R$ 7,00 ")

print("______________________________")
print(" ")

print("FAÇA O SEU PEDIDO PARA PIZZA:")
print("1 - CALABRESA")
print("2 - MILHO COM BACON")
print("3 - FRANGO COM CATUPIRY")

print("______________________________\n")

print("FAÇA SEU PEDIDO:\n")

print("SABOR DA PIZZA:")
print("1 - CALABREZA")
print("2 - MILHO COM BACON")
print("3 - FRANGO COM CATUPIRY")
sabor = int(input("DIGITE O NÚMERO DO SABOR DE PIZZA: "))

print("")

print("TAMANHO DA PIZZA:")
print("P - PEQUENA")
print("M - MEDIA")
print("G - GRANDE")
tamanho = input("DIGITE O TAMANHO DA PIZZA: ").upper()

print("")

print("REFRIGERANTE:")
print("1 - COCA-COLA")
print("2 - GUARANÁ")
print("3 - SUCO")
refrigerante = int(input("DIGITE O NÚMERO DO SEU REFRIGERANTE: "))

print("")

valor = 0

# Calcular o valor da pizza

if sabor == 1:
    sabor = "CALABRESA"
elif sabor == 2:
    sabor = "MILHO COM BACON"
elif sabor == 3:
    sabor = "FRANGO COM CATUPIRY"
else:
    sabor="ERROR!"

if tamanho == "P":
    tamanho="PEQUENA"
    valor=valor+19.90
elif tamanho == "M":
    tamanho="MÉDIA"
    valor=valor+29.90
elif tamanho == "G":
    tamanho="GRANDE"
    valor=valor+39.90
else:
    tamanho="ERROR!"

if refrigerante == 1:
    refrigerante="COCA-COLA"
    valor=valor+9.50
elif refrigerante == 2:
    refrigerante="GUARANÁ"
    valor=valor+8.50
elif refrigerante == 3:
    refrigerante="SUCO"
    valor=valor+7.99
else:
    refrigerante="ERROR!"


print("#########################################################\n")
print(f"VALOR: {valor} R$\n")
print("SUA PIZZA:\n")
print("SABOR: "+ sabor)
print("TAMANHO: "+tamanho)
print("REFRIGERANTE: "+refrigerante)