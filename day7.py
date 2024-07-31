stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

                                                                    
                                                                    
# hangman picture yet to be displayed
import random
print(logo)
word_list = ["jisung","haechan"]
chosen_word = random.choice(word_list)
kata_user = ["_"]*len(chosen_word)
max_taken = len(chosen_word)
attemps_taken = 0
while "_" in kata_user and attemps_taken < max_taken: 
     print("Guess the letter :")
     guess = str(input())
     if guess in chosen_word :
         for idx in range(0,len(chosen_word)) :
              if chosen_word[idx] == guess:
                kata_user[idx] = guess #ini perlu diindex
                kata_user2 = " ".join(kata_user)
                print(f"You guessed the letter: {guess}\n{kata_user2}")
                
                
     else : 
        attemps_taken += 1
        kata_user3 = " ".join(kata_user)
        print(f"You guess {guess}, it's the wrong letter, input again\n{kata_user3}")

if "_" not in kata_user:
    print(f"Congratulations! You guessed the word: {''.join(kata_user)}")
else:
    print(f"Sorry, you did not guess the word. It was: {chosen_word}")  
        
# print(f"you guess {kata_user2}, meanhwile the word is '{chosen_word}'")