from random import choice

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points = 5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0,0).
        self.x_values =[0]
        self.y_values =[0]

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length
        while len(self.x_values)<self.num_points:

            # Decide which direction to go and how far to go in that direction
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_steps = x_direction*x_distance

            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_steps = y_direction*y_distance

            #Reject moves that go nowhere
            if x_steps == 0 and y_steps == 0:
                continue

            # Calculate the new position
            x = self.x_values[-1] + x_steps
            y = self.y_values[-1] + y_steps

            self.x_values.append(x)
            self.y_values.append(y)

