### Exercises: Level 1###
# 1.Declare an empty list

new_list = []

# 2.Declare a list with more than 5 items

random_list = ["Alex", "Perez", "Engineer", "Argentina", 38, "Buenos Aires", "Audi"]

# 3.Find the length of your list

print(len(random_list))
print("--------------------")

# 4.Get the first item, the middle item and the last item of the list

print(random_list[0])
print(random_list[3])
print(random_list[6])
print("--------------------")

# 5.Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_types = ["Bob Marley", 37, 180, "married", "9 miles"]

# 6.Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7.Print the list using print()

print(it_companies)
print("--------------------")

# 8.Print the number of companies in the list

print(len(it_companies))
print("--------------------")

# 9.Print the first, middle and last company

print(it_companies[0])
print(it_companies[3])
print(it_companies[6])
print("--------------------")

# 10.Print the list after modifying one of the companies

it_companies[6] = "Ebay"
print(it_companies) 
print("--------------------")

# 11.Add an IT company to it_companies

it_companies.append("Intel")
print(it_companies)
print("--------------------")

# 12.Insert an IT company in the middle of the companies list

it_companies.insert(4, "SuperCell")
print(it_companies)
print("--------------------")

# 13.Change one of the it_companies names to uppercase (IBM excluded!)

print(it_companies[4].upper())
print("--------------------")

# 14.Join the it_companies with a string '#;  '

company = ['Lenovo']
mix_companies = company + it_companies
print(mix_companies)
print("--------------------")

# 15.Check if a certain company exists in the it_companies list.

print(mix_companies.count("IBM"))
print("--------------------")

# 16.Sort the list using sort() method

mix_companies.sort()
print(mix_companies)
print("--------------------")

# 17.Reverse the list in descending order using reverse() method

mix_companies.reverse()
print(mix_companies)
print("--------------------")

# 18.Slice out the first 3 companies from the list



# 19.Slice out the last 3 companies from the list

# 20.Slice out the middle IT company or companies from the list