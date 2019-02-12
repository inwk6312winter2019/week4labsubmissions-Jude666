#This is the code

import math
class point():
    def __init__(self):
        self.x1 = int(input("Please enter a integer: "))
        self.x2 = int(input("Please enter a number: "))
        self.y1 = int(input("Please enter a number"))
        self.y2 = int(input("Please enter a number"))
    def distance_between_points(self):
        dx = self.x1 - self.x2
        dy = self.y1 - self.y2
        dis = math.sqrt(dx**2 + dy**2)
        return dis

point().distance_between_points()
