# Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande,
# cada uma sendo vendida respectivamente por 30, 35 e 40 reais.
# Construa um algoritmo em que o usuário forneça a quantidade de camisetas pequenas,
# médias e grandes referentes a uma venda, e a máquina informe quanto será o valor arrecadado.

#peq - pequeno - 30.00
#med - medio - 35.00
#gra - grande - 40.00


peq = int (input ("INFORME A QUANTIDADE DE CAMISETAS PEQUENAS: "))
med = int (input ("INFORME A QUANTIDADE DE CAMISETAS MÉDIAS: "))
gra = int (input ("INFORME A QUANTIDADE DE CAMISETAS GRANDES: "))

a = float (peq * 30.00)
b = float (med * 35.00)
c = float (gra * 40.00)

total = a + b + c

print ("TOTAL DA COMPRA: ",total)