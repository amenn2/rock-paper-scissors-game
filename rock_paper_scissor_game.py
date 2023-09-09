from random import*

def playround():
    user_score=0
    computer_score=0
    while (user_score!=5) and (computer_score!=5):
        user=input("enter ur choice: ")
        choices=["rock","paper","scissors"]
        computer=choice(choices)
        if user==computer:
            print('tie...')
        elif (user=="rock" and computer=="scissors") or (user=="scissors" and computer=="paper") or (user=="paper" and computer=="rock"):
            user_score+=1
            print("you win the round!")
        else:
            computer_score+=1
            print("computer win the round!")
    return(user_score)

x=playround()
if x==5:
    print("you win the game!")
else:
    print("computer win the game!")



