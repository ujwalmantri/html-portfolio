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

error = '''
 ,adPPYba, 8b,dPPYba, 8b,dPPYba,  ,adPPYba,  8b,dPPYba,  
a8P_____88 88P'   "Y8 88P'   "Y8 a8"     "8a 88P'   "Y8  
8PP""""""" 88         88         8b       d8 88          
"8b,   ,aa 88         88         "8a,   ,a8" 88          
 `"Ybbd8"' 88         88          `"YbbdP"'  88   
'''

your_choice = int(input("Type 0 for rock, 1 for paper, 2 for scissors.\n"))
if your_choice == 0:
    print(rock)
elif your_choice == 1:
    print(paper)
elif your_choice == 2:
    print(scissors)
else:
    print(error)

computer_choice = random.randint(0,2)
if your_choice == 0 or your_choice == 1 or your_choice == 2:
    if computer_choice == 0:
        print(rock)
    elif computer_choice == 1:
        print(paper)
    else:
        print(scissors)

if your_choice == 0 and computer_choice ==2:
    print("You Won! Congratulations!")
elif your_choice == 2 and computer_choice ==0:
    print("You Lost! Better Luck Next Time")
elif your_choice == computer_choice:
    print("It's a tie")
elif your_choice > computer_choice and (your_choice == 0 or your_choice == 1 or your_choice == 2):
    print("You Won! Congratulations!")
else:
    print("You Lost! Better Luck Next Time")