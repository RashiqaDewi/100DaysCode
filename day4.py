
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random
isi = int(input("What do you choose? type 0 for rock, 1 for paper, 2 for scissors :"))
game = [rock,paper,scissors]
user = game[isi]
print("user's choice")
print(user)
print("computer's choice")
computer = random.choice(game)
print(computer)
if user == rock and computer == paper :
    print("You lose.")
elif user == rock and computer == scissors :
    print("You win!")
elif user == paper and computer==scissors :
    print("You lose.")
elif user == scissors and computer == paper:
    print("You win")
elif user == paper and computer == rock :
    print("You win")
elif user == scissors and computer == rock :
    print("You lose")
elif user == computer :
    print("You're tie.")
else :
    print("invalid number, you should only input a number between 0,1,2")

