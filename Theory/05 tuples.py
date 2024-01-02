### Tuples ###

'''
son colecciones de datos idénticos o distintos 
clasificados con un índice y que no pueden ser
modificados. Se crean de la misma manera que las 
listas 
'''


my_tuple = tuple()
my_o_tuple = (8900, 5471, "California")

my_tuple = (38, 1.80, "Alex", "Perez", "Audi")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[3])
# print(my_tuple[-3]) IndexError
# print(my_tuple[-6]) IndexError

print(my_tuple.count(38))
print(my_tuple.index("Alex")) #Posición donde se encuentra

# my_tuple[2] = 2.0 'tuple' object does not support item assignment

mix_tuples = my_tuple + my_o_tuple    # Las tuplas se pueden sumar
print(mix_tuples)

print(mix_tuples[2:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[3] = "Alexander"
my_tuple.insert(3, "Hawaii")
print(tuple(my_tuple))

del my_tuple
# print(my_tuple) NameError: name 'my_tuple' is not defined. Did you mean: 'my_o_tuple'?