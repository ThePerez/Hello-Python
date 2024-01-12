### Sets Practice ####

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#   1.  Find the length of the set it_companies

print(len(it_companies))

#   2.  Add 'Twitter' to it_companies

it_companies = list(it_companies)
print(type(it_companies))
it_companies.append("Twitter")
it_companies = set(it_companies)
print(it_companies)

#   3.  Insert multiple IT companies at once to the set it_companies

it_companies = list(it_companies)
print(type(it_companies))
it_companies.append("Nvidia")
it_companies.append("Intel")
it_companies.append("Tesla")
it_companies.append("Lenovo")
it_companies = set(it_companies)
print(it_companies)

#   4.  Remove one of the companies from the set it_companies

it_companies = list(it_companies)
print(type(it_companies))
it_companies.remove("Nvidia")
it_companies = set(it_companies)
print(it_companies)

#   5.  What is the difference between remove and discard

'''
We can remove an item from a set using remove() method. 
If the item is not found remove() method will raise errors,
so it is good to check if the item exist in the given set.
However, discard() method doesn't raise any errors.
'''