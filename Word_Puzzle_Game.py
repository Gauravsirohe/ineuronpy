#Words included in list
words = ["FATHER","DAUGHTER","MOBILE","ORANGE","PROGRAMMER","GREEN","AEROPLANE"]

#Welcome to user to play the game
name = input("May I Know Your Name, Please: ")
user = print(f"Hello {name}, Welcome to Word Puzzle Game!")

#import random module to choose randam words from the list
import random
#function for choosing random word.
def random_word():
    random_word = random.choice(words)
    return random_word

# Function for shuffling the
def combin_shuffling_word(random_word):
    #shuffling the character
    shuffling = random.sample(random_word, len(random_word))
    #Join the characters by join() methof after shuffling
    combin_shuffling_word = ''.join(shuffling)
    return combin_shuffling_word

#defin trun and score to count the attmpt and score
trun = 5
score = 0

#looping - to allow to answer 5 words in a round
while trun > 0:
    get_word = random_word()
    set_word = combin_shuffling_word(get_word)
    print("Arrange the letters to form a valid word:",set_word)
    guess = input("What is in your mind? ")
    if guess.capitalize() == get_word.capitalize():
        print("Great! You anwared correctly")
        score = score +1
    else:
        print("Bad Luck!, You answared incorrectly")
        score = score -1
    print("")
    trun = trun -1
    
print("Net Score is",score)









        

















