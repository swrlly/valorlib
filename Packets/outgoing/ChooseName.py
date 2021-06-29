from ..PacketReader import PacketReader

class ChooseName:

	""" sent by client to choose a name """

	def __init__(self):
		self.name = ""

	def read(self, data):
		reader = PacketReader(data)
		self.name = reader.ReadString()

	def write(self, writer):
		writer.WriteString(self.name)