from ..PacketReader import PacketReader

class PlayerText:

	"""
	Sent by client when player types a message in chat
	"""

	def __init__(self):
		self.text = ""

	def read(self, data):
		reader = PacketReader(data)
		self.text = reader.ReadString()

	def write(self, writer):
		writer.WriteString(self.text)

	def PrintString(self):
		print("text", self.text)