import random
def rock_paper_scissors():
 user_move=input("ener your choice:(Rock,Paper,Scissors):")
 Actions_possible=["Rock","Paper","Scissors"]
 computer_move=random.choice(Actions_possible)
 print(f"\nYou choose:{user_move} and computer choose:{computer_move}\n")
 if(user_move==computer_move):
    print(f"\nBoth you and computer choose same move:{user_move}\nIts a tie!!!")
 elif(user_move=="Rock"):
    if(computer_move=="Scissors"):
        print("You win!")
    else:
        print("You lose!")
 elif(user_move=="Paper"):
    if(computer_move=="Rock"):
        print("You win!")
    else:
        print("You lose!")
 elif(user_move=="Scissors"):
    if(computer_move=="Paper"):
        print("You win!")
    else:
        print("You lose!")
 else:
    print("Invalid choice!")
 play_again = input("Do you want to play again? (yes/no): ").lower()
 if play_again == "yes":
    rock_paper_scissors()
 else:
    exit
if __name__ == "__main__":
    rock_paper_scissors()

