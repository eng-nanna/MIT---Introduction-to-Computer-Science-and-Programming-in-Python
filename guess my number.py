print("Please think of a number between 0 and 100!")

low = 0
high = 100
guess = (low+high)//2
ans = ""

while ans != "c":

    ans = input("Is your secret number "+str(guess)+" ? \nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if ans == "h":
        high = guess
    elif ans == "l":
        low = guess
    elif ans == "c":
        break
    else:
        print("Sorry, I did not understand your input.")
    guess = (low+high)//2

print("Game over. Your secret number was: ",str(guess))