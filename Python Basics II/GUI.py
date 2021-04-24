
# Graphical User Interface ;
    # Exercise;
    # Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
image = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

    # Iterate over
for row in image:
    for box in row:
        # conditions
        if (box == 0):
            print(" ", end = "")     # because, default == \n
        else:
            print("*", end = "")
    # Out the image
    print("")


print("\n")


for row in image:
    for box in row:
        if (box == 0):
            print("*", end = "")     
        else:
            print(" ", end = "")
    print("")


print("\n")


for row in image:
    for box in row:
        if (box == 0):
            print(" ", end = "")    
        else:
            print("*", end = "")
    print("")




# What is a good code? ;
    # clean
    







