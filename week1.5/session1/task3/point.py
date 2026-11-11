# Week 1.5, Session 1: Task 3

class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
    def __init__(self, x_coordinate, y_coordinate):
        """
        Creates a Point, given x & y coordinates.
        """
        self.x = x_coordinate
        self.y = y_coordinate
    # Add distance() method here
    def distance(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    # Add distance_to() method here
    # (This will need a parameter representing another point)
    def distance_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


# Finally, add code here to demonstrate use of Point
p1 = Point(3, 4)
p2 = Point(0, 0)
print(p1.distance())  # Should print 5.0
print(p1.distance_to(p2))  # Should print 5.0