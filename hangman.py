# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
from operator import truediv
import random
import string
from webbrowser import get
from zoneinfo import available_timezones

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for char in secret_word:
      if char in letters_guessed:
        continue
      else:
        return False
    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_word = []
    msg = ""
    for char in secret_word:
      if char in letters_guessed:
        guessed_word.append(char)
      else:
        nch = "_ "
        guessed_word.append(nch)

    final_guess = "".join(guessed_word)
    return final_guess



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    available_letters = string.ascii_lowercase
    available_letters_lst = list(available_letters)
    for char in letters_guessed:
      if char in available_letters:
        available_letters_lst.remove(char)

    remain_letters = "".join(available_letters_lst)

    return remain_letters

    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guess_count = 6
    user_warning = 3
    letters_guessed = []
    vowels = ['a', 'e', 'i' , 'o', 'u']

    print("\nWelcome to the game Hangman!\n")
    print("I am thinking of a word that is", len(secret_word) , "letters long.\n")
    print("You have", user_warning, "warnings left\n")
    
    

    while guess_count>0:
      print("-------------")
      print("You have", guess_count, "guesses left\n")
      print("Available Letters:", get_available_letters(letters_guessed),"\n")
      user_guess = input("Please guess a letter:").lower()

      if user_guess.isalpha():
        if user_guess in letters_guessed:
          print("the letter has already been guessed before..You have", user_warning, "warnings left.\n")
          if user_guess in letters_guessed and user_guess not in secret_word:
            user_warning-=1
            if user_warning <=0:
              guess_count-=1
        elif user_guess not in letters_guessed and user_guess not in secret_word and user_guess in vowels:
          letters_guessed.append(user_guess)
          print(get_guessed_word(secret_word, letters_guessed),"\n")
          guess_count-=2
        elif user_guess in secret_word:
          letters_guessed.append(user_guess)
          print("Good guess:",get_guessed_word(secret_word, letters_guessed),"\n")
        else:
          letters_guessed.append(user_guess)
          print("Oops! That letter is not in my word.\n",get_guessed_word(secret_word, letters_guessed),"\n")
          guess_count-=1
      else:
        user_warning-=1
        if user_warning <=0:
          guess_count-=1
        print("Oops! That is not a valid letter.You have", user_warning, "warnings left. \n")

      if is_word_guessed(secret_word,letters_guessed):
        total_score = guess_count * len(set(secret_word))
        print("Good Job, You won")
        print("Your total score is", total_score)
        break

    if guess_count == 0 and is_word_guessed(secret_word,letters_guessed) == False:
      print("You have run out of guesses.\n", "The secret word is ",secret_word)
    
    






# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    unstrip_word = my_word.replace(" ", "")
    i = 0
    if len(unstrip_word) != len(other_word):
      return False
    else:
      while i < len(unstrip_word):
        if unstrip_word[i] == "_":
          if other_word[i] in unstrip_word:
            return False
        else:
          if unstrip_word[i] != other_word[i]:
            return False
        i+=1
    return True




def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    matchings = []

    for word in wordlist:
      if match_with_gaps(my_word, word):
        matchings.append(word)
    
    if len(matchings)>0:
      for word in matchings:
        print(word)
    else:
      print("No matches found")




def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guess_count = 6
    user_warning = 3
    letters_guessed = []
    vowels = ['a', 'e', 'i' , 'o', 'u']

    print("\nWelcome to the game Hangman!\n")
    print("I am thinking of a word that is", len(secret_word) , "letters long.\n")
    print("You have", user_warning, "warnings left\n")
    
    

    while guess_count>0:
      print("-------------")
      print("You have", guess_count, "guesses left\n")
      print("Available Letters:", get_available_letters(letters_guessed),"\n")
      user_guess = input("Please guess a letter:").lower()

      if user_guess.isalpha():
        if user_guess in letters_guessed:
          print("the letter has already been guessed before..You have", user_warning, "warnings left.\n")
          if user_guess in letters_guessed and user_guess not in secret_word:
            user_warning-=1
            if user_warning <=0:
              guess_count-=1
        elif user_guess not in letters_guessed and user_guess not in secret_word and user_guess in vowels:
          letters_guessed.append(user_guess)
          print(get_guessed_word(secret_word, letters_guessed),"\n")
          guess_count-=2
        elif user_guess in secret_word:
          letters_guessed.append(user_guess)
          print("Good guess:",get_guessed_word(secret_word, letters_guessed),"\n")
        else:
          letters_guessed.append(user_guess)
          print("Oops! That letter is not in my word.\n",get_guessed_word(secret_word, letters_guessed),"\n")
          guess_count-=1
      elif user_guess == "*":
        print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
      else:
        user_warning-=1
        if user_warning <=0:
          guess_count-=1
        print("Oops! That is not a valid letter.You have", user_warning, "warnings left. \n")

      if is_word_guessed(secret_word,letters_guessed):
        total_score = guess_count * len(set(secret_word))
        print("Good Job, You won")
        print("Your total score is", total_score)
        break

    if guess_count == 0 and is_word_guessed(secret_word,letters_guessed) == False:
      print("You have run out of guesses.\n", "The secret word is ",secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #secret_word = "nehal"
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
