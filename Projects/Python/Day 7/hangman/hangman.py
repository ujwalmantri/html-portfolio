import random
import hangman_art
from hangman_words import word_list
stages = hangman_art.stages

lives = 6

print(hangman_art.logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for i in range(len(chosen_word)):
    placeholder += "_"
print(f"Word to guess: {placeholder}\n")

game_over = False
correct_guess = []

while not game_over:

    print(f"**************************** {lives}/6 LIVES LEFT ****************************\n")
    guess = input("Guess a letter: ").lower()
    print("\n")
    if guess in correct_guess:
        print(f"The letter {guess} already guessed. Enter a different letter.\n")

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_guess.append(letter)
        elif letter in correct_guess:
            display += letter
        else:
            display += "_"
    if "_" in display:
        print(f"Remaining Word to guess: {display}\n")

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word! You lose a life\n")
        if lives == 0:
            game_over = True
            print(f"*********************** IT WAS {chosen_word.upper()}! YOU LOSE**********************")
            


    if "_" not in display:
        game_over = True
        print(f"******************************* YOU WON ********************************")
        print('''
       _      _                   
      (_)    | |                  
__   ___  ___| |_ ___  _ __ _   _ 
\ \ / / |/ __| __/ _ \| '__| | | |
 \ V /| | (__| || (_) | |  | |_| |
  \_/ |_|\___|\__\___/|_|   \__, |
                             __/ |
                            |___/   
              ''')
    
    if "_" in display:
        print(stages[lives])