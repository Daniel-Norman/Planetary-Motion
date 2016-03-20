import pygame
import pygame.gfxdraw as gfxdraw
from body import *
import random
import math

# Helper function to draw a circle for a given body
def draw_body(screen, body):
    gfxdraw.filled_circle(screen, int(body.x), int(body.y), body.r, body.color)


# Helper function to redraw the screen
def draw_screen(screen, body_list):
    # First we must repaint the background, and then add the bodies in the foreground
    screen.fill((0, 0, 40))
    for body in body_list:
        draw_body(screen, body)
    pygame.display.flip() # Used by pygame to refresh the screen

# Initialize the empty body_list to contain Body objects with
# attributes set correctly
def initialize_body_list(body_list):
    sun = Body(x=500, y=500, r=50, mass=3000, color=(200, 200, 0))
    sun.vx = 0
    sun.vy = 0
    sun.ax = 0
    sun.ay = 0
    body_list.append(sun)

    mercury = Body(x=600, y=500, r=10, mass=35, color=(255, 50, 50))
    mercury.vx = 0
    mercury.vy = 60
    mercury.ax = 0
    mercury.ay = 0
    body_list.append(mercury)


    earth = Body(x=700, y=500, r=15, mass=50, color=(25, 50, 255))
    earth.vx = 0
    earth.vy = 40
    earth.ax = 0
    earth.ay = 0
    body_list.append(earth)

    # Uncomment the following to have random planets in the simulation:

    #for i in range(0, 10):
    #    b = Body(random.randint(0, 1000), random.randint(0, 1000), random.randint(0, 100), random.randint(10, 1000), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    #    b.ax = random.randint(-50, 50)
    #    b.ay = random.randint(-50, 50)
    #    body_list.append(b)




# Use Newton's Law of Gravitation to calculate the force on each pair of bodies,
# and then use
#   a = sum(F)/m
# to set the acceleration for each body
def calculate_forces(body_list):

    # Clear out each body's acceleration from the previous timestep
    for body in body_list:
        body.ax = 0
        body.ay = 0

    # Look at all unique pairs of bodies
    for i in range(0, len(body_list)):
        for j in range(i + 1, len(body_list)):
            body1 = body_list[i]
            body2 = body_list[j]

            # F_G = G * m1 * m2 / r^2   where r = distance between the two

            # Use theta=math.atan2(y, x) to find the angle between the two bodies
            theta = math.atan2(body2.y - body1.y, body2.x - body1.x)


            # Use a normal distance calculation to find r^2, aka rsq
            # Hint: In python, x^2 can be achieved with x * x, or math.pow(x, 2) or x ** 2
            rsq = math.pow(body2.x - body1.x, 2) + math.pow(body2.y - body1.y, 2)

            # Cap the distance at a minimum of (20?) using rsq = max(rsq, 20);
            # This works because if rsq is less than 20, max(rsq, 20) returns 20
            rsq = max(rsq, 1)

            # Calculate the force both bodies feel
            force = 99 * body1.mass * body2.mass / rsq

            # Calculate the acceleration each body feels (remember it'll be different if they have different mass)
            abody1 = force / body1.mass
            abody2 = force / body2.mass

            # Add each body's acceleration to its body.ax and body.ay values,
            # using acceleration and theta calculated earlier
            body1.ax += math.cos(theta) * abody1
            body1.ay += math.sin(theta) * abody1
            body2.ax += math.cos(theta + math.pi) * abody2
            body2.ay += math.sin(theta + math.pi) * abody2


# Uses the body's acceleration and time elapsed since last update to change its x and y velocities
def update_velocity(body, dt):
    dvx = body.ax * dt
    body.vx = body.vx + dvx
    dvy = body.ay * dt
    body.vy = body.vy + dvy


# Uses the body's velocity and the time elapsed since last update to change its x and y positions
def update_position(body, dt):
    dx = body.vx * dt
    body.x = body.x + dx
    dy = body.vy * dt
    body.y = body.y + dy

    # Comment the following lines to stop bodies from wrapping around the screen boundaries:

    if body.x < body.r * -2:
        body.x = 1000 + body.r * 2
    if body.y < body.r * -2:
        body.y = 1000 + body.r * 2
    if body.x > 1000 + body.r * 2:
        body.x = body.r * -2
    if body.y > 1000 + body.r * 2:
        body.y = body.r * -2




# Uses Euler Method with Newton's Law of Universal Gravitation to simulate 2D planetary movement

def main():
    # Simulation initialization variables
    fps = 60
    screen = pygame.display.set_mode((1000, 1000))
    clock = pygame.time.Clock()

    # Create the list of all bodies (planets, stars, etc.)
    # It starts off as empty, then gets filled in the initialize_body_list() function
    bodies = []
    initialize_body_list(bodies)


    # While the simulation is still running
    while True:
        # Check to see if the user tried to close the window, and if so, stop the simulation
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break


        # Use physics to update accelerations of all bodies
        calculate_forces(bodies)

        # Get the time elapsed since last screen draw
        elapsed = clock.tick(fps) / 1000.0

        # Use new accelerations and time elapsed to update velocities of all bodies
        for body in bodies:
            update_velocity(body, elapsed)

        # Use new velocities and time elapsed to update positions of all bodies
        for body in bodies:
            update_position(body, elapsed)


        # Draw the screen
        draw_screen(screen, bodies)

if __name__ == "__main__":
    main()



