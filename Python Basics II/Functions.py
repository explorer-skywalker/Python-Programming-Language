
# Functions;
# - We're not limited to the python's pre-build functions, We can create our own functions using ( def ).
# - Code Reusability - Making code reusable, clean & easy to modify.

def say_hello():
    print("Hello my crtetor :)")


say_hello()

# Implementing Reusability;
image = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]


def show_image():
    fill = "*"
    empty = " "
    for row in image:
        for box in row:
            if (box):
                print(fill, end="")
            else:
                print(empty, end="")
        print("")


show_image()
show_image()
show_image()


# Parameters & Arguments;

# Parameters;
def say(first_name, last_name):
    print(f"Hello my crtetor :) {first_name} {last_name}")


    # Positional Arguments;
say("Captain", "Skywalker")
say("Captain", "Murlidhar Singh")


# Default Parameters & Keyword Arguments;

# Default Parameters;
def users(username="user", password="root"):    # It sets the default arguments for parameters
    print(f"{username} - {password}")


print("\nDatabase-1\n")
users()
users("Root", "tooR")

# Keyword Arguments;
# It's not a good idea, Use the standard
users(username="user1", password="/home")


# Return;
