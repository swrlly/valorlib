from ..PacketReader import PacketReader

class QuestObjId:

	""" sent by server to inform client of objectID of the latest quest """

	def __init__(self):
		self.objectID = 0

	def read(self, data):
		reader = PacketReader(data)
		self.objectID = reader.ReadInt()

	def write(self, writer):
		writer.WriteInt(self.objectID)