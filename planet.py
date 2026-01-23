
class Planet:
  def __init__(self, mass, radius, position, color):
    self.__mass = mass
    self.__radius = radius
    self.position = position
    self.color = color
    self.velocity = (0,0)

    def set_mass(self, mass):
      self.__mass = mass
   

  def get_mass(self):
    return self.__mass