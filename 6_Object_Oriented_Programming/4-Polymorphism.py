"""
# Polymorphism ;
            >_ Fourth & last pillar of OOP.
            >_ Poly (Many) - Morphism (Forms), Many Forms..

"""

class User():
    def __init__(self, name) -> None:
        self.name = name
    

    def intro(self):
        return (f"\tThis is {self.name}")


class Scientist(User):
    def welcome(self):
        return (f"\n\t Hello {self.name}, Welcome to the mindset of Scientists where, we are developing Spacefaring Civilisation...\n") 


user1 = Scientist("Murlidhar")
# print(user1.name)
print(user1.intro())
print(user1.welcome())


user2 = Scientist("Shree")
# print(user2.intro())
print(user2.welcome())


