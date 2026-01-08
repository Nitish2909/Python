import random
"""
 1 for stone
 2 for paper
 3 for sessior

"""

computer = random.choice([1,2,3])
yourChoice= input("Enter Your Choice :")
yourDict={ "stone":1 , "paper":2 , "sessior":3}
reverseDict={ 1:"stone" , 2:"paper",  3:"sessior"}
you = yourDict[yourChoice]

print(f"You Choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")
if(computer == you):
    print("DRAW")
else:
    if(computer==1 and you==2):
        print(" YOU WON!")
    elif(computer==2 and you==1):
        print(" COMPUTER WON!")
    elif(computer==1 and you==3):
        print(" COMPUTER WON!")
    elif(computer==3 and you==1):
        print(" YOU WON!")
    elif(computer==2 and you==3):
        print(" YOU WON!")
    elif(computer==3 and you==2):
        print(" COMPUTER WON!")

    else:
        print("Something Went Wrong !")

