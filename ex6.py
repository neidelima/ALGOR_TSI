# Um restaurante a quilo cobra R$45,00 o Kg de refeição. 
#Escreva um algoritmo que leia o peso do prato montado pelo cliente (em quilos) e imprima o valor a pagar. 
#Lembre-se que deve ser informado o peso do prato (tara), para que seja descontado do peso total.

# peso = peso da comida comprada
# tara = 250 gramas
# T = peso do prato menos a tara
# 

peso = float (input ("INFORME O PESO: "))


X = (peso - 250) * 45.0

total = X / 1000 

print ("VALOR DO PRATO: ", total)       


