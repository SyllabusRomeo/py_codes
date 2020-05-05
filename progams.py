'''
Write a program that asks the user to enter today in Celcius. Depending on the conditions, the program
will have different responses. If the temperature is below 15, then the program will print "It is cold."
If the temperature is above 15 but below 20, the program will print "It is warm." For any other temperature
the program will print "It is hot".
'''
#here is the code
temp = float(input("Enter temperature number: "))

if temp < 15:
    print("It is cold")
elif 15 < temp < 20:
    print("It is warm")
else:
    print("It is hot")
#-------------------------------------------------------------------------------------------------------
#boolean
is_water = input("Is water available (True or False)?")

if is_water =="True":
    is_water = True
else:
    is_water = False

if is_water == True:
    print("I will purchase this drink")
'''
#simplified version of the above
if is_water == True:
    print("I will purchase this drink")
'''
#A program to allow 1 or 0 input to display results
num = int(input("Please enter an integer value: "))

if num > 0:
    if num < 20:
        print("The number is a positive number and less than 20")
    else:
        print("The number is positive")
    print("The number is positive")
else:
    print("The number is not positive")

#simplified version using AND operator
if num > 0 and num < 20:
    print("The number is a positive number and less than 20")
elif num > 0:
    print("The number is positive")
else:
    print("The number is not positive")

#using OR operator
fever = True
cough = False
fatigue = False

if (fever or cough or fatigue):
    print("I will see a doctor")

#using NOT operator
password = input("Enter password: ")

if password != "8734":
    print("Sorry, that is the wrong password")

#simplified NOT
if not password == "8753":
    print("Sorry, that is the wrong password")
