### Dictionaries ###

# Definición

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Alex",
                 "Apellido": "Perez", "Edad": 38, 1: "Python"}

my_dict = {
    "Nombre": "Alexander",
    "Apellido": "Perez",
    "Edad": 38,
    "Lenguajes": {"Python", "Java", "Kotlin"},
    1: 1.80
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

# Búsqueda

print(my_dict[1])
print(my_dict["Nombre"])

print("Perez" in my_dict)          # Busca por clave NO por valor¿Está Perez en my_dict? False, está Apellido
print("Apellido" in my_dict)

# Inserción

my_dict["Calle"] = "Calle Caracas"
print(my_dict)

# Actualización

my_dict["Nombre"] = "David"
print(my_dict["Nombre"])

# Elimina un solo elemento

del my_dict["Calle"]
print(my_dict)

# Otras operaciones

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Nombre", 1, "Piso"]

print("----------------------------")
my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 9, "Piso"))
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, "MoureDev")
print((my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))