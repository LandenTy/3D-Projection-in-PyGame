"""
Vertices

Description:
"""
# Import and Initalize Pygame
import pygame
import sys
import math
pygame.init()

# Create a Window
win = pygame.display.set_mode([1000, 1000])

# Variables
focalLength = 300

# Projections Variables
position = 10
size = 10

# Vertice Variables
verticeTransformX = 1
verticeTransformY = 1
verticeTransformZ = 1

# Camera Variables
cameraTransformX = 0
cameraTransformY = 10
cameraTransformZ = -10

cameraRotationY = 0

# Player Rotation Variables
xRotation = 1
zRotation = 1

def Projection(x, y, z):

    position = (x * (focalLength / z), y * (focalLength / z))
    size = abs(focalLength / z)

def Create_Vertice(x, y, z):
    
    # Setting Up Variables
    global verticeTransformX
    global verticeTransformY
    global verticeTransformZ
    
    verticeTransformX = x
    verticeTransformY = y
    verticeTransformZ = z
    
    # Drawing
    pygame.draw.circle(win, (0, 0, 0), position, size)

def RotationMatrix(x, z, direction):
    
    # Setting Up Variables
    global xRotation
    global zRotation
    
    # Rotation Matrix
    xRotation = (z * (math.sin(direction))) + (x * (math.cos(direction)))
    zRotation = (z * (math.cos(direction))) + (x * (math.sin(direction)))

def UpdateFrames():
    
    RotationMatrix((verticeTransformX - cameraTransformX), (verticeTransformZ - cameraTransformZ), (0 - cameraRotationY))
    Projection(xRotation, (verticeTransformY - cameraTransformY), zRotation)
    
while True:
    
    for ev in pygame.event.get():
        
        if ev.type == pygame.QUIT:
            
            sys.exit()
        
# Called Every Frame
UpdateFrames()
pygame.display.flip()
