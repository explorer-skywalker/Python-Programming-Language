"""

>_  Inheritance, Using functionalities of other objects or inherit therir properties.

"""


class Scientist():
    def sign_in(self):
        return "\n\t Welcome, Signed-In Successfully...\n"

    # You don't need to use __init__ function first if, you don't want any variables...


# Here, we inherited the functionality of Scientist in a Creator...
class Creator(Scientist):
    def __init__(self, name, research_area):
        self.name = name
        self.research_area = research_area

    def intro(self):
        print(f"\tIt's {self.name},\n \tResearch Area - {self.research_area}")


user2 = Creator("Mr. Skywalker", "Spacefaring Civilisation")
print(user2.intro())


class Explorer(Scientist):
    pass


user1 = Explorer()
print(user1.sign_in())


class Destructor():
    pass
