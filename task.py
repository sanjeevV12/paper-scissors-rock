import random
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
game_choice =[rock, paper, scissors]

choose=int(input("what do you choose? Type 0 for Rock ,1 for Paper ,2 for Scissors\n "))
#0,1,
if choose >=0 and  choose<=2:
    print(game_choice[choose])
computer_choice =random.randint(0,2)
print("computer choose")
print(game_choice[computer_choice])
if choose >= 3 or choose < 0:
    print("please choose again, you type invalid number!")
elif choose == 0 and computer_choice == 2:
    print("you win")
elif choose == 2 and computer_choice == 0:
    print("you lose")
elif choose ==computer_choice:
    print("it's a draw")
elif computer_choice > choose:
    print("you lose")
elif choose > computer_choice:
    print("you win")
