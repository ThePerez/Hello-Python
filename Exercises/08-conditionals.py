##### Conditionals Exercises #####

#Level 1

# 1. Get user input using input (“Enter your age: ”). If user is 18 or older, give feedback: 
#    You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. 

# Obtener la entrada del usuario
age = int(input("Enter your age: "))

# Comprobar la edad del usuario
if age >= 18:
    print("You are old enough to drive.")
else:
    years_to_wait = 18 - age
    print(f"Sorry, you need to wait {years_to_wait} more year(s) before you can drive.")


# 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? 
#    Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. 

my_age = 38
your_age = int(input("Enter your age: "))

if (your_age > my_age):
    dif_age = your_age - my_age
    if dif_age == 1:
        print("Eres mayor que yo por 1 Año") 
    else:     
        print('Eres mayor que yo por', dif_age, 'años')
elif (my_age > your_age):
    dif_age = my_age - your_age
    if dif_age == 1:
        print("Soy mayor que tú por 1 Año") 
    else:     
        print('Soy mayor que tú por', dif_age, 'años')
    
else: 
    print('Tenemos la misma edad')


# 3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b,
#    if a is less b return a is smaller than b, else a is equal to b. 

a = int(input('Enter number one: '))
b = int(input('Enter number two: '))

if a == b:
    print ('Número 1 y 2 son iguales')
elif a > b:
    print ('Número 1 es mayor al número 2')
else:
    print('Número 2 es mayor al número 1')

### Exercises: Level 2
# Write a code which gives grade to students according to theirs scores:

# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F

# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

# The following list contains some fruits:

# fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
