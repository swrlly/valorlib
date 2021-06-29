from ..PacketReader import PacketReader

class Failure:

	""" sent by server to indicate some type of failure """

	def __init__(self):
		self.errorID = 0
		self.errorDescription = ""

	def read(self, data):
		reader = PacketReader(data)
		self.errorID = reader.ReadInt()
		self.errorDescription = reader.ReadString()

	def write(self, writer):
		writer.WriteInt(self.errorID)
		writer.WriteString(self.errorDescription)

	def PrintString(self):
		print("errorID", self.errorID, "errorDescription", self.errorDescription)
