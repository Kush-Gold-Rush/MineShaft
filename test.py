from stable_baselines3 import PPO
from stable_baselines3.common.cmd_util import make_vec_env

from MineShaft import ThetanArenaEnv

def main():
	env = ThetanArenaEnv(io_mode=ThetanArenaEnv.IO_MODE.SIMPLIFIED)
	env = make_vec_env(lambda: env, n_envs=1)
	model = PPO("MlpPolicy", env, verbose=1)
	model.learn(total_timesteps=10_000)

	info = {'waiting': True}
	action = env.action_space.sample()
	action = action * 0
	env.reset()
	for _ in range(10_000):
		if not info['waiting']:
			action, _states = model.predict(observation, deterministic=True)
		observation, reward, done, info = env.step(action)
		if done:
			observation = env.reset()

	env.close()


if __name__ == '__main__':
	main()