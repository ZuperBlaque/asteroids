# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    
    # Create sprite groups for all updatable and drawable objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)    # Set the containers for the Player class
    Asteroid.containers = (asteroids, updatable, drawable)  # Set the containers for the Asteroid class
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots)
    asteroid_field = AsteroidField() # Create an instance of AsteroidField

    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")  # Fill the screen with black
        updatable.update(dt)      # Update the player each frame

        for asteroid in asteroids: 
            if player.collide(asteroid):    # Check for collision
                pygame.quit()   # Quit the game
                sys.exit("Game over!") # Exit the program
                return
            
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()   # Refresh the screen
        dt = clock.tick(60) / 1000  # Amount of seconds between each loop
        

if __name__ == "__main__":
    main()
