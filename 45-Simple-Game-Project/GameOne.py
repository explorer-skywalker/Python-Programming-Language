"""
    Developer: Master Skywalker
    Purpose: Game Development Project with C++
    Stardate: 12021.254.00:45:32

"""
import random


print("""
            
            "ASAI's Research Lab Is Under Attack, Break The Codes To Get Into The Datacentre Facility, Cut The Hard Line & Save The Research Data From Going Into Wrong Hands..."
            

            """)


def PlayGame():
    CodeA = random.randint(1, 5)
    CodeB = random.randint(1, 5)
    CodeC = random.randint(1, 5)

    CodeSum = CodeA + CodeB + CodeC
    CodeProduct = CodeA * CodeB * CodeC

    print(">_\tHere's Some Information About The Codes...\n")
    print("+ The Total Numbers Of Code: 3")
    print("+ The Codes Join Upto:    ", CodeSum)
    print("+ The Codes Product Upto: ", CodeProduct)

    GuessA = int(input("\n\n\tEnter CodeA:\t"))
    GuessB = int(input("\tEnter CodeB:\t"))
    GuessC = int(input("\tEnter CodeC:\t"))

    GuessSum = GuessA + GuessB + GuessC
    GuessProduct = GuessA * GuessB * GuessC

    if (GuessSum == CodeSum) and (GuessProduct == CodeProduct):
        print("\n\t\t\t Welcome To The ASAI'S Datacentre Facility :)\n\n")
    else:
        print("\n\t\t Alert! There's A Breach In The Datacentre Facility :(\n\n")
        print("\tWell, The Codes Were: ", CodeA, CodeB, CodeC)
        print("\n")

while (True):
    PlayGame()
    continue
    


