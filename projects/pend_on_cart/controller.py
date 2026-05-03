import numpy as np

# Sliding Mode Controller
def SMC(robo, rkc):
  setpoint = robo.destination
  states = robo.state + rkc - setpoint
  # we have to calculate the F i.e the input to the robot
  # Defining the sliding surface
  CT = np.array([1,1,5,2])
  # CT = np.array([1,1,5,2])

  def sign_sat(s):
    phi = 1
    return np.clip(s/phi, -s, s)
    # if s > phi:
    #   return 1
    # elif s < phi:
    #   return -1
    # else:
    #   return s/phi

  def slidsurf(states):
    s = CT @ states    # s1 + s2 + s3 + s4 = 0
    return s

  def diffslids(states):
    return CT

  eta = 1
  s = slidsurf(states)       # Value wrt sliding surface
  
  f24 = robo.f24(states[2], states[3])
  g24 = robo.g24(states[2], states[3])

  f = np.array([states[1], f24[0], states[3], f24[1]])

  g = np.array([0, g24[0], 0, g24[1]])
  # Computing the input to the system
  inv = float((diffslids(states) @ g))

  if abs(inv) < 1e-6:
    F = 0
  else:
    F = (-diffslids(states) @ f - eta*sign_sat(s))/inv

  ##################################################
  statesd = np.zeros(4)
  statesd[0] = states[1]
  statesd[2] = states[3]
  [statesd[1], statesd[3]] = robo.acc(float(states[2]), F, float(states[3]))
  return statesd



# Linear Quadratic Regulator

def LQR(robo, rkc):
  s = robo.state + rkc
  setpoint = robo.destination

  # Computing the controller output
  K = np.matrix([-1.0000,   -2.0317,  -32.8597,  -10.0141])
  # K = np.matrix([-0.1000,   -0.5109,  -24.7488,   -7.5322])
  feedback = -setpoint + s
  F = float((- K @ feedback)[0,0])

  # F = 0
  # if ct == 0:
  #   F = -10
  # else:
  #   F = 0
  sd = np.zeros(4)

  # Calculating the derivatives
  sd[0] = s[1]
  sd[2] = s[3]
  [sd[1], sd[3]] = robo.acc(float(s[2]), F, float(s[3]))

  return sd

# No-Controller performance
def NoController(robo, rkc):
  s = robo.state + rkc
  setpoint = robo.destination

  # Computing the controller output
  K = np.matrix([0,  0,  0,  0])
  feedback = -setpoint + s
  F = float((- K @ feedback)[0,0])

  # F = 0
  # if ct == 0:
  #   F = -10
  # else:
  #   F = 0
  sd = np.zeros(4)

  # Calculating the derivatives
  sd[0] = s[1]
  sd[2] = s[3]
  [sd[1], sd[3]] = robo.acc(float(s[2]), F, float(s[3]))

  return sd