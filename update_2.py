import random


class IrrationalLimitError(Exception):
    def __init__(self,lower,higher):
        self.lower = lower
        self.higher = higher
    def __str__(self):
        return("Lower number{0} is higher than the upper number{1} please try again !".format(self.lower,self.higher))
class tooMuchInputError(Exception):
    def __init__(self,guessList=[]):
        self.guessList = guessList
    def __str__(self):
        return ("Number of passed input parameter is greaeter than needed, you"
                "have passed {} input please pass 2 input ".format(len(self.guessList)))

while(True):
    try:
        guessWhat = input("please enter min and max integers... ").split()
        try:
            limit_lower = int(guessWhat[0])
            limit_upper = int(guessWhat[1])
            if len(guessWhat)>2:
                raise tooMuchInputError(guessWhat)
            break
        except TypeError:
            print("Type Error")
        if limit_lower>=limit_upper:
            raise IrrationalLimitError(limit_lower,limit_upper)
    except ValueError:
        print("Value error occured")
hiddenNumber = random.randint(limit_lower, limit_upper)

while(True):
    guess = int(input("Guess What number it is ?"))
    if guess == hiddenNumber:
        print("Hit!")
        break
    elif guess < hiddenNumber:
        print("Your guess is too low")
    else:
        print("Your guess is too high")
