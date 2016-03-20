class Body:
    # Create attributes for the class, and give them default values
    x = 0.0
    y = 0.0
    r = 0.0
    mass = 0.0
    color = (255, 255, 255)

    vx = 0.0
    vy = 0.0

    ax = 0.0
    ay = 0.0

    # Allows you to create a new Body variable with the passed-in parameters
    def __init__(self, x, y, r, mass, color):
        self.x = x
        self.y = y
        self.r = r
        self.mass = mass
        self.color = color
