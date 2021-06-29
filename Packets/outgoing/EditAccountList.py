from ..PacketReader import PacketReader

class EditAccountList:

	""" sent by client to lock or ignore someone """

	def __init__(self):
		self.accountListID = 0
		self.add = False
		self.objectID = 0

	def read(self, data):
		reader = PacketReader(data)
		self.accountListID = reader.ReadInt()
		self.add = reader.ReadBoolean()
		self.objectID = reader.ReadInt()

	def write(self, writer):
		writer.WriteInt(self.accountListID)
		writer.WriteBoolean(self.add)
		writer.WriteInt(self.objectID)

	def PrintString(self):
		print(
			"accountListID:", self.accountListID, "add", self.add, "objectID", self.objectID
		)