import random

print("=====Rock, Paper, Scissor Game=====")
choices = [ "rock" , "paper" , "scissor"]

while True:
    print("choose one : Rock ,Paper ,Scissor")
    user_choice = input("My Choice : ").lower()
    if user_choice not in choices:
        print("choose a valid choice")
        continue
    bot_choice = random.choice(choices)
    print("Bot chose : " , bot_choice)

    if user_choice == bot_choice :
        print("Tie !!!")
    elif (user_choice == "rock" and bot_choice == "scissor") or \
        (user_choice == "scissor" and bot_choice == "paper") or \
        (user_choice == "paper" and bot_choice == "rock"):

        print("Congratulation ! ,You win this round ")
    else :
        print("Unfortunately , Bot wins this round")
    
    one_more = input("Want to play one more round ? (yes / no) :")
    if one_more.lower() != "yes":
        print("Bye bye , Thanks for Playing")
        break

