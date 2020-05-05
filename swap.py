'''
#LONG SWAP
x=10
y="ten"
#step 1
temp = x #temp is now 10
#step 2
x = y #x is now "ten"
#step 3
y=temp #y is now 10
print(x,y,temp)

#SIMPLE SWAP
x=10
y="ten"
x,y = y,x
print(x,y)

#another  swap example
you = "apple"
friend = "money"
you,friend = friend,you
print(you, friend)
'''
#program to swap values from a user input
acpt = float(input("Enter first number "))
acpt2 = float(input("Enter second number "))

#condition to reaccept user input if values are the same
if acpt2 == acpt:
    print("Your second number must be different from the first")
    acpt2 = float(input("Enter different number "))

#performing the swap
acpt, acpt2 = acpt2, acpt
print("Your swapped values are")
print(acpt, acpt2)
