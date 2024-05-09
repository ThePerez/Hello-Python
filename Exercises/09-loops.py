# 1. Iterate 0 to 10 using for loop, do the same using while loop.

loop1 = 0 
while loop1 < 11:
   print(loop1)
   loop1 += 1    
print('---------------------------------------')

# 2. Iterate 10 to 0 using for loop, do the same using while loop.

loop2 = 10 
while loop2 >= 0:
    print(loop2)
    loop2 -= 1  
print('---------------------------------------')

# 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:

loop3 = 0
while loop3 < 8:
    loop3 += 1 
    print(loop3 * "#")
print('---------------------------------------')
    
  
# 4. Use nested loops to create the following:

loop4 = 0
while loop4 < 7:
    loop4 += 1 
    print("# # # # # # # #")     
print('---------------------------------------')

# 5. Print the following pattern:

loop5 = 0
while loop5 < 11:
  print(loop5, "x", loop5, "= ", loop5*loop5)
  loop5 += 1
print('---------------------------------------')

# 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

lista = ['Python', 'Numpy','Pandas','Django', 'Flask']

        # Iterar a través de la lista e imprimir cada elemento
        
for elemento in lista:
    print(elemento)


Use for loop to iterate from 0 to 100 and print only even numbers

Use for loop to iterate from 0 to 100 and print only odd numbers
'''''''''''