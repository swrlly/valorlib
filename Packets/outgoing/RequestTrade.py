from ..PacketReader import PacketReader

class RequestTrade:

	""" sent by client to request a trade with a player """

	def __init__(self):
		self.name = ""

	def read(self, data):
		reader = PacketReader(data)
		self.name = reader.ReadString()

	def write(self, writer):
		writer.WriteString(self.name)