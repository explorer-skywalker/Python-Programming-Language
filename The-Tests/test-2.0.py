
"""
Developer: Mr. Skywalker
Purpose: Testing an Idea
Stardate: 12021.242.01:21:00
"""

class Human():
    def __init__(self, mindset="\nScientist\n", nature="Creator\n" , work="Explorer\n", thinking="Dreamer\n"):
        self.mindset = mindset
        self.nature = nature
        self.work = work
        self.thinking = thinking


    def Intro(self):
        return "Hello, I'm Captain Skywalker. I'm a Scientist & my nature is Research, Explore and Develop.. I'm the founder & C.E.O of ASAI Inc. (Automation Systems with Artificial Intelligence)... My ultimate aim is to develop a Galactic Human Empire....\n "


    def Logic(self):
        return "At the ultimate level, Everything Is Nothing because, this very universe itself doesn't have any purpose, It just is...\n"


    def Ultimate_Aim(self):
        return "If Everything Is Nothing then, You have to do the greatest thing that you ever could & Which is developing a Galactic Human Empire for good, advancement and to improve the quality of life...\n"


    def Perfect(self):
        return "There is nothing like perfect, It just the matter of the perseption of reality, Just be and build something better than ever that, You can proud of...\n"


skywalker = Human()
print(skywalker.mindset)
print(skywalker.nature)
print(skywalker.work)
print(skywalker.thinking)

print(skywalker.Intro())
print(skywalker.Logic())
print(skywalker.Perfect())
print(skywalker.Ultimate_Aim())
