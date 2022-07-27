import unittest

import numpy as np
import pyautogui

from MineShaft.ThetanArenaEnv import ThetanArenaEnv

class ThetanArenaEnvTestCase(unittest.TestCase):
	def setUp(self):
		self.args = (0.3, 0.6)
		self.env = ThetanArenaEnv()

	def tearDown(self):
		self.args = None

	def test__mouse_move(self):
		expected = np.asarray(pyautogui.size()) * np.asarray(self.args);
		self.env._mouse_click(*self.args);
		result = np.asarray(pyautogui.position());
		self.assertTrue(np.abs(expected - result) < 2);
