print("Welcome to the Guess game.\n")
print("Guess the right number which lies b/w 1 to 10.You will be given only three chances\n")
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('guess:'))
    guess_count+=1
    if guess==secret_number:
        print("you won")
        break
else:
    print("you failed")