from ..PacketReader import PacketReader

class Teleport:

	""" sent by client to teleport to a certain object ID """

	def __init__(self):
		self.objectID = 0

	def read(self, data):
		reader = PacketReader(data)
		self.objectID = reader.ReadInt()

	def write(self, writer):
		writer.WriteInt(self.objectID)