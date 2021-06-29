from ..PacketReader import PacketReader

class Buy:

	""" Sent by client to buy an item with a specific objectID """

	def __init__(self):
		self.objectID = 0
		self.quantity = 0
		self.marketID = 0
		self.type = 0

	def read(self, data):
		reader = PacketReader(data)
		self.objectID = reader.ReadInt()
		self.quantity = reader.ReadInt()
		self.marketID = reader.ReadUnsignedInt()
		self.type = reader.ReadInt()

	def write(self, writer):
		writer.WriteInt(self.objectID)
		writer.WriteInt(self.quantity)
		writer.WriteUnsignedInt(self.marketID)
		writer.WriteInt(self.type)

	def PrintString(self):
		print(
			"objectID", self.objectID, "quantity", self.quantity,
			"marketID", self.marketID, "type", self.type
		)