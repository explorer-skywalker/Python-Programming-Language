
"""
Encapsulation:
                Combining of data & functions.

"""


class Intro:
    def __init__(self, name="Human", age="Unknown") -> None:
        self.name = name
        self.age = age

    def skills(self):
        return "Skills depend on each individual's mindset..."


subject1 = Intro("Mr. Skywalker", "17")
print(f"This is {subject1.name}, {subject1.age} years old.")

subject2 = Intro(age=0)
print(f"This is {subject2.name}, {subject2.age} years old.")
print(subject2.skills())


dict
subject3 = {"name": "Captain", "lastname": "Skywalker"}
print(subject3["name"])
print(subject3["lastname"])


"""
Use OOP instead of anything to mimic the real world & for code reusability.

"""
