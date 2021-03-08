import random

while(True):
    try:
        guessWhat = input("please enter limit integers... ").split()
        limit_lower = int(guessWhat[0])
        limit_upper = int(guessWhat[1])
        hiddenNumber = random.randint(limit_lower, limit_upper)


    except ValueError: # found in generation of randint
        print("Value error")

while(True):
    guess = int(input("Guess What ?"))
    if guess == hiddenNumber:
        print("Hit!")
        break
    elif guess < hiddenNumber:
        print("Your guess is too low")
    else:
        print("Your guess is too high")

