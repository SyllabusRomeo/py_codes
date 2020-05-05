
#for Loop
'''
range(start, stop, steps = 1) -> rule --- 1
'''
for i in range(0,10,1): #indicating start, stop & steps
    print(i) #returns 0 1 2 3 4 5 6 7 8 9. 10 is not included because it is the stop range

#simplified version
for i in range(10):
    print(i)

#adding slice to range
for i in range(10)[:5]: #iterates only up to the 5th value
    print(i) #returns 0 1 2 3 4

#using the len operator
print(len(range(10))) #returns 10 because the values in range are from 0-9

'''
range indices is int value from 0 to len(collection)-1 -> rule --- 2
'''

#example
beverages = ['water', 'juice', 'soda', 'tea', 'coffee']
for i in range(len(beverages)):
    print(beverages[i]) #returns the values in the array

#example2 -> print every 2 numbers
for i in range(0,10, 2):
    print(i) #returns 0, 2, 4, 6, 8

#example3
for i in range(5, 0, -1):
    print(i)  # returns 5, 4, 3, 2, 1


#example4 -> print the entire loop twice
beverage = ['water', 'juice', 'soda', 'tea', 'coffee']
for i in range(-len(beverage),len(beverage)):
    print(beverage[i])
    # returns 'water', 'juice', 'soda', 'tea', 'coffee','water', 'juice', 'soda', 'tea', 'coffee'
'''
explanation
['water', 'juice', 'soda', 'tea', 'coffee']
     0       1       2       3       4
    -5      -4      -3      -2      -1
'''
#print formatting
string = 'Alphabet'
for char in string:
    print(char, end='')  #returns Alphabet
    #print(char, end=',') #returns A,l,p,h,a,b,e,t

#example5 -> printing list with spaces
lst_beverage = ['water', 'juice', 'soda', 'tea', 'coffee']
for drink in lst_beverage:
    print(drink, end=' ')

#example6
#adding items to a list array
int_lst = []
for i in range(10):
    int_lst.append(i)
print(int_lst)  # returns [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#example7
#attempt to duplicate element in the list
ins_lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in ins_lst:
    num *=2
print(ins_lst)  # returns [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#example8
inst_lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(inst_lst)):
    inst_lst[i] *=2
print(inst_lst)  # returns [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
'''
#infinite loop
val_list = [1, 2, 3, 4, 5]
for i in val_list:
    val_list.append(i)
'''
#'in & not in' operator with for loop
q_beverages = ['water', 'juice', 'soda', 'tea', 'coffee']

if 'soda' in q_beverages:
    print('I will purchase soda.')
else:
    print('Soda is not available.')

if 'smoothie' not in q_beverages:
    print('Smoothie is not available')
else:
    print('I will purchase soda.')

#for loop to print shapes
for i in range(5):
    print('*'*4)