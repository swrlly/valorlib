from ..PacketReader import PacketReader

class PotionStorageInteraction:

	"""

	Sent by client to deposit / withdraw potions into potion storage.

	type
	0 - life
	1 - mana
	2 - lexiographic order in the pot UI.

	action
	0 - deposit
	1 - withdraw
	"""

	def __init__(self):
		self.type = 0
		self.action = 0

	def write(self, writer):
		writer.WriteByte(self.type)
		writer.WriteByte(self.action)