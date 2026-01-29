import bodies
YELLOW = (255,255, 0)
BLACK = (0,0,0)
BLUE  = (0,0, 255)
class SolarSystem:
    sun = bodies.Bodies((1.989* 10**30), 30, [0,0], YELLOW)
    sun.sun = True
    #r = 695700
    earth = bodies.Bodies((5.9722* 10**24), 10, [-1*bodies.Bodies.ASTRONIMCAL_UNITS,0], BLUE)
    earth.velocity[1] = 29.783 * 1000
    # r = 6371

    START_TIME = 0
    TIME = START_TIME
  
    END_TIME = 3600*24 * 365 * 10

    def __init__(self):
        self.planets = [self.sun, self.earth]
        
    def add_body(self, body):
        self.planets.append(body)

    def remove_body(self, body):
        self.planets.remove(body)
    
    def update_all(self):
        for body in self.bodies:
            body.move()
            body.draw()
        self.solar_system.update()

        