import random

secret_code = random.randint(1,100)

print("You are Playing a Perfact Number Guessing Game")
print("Your are Guessing Number between 1 to 100")


attempts=0

while True:

    guess = int(input("Enter Your Guess.... :"))
    attempts=attempts+1

    if(guess<secret_code):
        print("Your guess is Too low ! Try again")
    elif(guess>secret_code):
        print("Your guess is Too Highhh! Try again")
    else:
        print(f"congratulation. You guess the right number in {attempts} attempts")
        break