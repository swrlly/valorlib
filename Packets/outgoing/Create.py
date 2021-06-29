from ..PacketReader import PacketReader

class Create:

	"""
	Sent by client to create a new character
	"""

	def __init__(self):
		self.classType = 0
		self.skinType = 0

	def read(self, data):
		reader = PacketReader(data)
		self.classType = reader.ReadShort()
		self.skinType = reader.ReadShort()

	def write(self, writer):
		writer.WriteShort(self.classType)
		writer.WriteShort(self.skinType)

	def PrintString(self):
		print("classType", self.classType, "skinType", self.skinType)