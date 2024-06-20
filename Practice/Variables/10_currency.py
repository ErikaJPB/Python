pesos = int(input('What do you have left in pesos? '))
soles = int(input('What do you have left in soles? '))
reales = int(input('What do you have left in reales? '))

total = pesos * 0.00024 + soles * 0.27 + reales * 0.18

print(total)