import pygame, math, sys
from pygame.locals import *


# Set the screen
screen = pygame.display.set_mode((800*3/2, 600*3/2))
# Initialize the clock
clock = pygame.time.Clock()

class car:
     MAX_FORWARD_SPEED = 3
     MAX_REVERSE_SPEED = 3

     def __init__(self, car_filename, X, Y, angle):
          #pygame.sprite.Sprite.__init__(self)

          # Load the car image
          self.car = pygame.image.load(car_filename).convert()
          # Speed is between 0-3
          self.speed = 0
          # Direction: 0 = right, 1 = down, 2 = left, 3 = up
          self.direction = 2
          # Keep track of rectangle's position
          self.xpos = X
          self.ypos = Y
          self.angle = angle
          # Initialize the car by blitting it
          self.display_car()


     # EFFECTS: Function to display the car image
     def display_car(self):
          self.xpos = self.xpos - self.speed*math.cos(math.radians(self.angle))
          self.ypos = self.ypos + self.speed*math.sin(math.radians(self.angle))
          screen.fill((0, 0, 0))
          screen.blit(pygame.transform.rotate(self.car, self.angle), (self.xpos, self.ypos))
          pygame.display.flip()

     # Makes car turn left
     def left(self):
          self.angle+=1
          #self.direction = (self.direction + 3) % 4
          # for i in range(91):
          #    clock.tick(45)
          #rotated_car = pygame.transform.rotate(self.car, self.angle)
          self.display_car()
        
     # Makes car turn right
     def right(self):
          self.angle-=1
          #self.direction = (self.direction + 1) % 4
          # for i in range(91):
          #    clock.tick(45)
          #rotated_car = pygame.transform.rotate(self.car, self.angle)
          self.display_car()

     def accelerate(self):
          self.speed += 1
          # for i in range(90):
          #    clock.tick(30)

          # self.speed = 0

     def decelerate(self):
          self.speed -= 1
          # for i in range(100):
          #    clock.tick(30)
          

          # self.speed = 0
def animateCar():
     rect = screen.get_rect()
     myCar = car("car.png", rect.centerx, rect.centery, 180)

     done = False 

     while(1):
          # Event handlers
          keys = pygame.key.get_pressed()
          clock.tick(30)
          if keys[K_ESCAPE]:
                pygame.quit()
                sys.exit()
          elif keys[K_RIGHT]:
                myCar.right()
          elif keys[K_LEFT]:
                myCar.left()
          elif keys[K_UP]:
                myCar.accelerate()
          elif keys[K_DOWN]:
                myCar.decelerate()

          myCar.display_car()
          pygame.event.pump()
          

          # Game logic

          # Clear the screen before drawing
     
          # Display what is drawn:
          # pygame.display.flip()
          
          # 
     
def main():
     abort_criteria = True

     # while abort_criteria:
     #    user_typing = input("Type 1 to escape or 2 to animate car: \n")
     #    if user_typing is "1":
     #         print ("Exiting now")
     #         abort_criteria = False
     #    else:
     #         animateCar()
     animateCar()
main()
          
