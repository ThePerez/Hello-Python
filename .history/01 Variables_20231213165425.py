#Variables

my_variable = "My String Variable"
print(my_variable)

my_int_variable = 1985
print(my_int_variable)

my_bool = True
print(my_bool)

print (my_variable, my_int_variable, my_bool)

#Concatenación de variables en un print
mix_variable = str(my_int_variable)
print(mix_variable)
print(type(mix_variable))

#Funciones del sistema 
print(len(my_variable)) #Cuenta los caracteres
print("Este es el valor de:",my_int_variable )

#Variables en una sola linea
name, surname, alias, age = "Alex","Perez","El Negro","38"
print("Mi edad es:", age, " y mi apellido y nombre es:", surname, name, "y me dicen:", alias)

#Hace preguntas
first_name = input("¿Cuál es tu nombre? : ")
edad = input("¿Cuál es tu edad? ")

print(first_name)
print(edad)