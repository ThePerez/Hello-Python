## Practice Tuples ##

# 1.Create an empty tuple

first_tuple = tuple()
print("---------------------")

# 2.Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

brothers = ("Anelxander", "Damaso", "Marcos", "Miguel")
sisters = ("Marianela", "Jenny", "Isadora")

# 3.Join brothers and sisters tuples and assign it to siblings

siblings = (brothers + sisters)
print(siblings)
print("---------------------")

# 4.How many siblings do you have?

print(len(siblings))
print("---------------------")

# 5.Modify the siblings tuple and add the name of your father and mother and assign it to family_members

siblings = list(siblings)
print(type(siblings))
siblings.append("Dad") # Add 'Father'
siblings.append("Mom")
print(siblings)
siblings = tuple()
print(type(siblings))