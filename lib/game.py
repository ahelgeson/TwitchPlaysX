import win32api
import win32con
import time

class Game:

  # Dictionary where you can add whatever text command you'd like to see make
	# an action. This uses the Windows Virtual Key Codes (https://docs.microsoft.com/en-us/windows/desktop/inputdev/virtual-key-codes)
	# to map commands to virtual keyboard inputs. For example, "up" presses 0x30,
	# which is the VKC for the 0 key. Use in conjunction with the emulator key
	# inputs.

	keymap = {
		'up': 0x30,
		'down': 0x31,
		'left': 0x32,
		'right': 0x33,
		'a': 0x34,
		'b': 0x35,
		'start': 0x36,
		'select': 0x37,
		'u': 0x30,
		'd': 0x31,
		'l': 0x32,
		'r': 0x33,
		'z': 0x59,
		'zl': 0x38,
		'zr': 0x39,
		'shift': 0x10,
		'f1': 0x70,
		'holdup': 0x30,
		'holdu': 0x30,
		'holddown': 0x31,
		'holdd': 0x31,
		'holdleft': 0x32,
		'holdl': 0x32,
		'holdright': 0x33,
		'holdr': 0x33,
		'stepup': 0x30,
		'stepu': 0x30,
		'stepdown': 0x31,
		'stepd': 0x31,
		'stepleft': 0x32,
		'stepl': 0x32,
		'stepright': 0x33,
		'stepr': 0x33,
		'cu': 0x57,
		'cd': 0x53,
		'cl': 0x41,
		'cr': 0x44,
		'spama': 0x34
	}

	def get_valid_buttons(self):
		return [button for button in self.keymap.keys()]

	def is_valid_button(self, button):
		return button in self.keymap.keys()

	def button_to_key(self, button):
		return self.keymap[button]

	def push_button(self, button):
		win32api.keybd_event(self.button_to_key(button), 0, 0, 0)
		# Define how long key is pressed below in sleep(x).
		time.sleep(1)
		win32api.keybd_event(
			self.button_to_key(button), 0, win32con.KEYEVENTF_KEYUP, 0)
		
	def hold_button(self, button):
		win32api.keybd_event(self.button_to_key(button), 0, 0, 0)
		# Define how long key is pressed below in sleep(x).		
		time.sleep(5)
		win32api.keybd_event(
			self.button_to_key(button), 0, win32con.KEYEVENTF_KEYUP, 0)

	def step_button(self, button):
		win32api.keybd_event(self.button_to_key(button), 0, 0, 0)
		# Define how long key is pressed below in sleep(x).		
		time.sleep(0.05)
		win32api.keybd_event(
			self.button_to_key(button), 0, win32con.KEYEVENTF_KEYUP, 0)
	
	def spam_button(self, button):
		spam = 0
		while spam <= 20:
			win32api.keybd_event(self.button_to_key(button), 0, 0, 0)
			time.sleep(0.5)
			win32api.keybd_event(
				self.button_to_key(button), 0, win32con.KEYEVENTF_KEYUP, 0)
			spam += 1