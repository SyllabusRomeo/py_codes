
#while loop
counter = 1
while counter <= 10:
    print(counter)
    counter += 1

#print items in a list
beverages = ['water', 'juice', 'soda', 'tea', 'coffee']
index = 0
while index < len(beverages):
    print(beverages[index])
    index += 1
    #Break statement
    if beverages[index] == 'soda':
        print('I found soda!')
        break

#random --- Guessing game
import random

num = random.randint(1,10) #guess a random number
guess = int(input('Guess a number from 1-10: '))
chances = 2 #chance is 3, first chance used in the above input
print('2 chances remaining')

while guess != num and chances:
    if guess < num:
        guess = int(input('Your guess is less than the number, try again! '))
    else:
        guess = int(input('your guess is greater than the number, try again! '))

    print((chances - 1), 'chance(s) remaining')
    chances -=1

    if chances == 0:
        print('better luck next time')
        break

    if guess == num:
        print('You guessed correctly.')
