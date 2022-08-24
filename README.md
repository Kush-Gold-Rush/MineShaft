# MineShaft
An Gym compatible environment for Artificial Intelligence Reinforcement Agent to play GameFi

> ⚠️ Currently support Windows 10 only

## Getting started (user)
```py3
from MineShaft import MineShaft

env = MineShaft()
env.enter_match(random_character=True)
for _ in range(1000):
  observation, reward, done, info = env.step(env.action_space.sample())
env.close()
```

## Getting started (developer)
Install dependencies
```bash
python3 -m pip install -r requirenments.txt
```

### Test Env with `PPO` (developer)
```bash
python3 test.py
```

Open your favourite editor and change anything to see what will happen.

> ⚠️ Before submitting pull request, please read instructions in [CONTRIBUTING.md](CONTRIBUTING.md)
to prevent reject of pull request ( 🚧 `400 Bad Request`) and make both of us happy ☕.

## Functional requirements
- [ ] The frame-rate of screen capture must be more than 30 frames-per-second.

## Supported GameFis
- Thetan Arena
