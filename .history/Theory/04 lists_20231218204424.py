### lists ###

#las listas se pueden definir de estas dos maneras
my_list = list()
my_o_list = []

print(len(my_list))

my_list = [10, 32, 38, 12, 20, 99, 1010]
print(my_list)
print(len(my_list))

my_o_list = [38, 1.80, "Alex", "Perez"]
print(type(my_o_list))

print(my_list[1]) #muestra elementos de la lista
print(my_o_list[3])
print(my_o_list.count("Alex")) #retorna el valor que se repite de la lista

age, height, name, surname = my_o_list
print(age)

print(my_list + my_o_list) # Se suman las listas

my_o_list.append("Apple") #Adiciona al final un elemento
print(my_o_list)

my_o_list.insert(2,"Green") #inserta un elemento en la posicion indicada
print(my_o_list)

my_o_list.remove("Green") #Elimina el elemento seleccionado
print(my_o_list)

my_list.pop()     #Elimina el último elemento y lo guarda
print(my_list)
print(my_list.pop(2)) #elimina el elemento que quiero

my_list.reverse() #Se listan los elementos comenzando desde el último
print(my_list)

my_pop_element = my_list.pop(6)
print()

