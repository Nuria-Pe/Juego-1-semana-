import random

empiezacon = 0
print("Hola! ¿Cómo te llamas?")
minombre = input()
numero = random.randint(1, 15)
print('Genial, ' + minombre + ', Estoy pensando en un número entre el 1 y el 15.')

while empiezacon < 6:
    print('Adivina el número.') 
    adivina = input()
    adivina = int(adivina)
    empiezacon = empiezacon + 1
    if adivina < numero:
        print('Tu número es muy bajo.') 
    if adivina > numero:
        print('Tu número es muy alto.')
    if adivina == numero:
        break

if adivina == numero:
    empiezacon = str(empiezacon)
    print('Bien, ' + minombre + '! Has adivinado mi número en ' + empiezacon + ' intentos!')

if adivina != numero:
    numero = str(numero)
    print('No. El número que estaba pensando era ' + numero)