### Strings

my_string = "Alexander"
mi_string = 'Perez'

print(len(my_string))
print(len(mi_string))

new_string = "String con\nsalto de linea"
print(new_string)

tab_string = "\tString con tabulacion"
print(tab_string)

#formateo

name, surname, age = "Alex", "Perez", 38

print('Me llamo {} {} y tengo {} a#os'.format(name,surname,age))
print('Me llamo %s %s y tengo %d a#os'%(name,surname,age))
print(f'Me llamo {name} {surname} y tengo {age} a#os') #
