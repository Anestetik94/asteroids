import pygame
import sys
from asteroidfield import AsteroidField
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
   
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()  # Create a Clock object
    dt = 0  # Delta time in seconds
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (updatable, drawable, shots)  # Add Shot to the groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()  # Create an instance of AsteroidField
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  # Create a player instance
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
        updatable.update(dt)
       
        for shot in shots:
            for asteroid in asteroids:
                if asteroid.collisions(shot):
                    shot.kill()
                    asteroid.split()


        for obj in asteroids:
            collisions = obj.collisions(player)
            if collisions:
                sys.exit("Game over!")

        screen.fill((0, 0, 0))

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000  # Limit to 60 FPS and get delta time in seconds


if __name__ == "__main__":
    main()
