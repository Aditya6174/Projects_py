import random
#We need to guess the number equal to the computer's number 
def guess(x) :
    my_rand = random.randint(1,x)
    #initialising a temporary variable for storing inputs
    guess = 0
    while(guess != my_rand) :
        guess = int(input(f'Guess a number between 1 and {x} :'))
        if(guess > my_rand) :
            print("Guess again , too high")
        elif guess < my_rand :
            print ("Guess again , too low !")


    print(f"Yay right ans {my_rand}")
# We let the computer guess our number 
def computerGuess(x) :
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' :
        if(low != high) :
            guess = random.randint(low,high)
        else :
            guess = low
        feedback = input(f'Is {guess} , too high(H) , too low(L) , is correct(C) ?? ').lower()
        if feedback == 'h' :
            high = guess - 1
        elif feedback == 'l' :
            low = guess + 1

    print(f'yay rightly guessed {guess}')

guess(100)
computerGuess(100)
