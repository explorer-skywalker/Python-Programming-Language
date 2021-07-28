
"""
Abstraction:
            >_ Extraction of data, as we wanted & hide all other stuff.

"""


class Universe():
    def __init__(self, forces="""Electromagnetism", "Gravity", "Strong & Weak Nuclear Forces""", laws="Laws Of Physics") -> None:
        self.forces = forces
        self.laws = laws


    def life(self):
        return self.forces + " And " + self.laws


earth = Universe()
print("Fundamental Forces: \n", earth.forces)
print(f"Laws of Earth means: \n {earth.laws}")

earth.laws = "made by the peoples who forms the government ;)"
print("Today's citizen Rules are", earth.laws)


human = Universe("Unknown", "Nonsence")
print(f"Human forces are {human.forces} & human laws are {human.laws}")




"""
Private vs Public Variables:
                            >_ There is no such functions as private but, the python community decided that ( _ ) started variables should be private & not modified.

"""

class Dark():
    def __init__(self, matter="Dark Matter", energy="Dark Energy") -> None:
        self._matter = matter
        self._energy = energy


research = Dark()
print(research._matter)
print(research._energy)
print(f"This research topic about {research._matter} and {research._energy} are still under R&D...")

