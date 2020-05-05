nested_list = [[2,4,12], ['A', 'B', 'C'], [6.5, 4.2, 10.0]]
nested_list2 = nested_list[:]
nested_list3 = nested_list.copy()

#substituting values
nested_list[0][0]= 20
nested_list2[1][1] = 'D'
nested_list3[2][2] = 40.0
#printing the variables
print(nested_list)
print(nested_list2)
print(nested_list3)

print(nested_list2 is nested_list)
print(nested_list3 is nested_list)

print('\nChecking the first nested_list: [2,4,12]')
print(nested_list2[0] is nested_list[0])
print(nested_list3[0] is nested_list[0])

print('\nChecking the second nested_list: ["A", "B", "C"]')
print(nested_list2[1] is nested_list[1])
print(nested_list3[1] is nested_list[1])

print('\nChecking the first nested_list: [6.5, 4.2, 10.0]')
print(nested_list2[2] is nested_list[2])
print(nested_list3[2] is nested_list[2])
