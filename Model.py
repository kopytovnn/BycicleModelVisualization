from math import cos, sin


class Bicycle:
    def __init__(self):
        self.lf = 0.721 * 10
        self.lr = 0.823 * 10

    def update(self, pos=(0, 0), global_angle=0):
        front_axle = (pos[0] + self.lf * cos(global_angle), pos[1] + self.lf * sin(global_angle))
        rear_axle = (pos[0] - self.lr * cos(global_angle), pos[1] - self.lr * sin(global_angle))
        return front_axle, rear_axle