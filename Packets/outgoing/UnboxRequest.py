from ..PacketReader import PacketReader

class UnboxRequest:

	"""
	Sent by client when player requests to unbox a lootbox.
	"""

	def __init__(self):
		self.lootboxType = 0

	def read(self, data):
		reader = PacketReader(data)
		self.lootboxType = reader.ReadInt()

	def write(self, writer):
		writer.WriteInt(self.lootboxType)