from words import cs_words
import random 

def choose_word():
    selected_word = random.choice(cs_words)
    return selected_word.upper()

def play(word):
    blank_spaces = " _ " * len(word)
    guessed  = False
    guessed_letters = []
    guessed_words = []
    tries = 6 
    print("||  Welcome To CS Hanggman! ||")
    print("|| Computer Science Hangman ||")
    print(display_hangman(tries))
    print(blank_spaces)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if  guess in guessed_letters:
                print(f"'{guess}' has already been guessed. ")
            elif guess not in word:
                print(f"'{guess}' is not in the selected word. ")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f" Correct, '{guess}' is in the selected word")
                guessed_letters.append(guess)
                word_list = list(blank_spaces)
                indices = [ i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_list[index] = guess
                blank_spaces = "".join(word_list)
                if " _ " not in blank_spaces:
                    guessed = True
                    
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"'{guess}' has already been guessed. ")
            elif guess != word:
                print (guess, "is not the word")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                blank_spaces = word
                print("correct guess: ", word)

        else:
            print("Not a valid guess.")
            print(display_hangman(tries))
            print(blank_spaces)
            print("\n")

    if guessed:
        print("Congrats, you won")
    else: 
        print(f"Sorry, you lost. The correct word was '{word}' ")












def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    word = choose_word()
    play(word)
    while input("Play Again? Y/N ").upper() == "Y":
        word = choose_word()
        play(word)

    if __name__ == "__main__":
        main()