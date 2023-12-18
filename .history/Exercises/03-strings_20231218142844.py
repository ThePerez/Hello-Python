## 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

one = "Thirty "
two = "Days "
three = 'Of '
four = 'Python'

conca = one + two + three + four
print(conca)

## 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
print('-------------------')
conca_two = 'Coding' + ' ' + 'For' + ' ' + 'All'
print(conca_two)

## 3. Declare a variable named company and assign it to an initial value "Coding For All".

company = conca_two

## 4. Print the variable company using print().
print('-------------------')
print(company)

## 5. Print the length of the company string using len() method and print().
print('-------------------')
print(len(company))


## 6. Change all the characters to uppercase letters using upper() method.
print('-------------------')
print(company.upper())

## 7. Change all the characters to lowercase letters using lower() method.
print('-------------------')
print(company.lower())

## 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print('-------------------')
print(company.capitalize())
print(company.title())
print(company.swapcase())

## 9. Cut(slice) out the first word of Coding For All string.
print('-------------------')
slice_practice = company[0:4]
print(slice_practice)

## 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
print('-------------------')
company = "Coding" in company
print("Does the straing contain Coding? :", company)

## 11. Replace the word coding in the string 'Coding For All' to Python.
print('-------------------')
company = "Coding For All"
print(company.replace('Coding','Python'))

## 12. Change 'Python for Everyone' to 'Python for All' using the replace method or other methods.
print('-------------------')
print(company.replace('Coding For All','Python For Everyone'))

## 13. Split the string 'Coding For All' using space as the separator (split()) .
print('-------------------')
company = 'Coding For All'
split_exercise = company.split()
print(split_exercise)

## 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
print('--------------------')
companies = 


## 15. What is the character at index 0 in the string Coding For All.
## 16. What is the last index of the string Coding For All.
## 17. What character is at index 10 in "Coding For All" string.
## 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
## 19. Create an acronym or an abbreviation for the name 'Coding For All'.
## 20. Use index to determine the position of the first occurrence of C in Coding For All.