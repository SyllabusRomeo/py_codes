lst1 = [1, 2, 3, 'Hello', 'World'] #original list
lst2 = lst1                        #assignment operator
lst3 = lst1[:]                     #slice copy
lst4 = lst1.copy()                 # copy() method

lst1[0] = 5
lst2[1] = 10
lst3[2] = 15
lst4[3] = 20

print('lst1: ', lst1)
print('lst2: ', lst2)
print('lst3: ', lst3)
print('lst4: ', lst4)


#is operator
alst = [1, 2, 3]
blst = ['a', 'b', 1]
print(alst[0] is blst[2]) # Returns true; value of the array position is the same value in the second array position
#meaning alst[0] is 1 and blst[2] also has one, so 1 is 1 means True

cblst = [1, 2, 3]
num1 = 2
print(cblst[1] is num1) #Returns True

#Nested list
nested_list = [[2, 4, 6], ['A', 'B', 'C'], [6.5, 4.2, 10.0]]

print(nested_list[0])  # returns [2, 4, 6]
print(nested_list[1])  # retunrs ['A', 'B', 'C']
print(nested_list[2])  # returns [6.5, 4.2, 10.0]
print(len(nested_list)) # returnd length of array as 3
#print the elements within the nested array
print(nested_list[0][0])  # returns 2
print(nested_list[1][1])  # retunrs B
print(nested_list[2][2])  # returns 10.0
