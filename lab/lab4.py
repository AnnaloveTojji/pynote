# July 17
# nested 'if' 

#nested 'if'
var = 100
if var < 200:
   print ("Expression value is less than 200")
   if var == 150:
      print ("Which is 150")
   elif var == 100:
      print ("Which is 100")
   elif var == 50:
      print ("Which is 50")
   elif var < 50:
      print ("Expression value is less than 50")
else:
   print ("Could not find true expression")

print ("Good bye!")

# pseudo code exercise
# if
# rock, paper, scissors - level1
player1 = 'r'  # assign 'rock'
player2 = 's'  # assign 'scissors'
if player1 == player2:
   print("It's a tie!")
elif player1 == 'r' and player2 == "s":
   print("Player1 win!")
elif player1 == 'p' and player2 == "r":
   print("Player1 win!")


# rock, paper, scissors - level2
import random
user_action = input("Enter a choice (rock, paper, scissors): ")

possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)

print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")

# loop
# even or odd number
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("Even")
else:
   print("Odd")
