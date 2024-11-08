import random
def get_computer_choice():
    return random.choice(['rock','paper','scissors'])
def determine_winner(user_choice,computer_choice):
    if user_choice==computer_choice:
        return 'tie'
    elif(user_choice=='rock' and computer_choice=='scissors')or(user_choice=='scissors' and computer_choice=='paper')or(user_choice=='paper' and computer_choice=='rock'):
        return 'user'
    else:
        return 'computer'
def play_game():
    user_score=0
    computer_score=0
    print("welcome to ROCK_PAPER_SCISSORS!")
    print("Instructiond:choose 'rock','paper',or 'scissors'.Type 'exit' to end the game.")
    while True:
        user_choice=input("Enter your choice:").lower()
        if user_choice=='exit':
            break
        if user_choice not in['rock','paper','scissors']:
            print("Invalid choice,please try again.")
            continue
        computer_choice=get_computer_choice()
        print(f"Computer chose:{computer_choice}")
        winner=determine_winner(user_choice,computer_choice)
        if winner=='user':
            print("you win!")
            user_score+=1
        elif winner=='computer':
            print("you lose!")
            computer_score+=1
        else:
            print("It 's tie!")
            print(f"score-you:{user_score},computer:{computer_score}")
            play_again=input("Do you want to play again?(yes/no):").lower()
        if play_again!='yes':
            break
    print("Thanks for playing!")
if __name__=="__main__":
    play_game()

