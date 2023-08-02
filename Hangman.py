import random

words_list = ["apple", "journal", "school", "telephone", "airplane", "lion", "computer", "math", "algebra", "rocket",
              "blue", "sunlight", "star", "teacher", "language", "zebra", "aquarium", "kangaroo", "scientist",
              "motorcycle", "car", "tiger", "elephant", "soldier", "code", "lamp", "water"]

hangman = ['''
  +---+
  |   |
      |
      |
      |
	  |
=========
''', '''
  +---+
  |   |
  0   |
      |
      |
	  |
=========
''', '''
  +---+
  |   |
  0   |
 /    |
      |
	  |
=========
''', '''
  +---+
  |   |
  0   |
 /|   |
      |
	  |
=========
''', '''
  +---+
  |   |
  0   |
 /|\  |
      |
	  |
=========
''', '''
  +---+
  |   |
  0   |
 /|\  |
 /    |
	  |
=========
''', '''
  +---+
  |   |
  0   |
 /|\  |
 / \  |
	  |
=========
''']


def main():
    print(""" _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/ """)
    guess_letter = input("Guess a letter: ").lower()
    last_index = int(len(words_list) - 1)
    word = words_list[random.randint(0, last_index)]
    word_length = len(word)
    guess_word = list('_') * word_length
    chances = 0
    check_word = ""
    guessed_letters = set()
    exit_loop = False
    letter_guessed_bool = False
    while chances != 6:
        guessed_letters.add(guess_letter)
        right_or_wrong = 0
        if exit_loop:
            print("You Win!")
            break
        for index in range(0, word_length):  # traverses the string and checks each letter
            if guess_letter == word[index]:  # if letter is in word then it replaces the blank space with the guessed letter
                guess_word[index] = guess_letter
                right_or_wrong = 1
                copied_list = guess_word.copy()
                check_word = check_word + copied_list.pop(index)
                if len(check_word) == len(guess_word):
                    exit_loop = True
                    break
        if right_or_wrong == 1:
            print(''.join(guess_word))
            print(hangman[chances])
        if right_or_wrong == 0:
            chances += 1
            print(f"You guessed \'{guess_letter}\', that\'s not in the word. You lose a life.")
            print(''.join(guess_word))
            print(hangman[chances])
        if chances != 6 and exit_loop == False:
            guess_letter = input("Guess a letter: ").lower()
            if guess_letter in guessed_letters:
                letter_guessed_bool = True
            while letter_guessed_bool:
                print(f"You\'ve already guessed \'{guess_letter}\'")
                print(''.join(guess_word))
                print(hangman[chances])
                guess_letter = input("Guess a letter: ").lower()
                if guess_letter not in guessed_letters:
                    letter_guessed_bool = False
        if chances == 6:
            print("\nGame Over")
    print("Answer reveal: " + word)


main()
