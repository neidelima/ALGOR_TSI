#Uma padaria vende uma certa quantidade de pães franceses e uma quantidade de broas a cada dia. Cada pãozinho custa R$ 0,50 e a broa custa R$ 1,50. 
#Ao final do dia, o dono quer saber quanto arrecadou com a venda dos pães e broas (juntos), e
#quanto deve guardar numa conta de poupança (10% do total arrecadado). Faça um algoritmo para ler as quantidades de pães e de broas,
#e depois calcular os dados solicitados.


# p é a quantidade de pães
# b é a quantidade de broas
#vp é o valor  dos pães vendidos no dia  = 0,50 cada
#vb é o valor das broas vendidas no dia = 1,50 cada
# t é o valor total de broas e pães

p = int (input("Quantidade de pães vendidos: "))
b = int (input("Quantidade de broas vendidas: "))
vp = float (input("Valor do pão: "))
vb = float (input("Valor da broa: "))

vp = p * vp
vb = b * vb
total = vp + vb
poup = total / 10.0

print ("Foram vendidos o valor de pães: ", vp)
print ("Foram vendidos o valor de broas: ", vb)
print ("Foram vendidos o valor total de pães e broas: ", total)
print ("Devem ser guardado: ", poup)