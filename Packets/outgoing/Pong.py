from ..PacketReader import PacketReader

class Pong:

	""" sent by client to respond to Ping """

	def __init__(self):
		self.serial = 0
		self.time = 0

	def read(self, data):
		reader = PacketReader(data)
		self.serial = reader.ReadInt()
		self.time = reader.ReadInt()

	def write(self, writer):
		writer.WriteInt(self.serial)
		writer.WriteInt(self.time)

	def PrintString(self):
		print("serial", self.serial, "time", self.time)