def game():
    player1 = input("Player 1 Enter Rock, Paper, or Scissor: ").lower()
    player2 = input("Player 2 Enter Rock, Paper, or Scissor: ").lower()
    while player1 == "rock":
        if player2 == "paper":
            print("Player 2 you win!")
            break
        elif player2 == "scissor":
            print("Player 1 you win!")
            break
        else:
            print("It's a tie!!")
            break
    while player1 == "paper":
        if player2 == "rock":
            print("Player 1 you win!")
            break
        elif player2 == "scissor":
            print("Player 2 you win!")
            break
        else:
            print("It's a tie!!")
            break
    while player1 == "scissor":
        if player2 == "paper":
            print("Player 1 you win!")
            break
        elif player2 == "rock":
            print("Player 2 you win!")
            break
        else:
            print("It's a tie!!")
            break
    print("Do you want to play again?")
    answer2 = input("Type 'Yes' or 'No': ").lower()
    if answer2 == "yes":
        game()
    else:
        print("Goodbye")
        quit()
        
print("Are you ready?")
answer1 = input("Type 'Yes' or 'No': ").lower()
if answer1 == "yes":
    game()
else:
    print("Goodbye")
    quit()
    


        