### Loops ###

# While

my_app = 0

while my_app < 10:
    print(my_app)
    my_app += 2
else:
    print("Mi condición es mayor o igual a 10")   

## 2 ##

while my_app < 20:
    my_app += 1
    if my_app == 15:
        print("Se detiene la ejecución")
        break
    print(my_app)
    
    
    ######### for loop ########
    
    my_list = [10, 32, 38, 12, 20, 99, 1010]
    
    for element in my_list:
        print(element)
    break

my_other_dict = {"Nombre": "Alex","Apellido": "Perez", "Edad": 38, 1: "Python"}
for element in my_other_dict:
        print(element)

my_set = {"Python", "JavaScript", "CSS"}
for element in my_set:
        print(element)
    
my_tuple = (38, 1.80, "Alex", "Perez", "Audi")
for element in my_tuple:
        print(element)
    