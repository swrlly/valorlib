from ..PacketReader import PacketReader

class Load: 

	""" sent by client to load a character """

	def __init__(self):
		self.charID = 0
		self.isFromArena = False

	def read(self, data):
		reader = PacketReader(data)
		self.charID = reader.ReadInt()
		self.isFromArena = reader.ReadBoolean()

	def write(self, writer):
		writer.WriteInt(self.charID)
		writer.WriteBoolean(self.isFromArena)

	def PrintString(self):
		print("charID", self.charID, "isFromArena", self.isFromArena)