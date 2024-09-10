import pygame
import random
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
	
	def draw(self, screen):
		pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width=2)
	
	def update(self, dt):
		self.position += self.velocity * dt
	
	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		rand_angle = random.uniform(20, 50)
		asteroid1_vel = self.velocity.rotate(rand_angle)
		asteroid2_vel = self.velocity.rotate(-rand_angle)
		asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
		asteroid1 = Asteroid(self.position.x, self.position.y, asteroid_radius)
		asteroid2 = Asteroid(self.position.x, self.position.y, asteroid_radius)
		asteroid1.velocity = asteroid1_vel * 1.2
		asteroid2.velocity = asteroid2_vel * 1.2
		return asteroid1, asteroid2