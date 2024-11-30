import random
from hangman_art import stages, logo
from hangman_words import word_list

guessWord = []
def printGuessWord():
    print(" ".join(guessWord))

print(logo)
# word = random.choice(word_list)
word = "hello"
word_len = len(word)
lives = 6
indices = []
guessed_letter = (input("Guess a letter: ")).lower()

# create the Spaces
for n in range(0, word_len):
    guessWord.append('_')

#Start of a loop for the game
while lives>0:

    if guessed_letter in guessWord:
        print(f"You have already guessed {guessed_letter}")
        printGuessWord()
        print(stages[lives])
    else:
        word_index = word.find(guessed_letter)
        if word_index == -1:
            print(f"You guessed {guessed_letter}, that's not in the word. You lose a life.")
            # printGuessWord()
            # print(stages[lives-1])
            lives -= 1
        else:
            while word_index != -1:
                indices.append(word_index)
                word_index = word.find(guessed_letter, word_index+1)

            for n in indices:
                guessWord[n] = guessed_letter
                # printGuessWord()
                # print((stages[lives]))

            indices.clear()
    if '_' not in guessWord:
        printGuessWord()
        print("Great! You guessed the correct word!")
        break
    printGuessWord()
    print((stages[lives]))
    guessed_letter = (input("Guess a letter: ")).lower()

if lives<=0:
    print("You lose")
    printGuessWord()
    print(stages[0])