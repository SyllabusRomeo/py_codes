#pop method
grocery_list = ['Milk', 'Gari', 'Orange', 'Sugar', 'Groundnut']
print(grocery_list.pop()) # Returns Groundnut
print(grocery_list)  # Returns ['Milk', 'Gari', 'Orange', 'Sugar']
print(grocery_list.pop(3))  # returns Sugar
print(grocery_list)  # Returns ['Milk', 'Gari', 'Orange']

#remove method
shopping_list = ['Milk', 'Gari', 'Orange', 'Sugar', 'Groundnut']
print(shopping_list.remove('Milk'))  # Returns none. Remove method does not return any value
print(shopping_list) # Returns ['Gari', 'Orange', 'Sugar', 'Groundnut'] => 'Milk' has been removed

#index() method
my_list = [1, 'Hello', 2, 3, 'Hello','World']
print(my_list.index('Hello')) #prints the position of an item in the array. index(value)

#insert() method
ur_list = [1, 'Hello', 2, 3, 'World']
ur_list.insert(0,4) #insert 4 to the first array position
print(ur_list) # Returns [4, 1, 'Hello', 2, 3, 'World']
ur_list.insert(3,'language') #insert language to the 3 array position
print(ur_list)  # Returns [4, 1, 'Hello', 'language', 2, 3, 'World']

#clear() method
ur_list.clear() # Clears everything in the array list
print(ur_list)  # Returns []

#count() method
slist = [1, 1, 'Hello', 2, 3, 'Hello', 'World']
print(slist.count('Hello')) # Returns 2: counting the number of value occurrence in the array
print(slist.count('Helo')) # Returns 0

#reverse() method
alist = [1, 1, 'Hello', 2, 3, 'Hello', 'World']
alist.reverse()
print(alist)  # prints in reverse ['World', 'Hello', 3, 2, 'Hello', 1, 1]

#sort() method
blist = [1, 1, 9, 2, 3, 0.5, 0.2]
blist.sort()
print(blist) #sorts in alphabetical order




