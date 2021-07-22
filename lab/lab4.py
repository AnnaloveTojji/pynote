# conditional execution - exercises
# nested 'if' 

# rock, paper, scissors - level 1
print("*** rock, paper, scissors w/o user input ***")
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
print("*** rock, paper, scissors w/ user input ***")
user_action = input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions) #computer will make a random choice
if user_action == computer_action: #case1
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock": 
    if computer_action == "scissors": #case2
        print("Rock smashes scissors! You win!")
    else: #case3
        print("Paper covers rock! You lose.")
elif user_action == "paper":
    if computer_action == "rock": #case4
        print("Paper covers rock! You win!")
    else: #case5
        print("Scissors cuts paper! You lose.")
elif user_action == "scissors":
    if computer_action == "paper": #case6
        print("Scissors cuts paper! You win!")
    else: #case7
        print("Rock smashes scissors! You lose.")

