import pygame
class Bodies:
  #distance from sun in meters from earth earth
  ASTRONIMCAL_UNITS = (149.6e6*1000)

  #gravitational constant
  G = 6.6743e-11 #(m/kg)^2
  SCALE = 250/ASTRONIMCAL_UNITS #1AU = 100 pixels
  TIMESTEP = 3600*24 # 1 day

  def __init__(self, mass, radius, position, color):
    self.__mass = mass #in kg
    self.radius = radius 
    self.position = position # vector (x, y, z) in meters
    self.color = color
    self.velocity = (0,0,0) # vector (vx, vy, vz) in m/s

    
    self.sun = False
    self.distance_to_sun = 0
    self.orbit = []

  def draw(self, win, winWidth, winHeight):
      x, y = self.position
      x = x * self.SCALE + winWidth/2
      y = y * self.SCALE + winHeight/2
      pygame.draw.circle(win, self.color, (x, y), self.radius)
      

  def set_mass(self, mass):
    self.__mass = mass
  

  def get_mass(self):
      return self.__mass

  def set_position(self, mass):
    self.__mass = mass
  

  def get_position(self):
      return self.__mass
  
  