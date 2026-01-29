import math
import pygame
class Bodies:
  #distance from sun in meters from earth earth
  ASTRONIMCAL_UNITS = (149.6e6*1000)

  #gravitational constant
  G = 6.6743e-11 #(m/kg)^2
  SCALE = 250/ASTRONIMCAL_UNITS #1AU = 250 pixels
  TIMESTEP = 3600*24 # 1 day

  def __init__(self, mass, radius, position, color):
    self.mass = mass #in kg
    self.radius = radius 
    self.position = position # vector (x, y, z) in meters
    self.color = color
    self.velocity = [0,0,0] # vector (vx, vy, vz) in m/s

    
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
  
  def calc_position():
      return -1
  
  def calc_acceleration():
      return -1

  def calc_velocity():
      return -1
  
  def calc_fattraction(self, body2):
        #F = Gm1m2/r.sqr
        p2_x, p2_y = body2.position
        p1_x, p1_y = self.position
        distanceX = p2_x - p1_x
        distanceY = p2_y - p1_y
        distance = math.sqrt(distanceX**2 + distanceY**2)
        if body2.sun:
           self.distance_to_sun = distance
        #force of attraction
        force = (self.G * self.mass * body2.mass)/distance**2
        # Direction of the force 
        theta = math.atan2(distanceY, distanceX)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y
    
    #rethink this code, maybe it can go in 
    #system.py since it loops through a list of planets
  def update_position(self, planets):
    total_fx, total_fy = 0, 0

    for planet in planets:
        if self == planet:
            continue
        force_x, force_y = self.calc_fattraction(planet)
        total_fx += force_x
        total_fy += force_y
    #f=ma = a=f/m && a = vf-vi/t -- v=d/t  vf = vi + at 
    # -- vf = vi + f/m * t
    self.velocity[0] += total_fx / self.mass * self.TIMESTEP
    self.velocity[1] += total_fy / self.mass * self.TIMESTEP

    #s = dt
    self.position[0] += self.velocity[0] * self.TIMESTEP
    self.position[1] += self.velocity[1] * self.TIMESTEP

    self.orbit.append(self.position)
  
        
