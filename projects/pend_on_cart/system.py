import math

class Robot:
    def __init__(self, s, setpoint):
        self.m = 0.1
        self.M = 1
        self.g = 9.81
        self.l = 1
        self.state = s
        self.destination = setpoint

    def acc(self, theta, F, vtheta):  # 
        m = self.m
        M = self.M
        g = self.g
        l = self.l

        n = (m+M)*g*math.sin(theta)-m*l*math.sin(theta)*math.cos(theta)*(vtheta)**2
        cost = math.cos(theta)
        d = m*l*(math.sin(theta))**2 + M*l

        acc_theta = n/d - F*cost/d
        # acc_x = (n/cost)/(d/l) + g*math.tan(theta) + F/(d/l)
        # acc_x = -(n/cost)/(d/l) + g*math.tan(theta) + F/(d/l)
        acc_x = (m*l*math.sin(theta)*(vtheta)**2 - m*g*math.sin(theta)*math.cos(theta))/(d/l) + F/(d/l)
        return [acc_theta, acc_x]