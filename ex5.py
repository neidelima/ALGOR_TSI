#Um motorista deseja colocar no seu tanque X reais de gasolina.
# Escreva um algoritmo para ler o preço do litro da gasolina e o valor do pagamento,
#e exibir quantos litros ele conseguiu colocar no tanque.

#preço- valor da gasolina
#x - valor a ser abastecido
#L - litros

preço = float (input ("INFORME O PREÇO DO LITRO DA GASOLINA: "))
valor = float (input ("INFORME VALOR A SER GASTO: "))

L = valor / preço

#roud => ARREDONDA O VALOR DE LITROS COM 3 CASAS

arred = round (L, 2)

print (arred, "litros")






