#hangman game
import random as rd
from hangamstage import hangman_stages as hs

word_list =['apple','beauty','potato','bhargavi']
lives = 6
chosen_word = rd.choice(word_list)
print(chosen_word)
# this show display blank or emjoy 
display =['🥹' for _ in range(len(chosen_word))]
print(' '.join(display))
while lives > 0 and '🥹' in display:
    guess_lt = input('guess a letter:').lower()
      # Check if the guessed letter is in the chosen word
    if guess_lt in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess_lt:
                display[i] = guess_lt
        print('correct guess:',guess_lt)
        
    else:
            lives=lives -1
            print('wrong guess .lives left:',lives)
            # Display the appropriate Hangman stage
            print(hs[6-lives])
    print(' '.join(display))
            
if  '🥹'  not in display:
    print('Congratulations! You guessed the word:',' '.join(display))
else:
    print('Out of lives. The word was:', chosen_word)