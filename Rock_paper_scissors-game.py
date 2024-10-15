import random

user_wins=0
comp_wins=0

choices=["rock" ,"paper", "scissors"]
while True:
    user_input=input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input=="q":
        break
    
    if user_input not in choices:
        print("type correctly")
        continue
    
    random_number=random.randint(0,2)
    comp_pick=choices[random_number]
    print("comp pick",comp_pick + ".")
    
    if user_input =="rock" and comp_pick=="scissors":
        print("You Won!")
        user_wins+=1
        continue
    
    elif user_input =="paper" and comp_pick=="rock":
        print("You Won!")
        user_wins+=1
        continue
    
    elif user_input =="scissors" and comp_pick=="paper":
        print("You Won!")
        user_wins+=1
        continue
    
    else:
        print("You Lost!")
        comp_wins+=1
        
print("You won", user_wins, "times.")
print("The computer won", comp_wins, "times.")
