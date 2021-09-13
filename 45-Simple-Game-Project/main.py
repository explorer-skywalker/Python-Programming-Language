"""
    Developer: Master Skywalker
    Purpose: Game Development Project with C++
    Stardate: 12021.254.00:45:32

"""

print("""
            
            "ASAI's Research Lab Is Under Attack, Break The Codes To Get Into The Datacentre Facility, Cut The Hard Line & Save The Research Data From Going Into Wrong Hands..."
            
            """)

def PlayGame():
    CodeA = 3
    CodeB = 6
    CodeC = 9

    CodeSum = CodeA + CodeB + CodeC
    CodeProduct = CodeA * CodeB * CodeC

    print(">_\tHere's Some Info...")
    print("+ The Numbers Of Code: 3")
    print("+ The Codes Join Upto: ", CodeSum)
    print("+ The Codes Product Upto: ", CodeProduct)

    userCode = int(input("\n\tNow, Enter The Codes: ").strip())



while (True):
    PlayGame()
    


