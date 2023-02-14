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

a = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
print("You chose : ")
if a == 0:
  print(rock)
elif a == 1:
  print(paper)
else:
  print(scissors)

print("Computer chose:")
b = random.randint(0,2)
if b == 0:
  print(rock)
elif b == 1:
  print(paper)
else:
  print(scissors)

if a == 0 and b == 2:
  print("You WIN!")
elif a == 1 and b == 0:
  print("You WIN!")
elif a == 2 and b == 1:
  print("You WIN!")
elif a == b:
  print("It's a DRAW!")
else:
  print("You LOSE!")