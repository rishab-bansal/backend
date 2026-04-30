import numpy as np

def LQR(robo, rkc):
  s = robo.state + rkc
  setpoint = robo.destination

  # Computing the controller output
  K = np.matrix([-1.0000,   -2.0317,  -32.8597,  -10.0141])
  feedback = -setpoint + s
  F = float(- K @ feedback)

  # F = 0
  # if ct == 0:
  #   F = -10
  # else:
  #   F = 0
  sd = np.zeros(4)

  # Calculating the derivatives
  sd[0] = s[1]
  sd[2] = s[3]
  [sd[3], sd[1]] = robo.acc(float(s[2]), F, float(s[3]))

  return sd

def NoController(robo, rkc):
  s = robo.state + rkc
  setpoint = robo.destination

  # Computing the controller output
  K = np.matrix([0,  0,  0,  0])
  feedback = -setpoint + s
  F = float(- K @ feedback)

  # F = 0
  # if ct == 0:
  #   F = -10
  # else:
  #   F = 0
  sd = np.zeros(4)

  # Calculating the derivatives
  sd[0] = s[1]
  sd[2] = s[3]
  [sd[3], sd[1]] = robo.acc(float(s[2]), F, float(s[3]))

  return sd