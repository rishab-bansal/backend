import math

class Robot:
    def __init__(self, s, setpoint):
        self.m = 0.1
        self.M = 1
        self.g = 9.81
        self.l = 1
        self.state = s
        self.destination = setpoint

    def f24(self, theta, vtheta):
        m = self.m
        M = self.M
        ag = self.g # accelaration due to gravity
        l = self.l
        n = (m+M)*ag*math.sin(theta)-m*l*math.sin(theta)*math.cos(theta)*(vtheta)**2
        d = m*l*(math.sin(theta))**2 + M*l
        f2 = (m*l*math.sin(theta)*(vtheta)**2 - m*ag*math.sin(theta)*math.cos(theta))/(d/l) # acc_x
        f4 = n/d                                                                        # acc_theta
        return [f2, f4]


    def g24(self, theta, vtheta):
        m = self.m
        M = self.M
        ag = self.g
        l = self.l
    
        # n = (m+M)*g*math.sin(theta)-m*l*math.sin(theta)*math.cos(theta)*(vtheta)**2
        d = m*l*(math.sin(theta))**2 + M*l

        g2 = 1/(d/l) # For the calculationn of acc_x but x is s[0]
        g4 = -math.cos(theta)/d # for the calculation of acc_theta but theta is s[2]

        return [g2, g4]

    def acc(self, theta, F, vtheta):  # 
        # m = self.m
        # M = self.M
        # g = self.g
        # l = self.l

        # n = (m+M)*g*math.sin(theta)-m*l*math.sin(theta)*math.cos(theta)*(vtheta)**2
        # cost = math.cos(theta)
        # d = m*l*(math.sin(theta))**2 + M*l
        f = self.f24(theta, vtheta)
        g = self.g24(theta, vtheta)

        # acc_x = (m*l*math.sin(theta)*(vtheta)**2 - m*g*math.sin(theta)*math.cos(theta))/(d/l) + F/(d/l)
        acc_x = f[0] + g[0]*F

        # acc_theta = n/d - F*cost/d
        acc_theta = f[1] + g[1]*F
        return [acc_x, acc_theta]