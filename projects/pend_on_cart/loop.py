import numpy as np
import math
import matplotlib.pyplot as plt
from projects.pend_on_cart.system import Robot  # System
import asyncio
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def simulate(ws, context): # For the websocket to await for a function, the function must be declared as async def
  strat = None
  if context == "lqr":
    from projects.pend_on_cart.controller import LQR as strat  # Controller
    await ws.send_json({"message": "strategyType","strategy":"lqr"}) # For FastAPI websocket the send must be awaited

  elif context == "desc":
    from projects.pend_on_cart.controller import NoController as strat  # Controller
    await ws.send_json({"message": "strategyType","strategy":"no_controller"})

  elif context == "smc":
    from projects.pend_on_cart.controller import SMC as strat
    await ws.send_json({"message": "strategyType","strategy":"no_controller"})

  # Time step width
  dt = 0.01

  # Number of steps
  N = 1000

  # initial starting point
  setpoint = np.array([0,0,0,0])


  # Initial state
  vx = 0            # Translational velocity of cart
  x = 0.00          # Position of cart
  tdi = 58  # Angle of pendulum in degrees
  th = math.pi/180 * tdi # Angle in radians
  wt = 0            # Angular velocity of pendulum

  # Arrays to record the data
  ct = 0 # Current time

  s = np.array([x, vx, th, wt]) # Current states

  robo = Robot(s, setpoint)

  t = np.array([])
  arrx = np.array([])
  arrth = np.array([])

  if strat != None:
    await ws.send_json({"message":"sending_simulation_data"})

    for i in range(N):

      # Updated states using RK4 method
      k1s = dt*strat(robo, 0)                # strat defines the strategy used to control e.g. LQR
      k2s = dt*strat(robo, 0.5*k1s)
      k3s = dt*strat(robo, 0.5*k2s)
      k4s = dt*strat(robo, k3s)

      s += (k1s + 2*k2s + 2*k3s + k4s)/6 # New states
      robo.state = s + 0.01*np.random.randn(4)
      ct += dt

      t = np.append(t,ct)
      arrx = np.append(arrx, robo.state[0])
      arrth = np.append(arrth, robo.state[2])

      await ws.send_json({"message":"simdata", "states":s.tolist(), "time": ct}) # Numpy array s is not JSON serializable so it is converted to python list
      await asyncio.sleep(dt)

  else:
    await ws.send_json({"message":"strategyType", "strategy":"None"})
    return
  
  plt.plot(arrth, arrx)
  plt.show()