cups_lemon_juice = float(input('Enter amount of juice (in cups): \n '))
cups_water = float(input('Enter amount of water (in cups): \n'))
cups_nectar = float(input('Enter amount of agave nectar (in cups): \n '))

servings = float(input('How many servings does this make? \n'))


print('Lemonade ingredients - yields ', servings, 'servings')
print(cups_lemon_juice, 'cup(s) lemon juice')
print(cups_water, 'cup(s) water')
print(cups_nectar, 'cup(s) agave nectar')

number_servings = float(input('How many servings would you like to make?'))
cups_lemon_juice = cups_lemon_juice/servings * number_servings
cups_water = cups_water/servings * number_servings
cups_nectar = cups_nectar/servings * number_servings
servings = number_servings
print('\n')
print('Lemonade ingredients - yields ', servings, 'servings')
print(cups_lemon_juice, 'cup(s) lemon juice')
print(cups_water, 'cup(s) water')
print(cups_nectar, 'cup(s) agave nectar')

print('\n')
print('Lemonade ingredients - yields ', servings, 'servings')
print(cups_lemon_juice/16, 'gallon(s) lemon juice')
print(cups_waterr/16, 'gallon(s) water')
print(cups_nectar/16, 'gallon(s) agave nectar')
























