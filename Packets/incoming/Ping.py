from ..PacketReader import PacketReader

class Ping:

	""" 
	sent by server to ensure client is still connected
	sent every 3 seconds on valor
	"""

	def __init__(self):
		self.serial = 0

	def read(self, data):
		reader = PacketReader(data)
		self.serial = reader.ReadInt()

	def PrintString(self):
		print("serial", self.serial)