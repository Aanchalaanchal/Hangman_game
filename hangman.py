import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("you are playing hangman")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("guess a letter or a word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("already guessed. guess again")
            elif guess not in word:
                print("you have guessed wrong. ", guess, " is not in my word")
                guessed_letters.append(guess)
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("you have guessed right. ", guess, " is in my word.")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("already guessed. guess again")
            elif guess != word:
                print("you guessed wrong. guess again")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("no. this is not a guess. i'm asking you to guess again. guess")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("you got this word right. this has been a good wasting of your time. now go back and justify the amount of oxygen that you breathe to the trees tirelessly producing it")
    else:
        print("you are out of tries. you have wasted your time and unnecessarily increased your carbon footprint. and you did not even win this silly game. my word was " + word)

def display_hangman(tries):
    stages = [   """
                    _________
                    |   |
                    |  \O/
                    |   |
                    |  / \
                 """,
                 """
                    _________
                    |   |
                    |  \O/
                    |   |
                    |  / 
                 """,
                 """
                    _________
                    |   |
                    |  \O/
                    |   |
                    |  
                 """,
                 """
                    _________
                    |   |
                    |  \O
                    |   |
                    |  
                 """,
                """
                    _________
                    |   |
                    |   O
                    |   |
                    |  
                 """,
                 """
                    _________
                    |   |
                    |   O
                    |   
                    |  
                 """,
                 """
                    _________
                    |   |
                    |   
                    |   
                    |  
                 """,

    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("play again to waste more time? type y/n").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()
