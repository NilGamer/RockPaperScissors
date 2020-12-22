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

signs = [rock , paper , scissors]

userInput = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

cmpGuess = random.randint(0,2)

print(signs[userInput])
print(f"Computer chose: \n {signs[cmpGuess]}")

if(userInput == cmpGuess):
  print("Draw")
elif(userInput == 0 and cmpGuess == 1):
  print("You Lose")
elif(userInput == 1 and cmpGuess == 2):
  print("You Lose")
elif(userInput == 2 and cmpGuess == 0):
  print("You Lose")
elif userInput > 2:
  print("Invalid Input, You Lose")
else:
  print("You Won")
