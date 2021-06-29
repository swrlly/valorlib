from ..PacketReader import PacketReader

class GotoAck:

	""" sent by client to acknowledge receiving a goto packet """

	def __init__(self):
		self.time = 0

	def read(self, data):
		reader = PacketReader(data)
		self.time = reader.ReadInt()

	def write(self, writer):
		writer.WriteInt(self.time)

	def PrintString(self):
		print("time", self.time)
