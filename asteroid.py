import pygame
import random

from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            LINE_WIDTH,
        )

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        # Destroy the current asteroid
        self.kill()

        # Small asteroids disappear without splitting
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Log the splitting event
        log_event("asteroid_split")

        # Generate a random angle between 20 and 50 degrees
        angle = random.uniform(20, 50)

        # Calculate new movement directions
        velocity1 = self.velocity.rotate(angle)
        velocity2 = self.velocity.rotate(-angle)

        # Calculate the new asteroid radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create two smaller asteroids at the current position
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        # Give both asteroids faster movement
        asteroid1.velocity = velocity1 * 1.2
        asteroid2.velocity = velocity2 * 1.2
