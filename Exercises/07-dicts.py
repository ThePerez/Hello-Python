## Exercises Dictionary ##

# 1. Create an empty dictionary called dog

dog = dict()
print(type(dog))

# 2. Add name, color, breed, legs, age to the dog dictionary

dog = {"name" : "Spike", "color":"Brown", "breed":"Chow Chow", "legs":4, "age":5}
print(dog)

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary

student = {"first_name":"Alex", "last_name":"Perez", "gender":"Male", "age":"38", "marital status":"married",
           "skills":"programmer", "country":"Argentina", "city":"Buenos Aires", "address":"CABA"}
print(student)


# 4. Get the length of the student dictionary

print(len(student))

# 5. Get the value of skills and check the data type, it should be a list

print(student["skills"])

# 6. Modify the skills values by adding one or two skills

student["skills"] = {"Developer", "QA Automation"}
print(student)

# 7. Get the dictionary keys as a list
print("-------------------------------")
print(student.keys())

# 8. Get the dictionary values as a list

print("-------------------------------")
print(student.values())

# 9. Change the dictionary to a list of tuples using items() method

print("----------TUPLE---------------------")
print(tuple(student))

# 10. Delete one of the items in the dictionary

del student["address"]
print(student)

# 11. Delete one of the dictionaries

del dog
print(dog)