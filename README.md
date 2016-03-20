# Planetary-Motion
Simple 2D planetary motion simulator created initially as a Python tutorial.

This program is heavily commented to provide a detailed explainiation of the purpose of each line of code.
This particular simulator uses the Euler method of approximating solutions to the ODEs for the motion of the planetary bodies.

The force each body feels is calculated at each timestep using Newton's law of universal gravitation, which is then used to determine acceleartion. Then, using Euler's method, we are able to approximate velocity and position in a manner that appears realistic.
