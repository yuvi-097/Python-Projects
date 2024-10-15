name=input("Type your Name: ")
print("Welcome",name,"to this Adventure!")

answer=input("your are on a dirt road and you can go left or right .Which way u wanna go?").lower()
if answer=="left":
    if answer=="swim":
        print("you swam across and were eaten by a Anaconda")
    elif answer=="walk":
        print("you walked for miles ,ran out of water and you lost the game")
    else:
        print("Not a valid option")
    answer=input("you come to a river .you can walk around it or swim across. Type walk to walk around and swim to swim across:").lower()
elif answer=="right":
        print("You walked for miles and reached a castle.")
        answer=input("You can either go inside or climb the wall. Type 'go' to go inside and 'climb' to climb the wall: ").lower()
        if answer=="go":
            print("You found the treasure!")
        elif answer=="climb":
            print("You fell and broke your leg. Game over.")
        else:
            print("Not a valid option")

