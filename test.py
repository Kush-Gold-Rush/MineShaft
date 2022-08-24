import time

from stable_baselines3 import PPO

from MineShaft import ThetanArenaEnv

def main():
	env = ThetanArenaEnv()
	model = PPO("MlpPolicy", env, verbose=1)
	model.learn(total_timesteps=10_000)

	info = {'waiting': True}
	action = env.action_space.sample()
	action = action * 0
	i = 0
	while i < 10_000:
		start_time = time.time()
		if not info['waiting']:
			action, _states = model.predict(observation, deterministic=True)
		else:
			i -= 1
		observation, reward, done, info = env.step(action)
		if done:
			observation = env.reset()
		if time.time() - start_time < 0.9:
			try:
				time.sleep(0.1 - time.time() - start_time)
			except:
				pass

	env.close()


if __name__ == '__main__':
	main()