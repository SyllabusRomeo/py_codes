'''
# concatenation
stri = 'Hello'
stri += 'World'
print(stri)

#printing memory address location
string1 = 'Hello'
print(id(string1))
string1 += 'World'
print(id(string1))

#list concatenation & mutation
lst = [1, 2, 'a', 'b']
lst += ['hello', 5]
print(lst)

#extend() method
lstA = [1, 2, 'a', 'b']
lstA.extend(['hello', 5, 6])
print(lstA)
'''
#array list checking + and +=
lst0 = [1, 2, 3]
lst1 = [1, 2, 3]
lst2 = [1, 2, 3]
lst3 = [1, 2, 3]

print('\nConcatenating: +')
print(id(lst1))
lst1 = lst1 + lst0
print(id(lst1))

print('\nMutating: +=')
print(id(lst2))
lst2 += lst2
print(id(lst2))

print('\nMutating: extend')
print(id(lst3))
lst3.extend(lst3)
print(id(lst3))

print('\nChecking the Values in the list:\n')
print(lst1)
print(lst2)
print(lst3)

#Multiplication
lst4 = [1, 2, 3]
lst4 = lst4 *3
print(lst4)

lst5 = [1, 2, 3]
lst5 *= 3
print(lst5)
