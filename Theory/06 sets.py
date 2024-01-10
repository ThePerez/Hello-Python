### Sets ###

# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, 
#     the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.


my_set = set()
my_o_set = {}

print(type(my_set))
print(type(my_o_set)) #Inicialmente es un diccionario

my_set = {"Python", "JavaScript", "CSS"}

my_o_set = {"Alex", "Perez", "Developer", 38}
print(type(my_o_set))

my_n_set = my_set.union(my_o_set)           #Concatena los sets. No acepta repetidos
print(my_n_set)

print(my_n_set.difference(my_set))          #Diferencia my_n_ser menos my_set

