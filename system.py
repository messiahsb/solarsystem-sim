class SolarSystem:
    def __init__(self, width, height):
        self.solar_system = turtle.Screen()
        self.solar_system.tracer(0)
        self.solar_system.setup(width, height)
        self.solar_system.bgcolor("black")

        self.bodies = []
        
    def add_body(self, body):
        self.bodies.append(body)
        
    def remove_body(self, body):
        self.bodies.remove(body)