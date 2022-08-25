# MineShaft
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
An Gym compatible environment for Artificial Intelligence Reinforcement Agent to play GameFi

> ⚠️ Currently support Windows 10 only
## Getting started
Install [Thetan Arena](https://thetanarena.com/)
And set its resolution to 1280 * 720

Download this repository
```bash
git clone -b develop https://github.com/NewJerseyStyle/MineShaft.git
```

Install dependencies
```bash
cd MineShaft
python3 -m pip install -r requirenments.txt
```

Test to train with PPO (CnnPolicy)
```bash
python3 test.py
```

## Getting started (user)
```py3
from MineShaft import MineShaft

env = MineShaft()
env.enter_match(random_character=True)
for _ in range(1000):
  observation, reward, done, info = env.step(env.action_space.sample())
env.close()
```

## Supported GameFis
- Thetan Arena

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/210388248"><img src="https://avatars.githubusercontent.com/u/110087604?v=4?s=100" width="100px;" alt=""/><br /><sub><b>LeeKaYip</b></sub></a><br /><a href="https://github.com/Kush-Gold-Rush/MineShaft/commits?author=210388248" title="Tests">⚠️</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

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
- [ ] Support multi resolution
