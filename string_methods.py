
#capitalize() method
string = "python CODING 123!"
print(string)
new_string = string.capitalize()#converts on the first character to upper case and the rest into small cases
print(new_string)

#lower() method
string = "python CODING 123!"
print(string)
new_string = string.lower() #converts the all charaters into lower case
print(new_string)

#upper() method
string = "python CODING 123!"
print(string)
new_string = string.upper()  # converts the all charaters into upper case
print(new_string)

#isdigit() method
only_digits = '12512'
print(only_digits.isdigit()) #returns true - all string characters are digits
has_digits = '12mn2'
print(has_digits.isdigit())#returns false only part of characters are numbers/digits
no_digits = 'mnop'
print(no_digits.isdigit())# returns false - has no digits

#isalpha() method
only_letters = 'abcdef'
print(only_letters.isalpha())  # returns true - all string characters are letters
has_letters = '12mn3'
print(has_letters.isalpha())# returns false only part of characters are letters
no_letters = '1245@'
print(no_letters.isalpha())  # returns false - has no letters

#isspace() method
only_spaces = '   '
print(only_spaces.isspace())  # returns true - ther are whitespaces
has_spaces = '12 3'
print(has_spaces.isspace()) # returns false only part has whitespaces
no_spaces = 'mnop'
print(no_spaces.isspace())  # returns false - has no whitespaces

#isalnum() method
only_digits = '12512'
print(only_digits.isalnum()) #True
only_letters = 'abcde'
print(only_letters.isalnum()) #True
has_digits = '1245@'
print(has_digits.isalnum()) #False
has_letters = 'mnop'
print(has_letters.isalnum()) #True
has_digits_letters = '12mn3'
print(has_digits_letters.isalnum()) #True
no_digits_letters = '@ @ @ !'
print(no_digits_letters.isalnum()) #False

#string propertis
string1 = input("Enter any character with or without spaces: ")

if string1.isspace():
    print("only white spaces")
elif string1.isalpha():
    print("Only letters")
elif string1.isdigit():
    print("Only digits")
elif string1.isalnum():
    print("Only letters and digits")
else:
    print("digits, letters, and/or symbolys")
