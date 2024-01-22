class Info:
    def __init__(self, filename):
        file = open(filename, 'rt').read().replace('\n', '').split('END')
        self.centerLine = []
        self.carPose = []
        self.yaw = []
        self.intersection = []

        for moment in file[:-1]:
            cl, carPose, yaw, intersection, other = moment.split(';')
            cl = cl.split(':')[1]
            centerLine = []
            for dot in cl.split(','):
                if ' ' not in dot:
                    break
                dotx, doty = [float(i) for i in dot.split(' ')]
                centerLine.append((dotx, doty))
            self.centerLine.append(centerLine)
            # print('center line:', self.centerLine)
            carPose = [float(i) for i in carPose.split(':')[1].split()]
            self.carPose.append(carPose)
            # print("carPose:", self.carPose)
            yaw = float(yaw.split(":")[1])
            self.yaw.append(yaw)
            # print('yaw:', self.yaw)
            intersection = [float(i) for i in intersection.split(':')[1].split()]
            self.intersection.append(intersection)
            # print("intersection:", self.intersection)

    def get_centerLine(self, t):
        return self.centerLine[t]

    def get_yaw(self, t):
        return self.yaw[t]

    def get_carPose(self, t):
        return self.carPose[t]

    def get_intersection(self, t):
        return self.intersection[t]

    def get_count(self):
        return len(self.yaw)


if __name__ == "__main__":
    info = Info('a')