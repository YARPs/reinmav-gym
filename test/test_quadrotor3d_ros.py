# core modules
import unittest

# 3rd party modules
import gym

# internal modules
import gym_reinmav
from timeit import default_timer as timer
import time

class Environments(unittest.TestCase):
	def test_env(self):
		env = gym.make('quadrotor3d-v0')
		env.reset()
		start_t=timer()
		for i,_ in enumerate(range(4000)): #dt=0.01, 400*0.01=4s

			action = env.control()
			_, reward, done, _ = env.step(action) # take a random action
			env.ros_render()  # take a random action
			if(done):
				env.reset()
			time.sleep(0.01)
		end_t=timer()
		print("simulation time=",end_t-start_t)
		# env.plot_state()
if __name__ == "__main__":
	env=Environments()
	env.test_env()