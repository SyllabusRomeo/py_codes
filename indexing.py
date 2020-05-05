
#print array positions
string = "Hello World"
first_char = string[0]
print(first_char)

#simplified version; (-1) prints the last character in a string
string2 = "Alphabet"
last_char = string2[-1]
print(last_char)

#lenght of string minus 1
string3 = "Apples"
last_char2 = string3[len(string3)-1]
print(last_char2)

#method indexing
char1 = "Biscuits"
las_char = char1[4]
print(las_char.isalpha()) #this should return True
print(las_char.isdigit()) #this should return False, last character is not a number/digit

#print a part of an array
pArray = "Alphanumeric"
sArray = pArray[3:]
print(sArray)  # prints hanumeric

pArray = "Alphanumeric"
sArray = pArray[:3]
print(sArray)  # prints Alp
