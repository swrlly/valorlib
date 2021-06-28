from ..PacketReader import PacketReader

class InvResult:

	""" sent by server to inform the client on success after invswap / invdrop """

	def __init__(self):
		self.result = 0

	def read(self, data):
		reader = PacketReader(data)
		self.result = reader.ReadInt()

	def write(self, writer):
		writer.WriteInt(self.result)

	def PrintString(self):
		print("result:", self.result)