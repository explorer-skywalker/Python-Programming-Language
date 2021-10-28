
"""
Developer: Master Skywalker
Purpose: Object-Cosmos *
Stardate: 12021.301.13:48:00

"""


class Cosmos():
    def __init__(self, _UFO=True, _Space_Dust=False, _Meteoroid=False, _Asteroid=False, _Comet=False, _Moon=False, _Planet=False, _Rouge_Planet=False, _Star=False, _Neutron_Star=False, 
    _Magnetar=False, _Solar_System=False, _Black_Hole=False, _Galaxy=False, 
    _Electromagnetic_Force=True, _Strong_Force=True, _Weak_Force=False, _Gravitational_Force=True) -> None:
        self.ufo = _UFO
        self.sd = _Space_Dust
        self.meteo = _Meteoroid
        self.astro = _Asteroid
        self.comet = _Comet
        self.moon = _Moon
        self.planet = _Planet
        self.rp = _Rouge_Planet
        self.star = _Star
        self.nstar = _Neutron_Star
        self.magnetar = _Magnetar
        self.ss = _Solar_System
        self.bh = _Black_Hole
        self.galaxy = _Galaxy

        self.electromagnetism = _Electromagnetic_Force
        self.gravity = _Gravitational_Force
        self.strong = _Strong_Force
        self.weak = _Weak_Force

        super().__init__()



x_ufo = Cosmos()
print(x_ufo.ufo)
print(x_ufo.astro)
    
print(x_ufo.weak)
x_ufo.weak = True
print(x_ufo.weak)

  