from ..PacketReader import PacketReader

class QueuePing:

	"""
	Sent by server to inform client which position in the queue you are in
	should be realm portal queue? not sure as valor :dead: rn
	"""

	def __init__(self):
		self.serial = 0
		self.position = 0
		self.count = 0

	def read(self, data):
		reader = PacketReader(data)
		self.serial = reader.ReadInt()
		self.position = reader.ReadInt()
		self.count = reader.ReadInt()

	def PrintString(self):
		print("serial", self.serial, "position", self.position, "count", self.count)
