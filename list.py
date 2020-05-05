#printing empty list array with in-built list method list()
lst1 = list()
print(lst1)  # returs []

lst2 = []
print(lst2)  # returns []
print(len(lst2))

#append() method: Adding items to a list
grocery_list = []
grocery_list.append("Milk")
grocery_list.append("eggs")
grocery_list.append("bread")
grocery_list.append("rice")
grocery_list.append(20.00)
print("Grocery list = ", grocery_list)  # output is ['Milk', 'eggs', 'bread', 'rice']
print(len(grocery_list)) # output is 4

#indexing + slicing with list
grocery_list = ['Milk', 'eggs', 'bread', 'rice', 20.00]
print(grocery_list[0])
print(grocery_list[:3])
print(grocery_list[-1])
print(grocery_list[4])

#replacing array index
market_list = ['Orange', 'Pawpaw', 'Mango', 'Pear']
market_list[0] = 'eggs'
print(market_list)
