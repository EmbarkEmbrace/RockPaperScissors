import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____) *bam*
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)_______________
          _________________)
          __________________) *woosh*
         _________________)
---.__________________)
'''

scissors = '''
    _______
---'   ____)__________________
          ____________________) 
       _______________________)  *snip*
      (____)
---.__(___)
'''

#Write your code below this line 👇\
game_imgae = [rock, paper, scissors]

user_call = int(input('Would you like to choose "0" for Rock, "1" for Paper, or "2" for Scissors?\n'))

if user_call >=3 or user_call < 0:
  print("you've typed an invalid number; therefore, you lose.")
else:
  print(game_imgae[user_call])
  
  computer_call = random.randint(0, 2)
  print("Computer chose:")
  print(game_imgae[computer_call])
  
  if user_call == 0 and computer_call == 2:
    print("You win!")
  elif user_call == 2 and computer_call == 0:
    print("You lose!")
  elif computer_call > user_call:
    print("You lose!")
  elif user_call > computer_call:
    print("You Win!")
  elif user_call == user_call:
    print("it's a draw!\n")