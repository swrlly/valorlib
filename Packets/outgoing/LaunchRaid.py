from ..PacketReader import PacketReader

class LaunchRaid:

	"""
	Sent by client to launch a raid.
	"""

	def __init__(self):
		self.raidID = 0
		self.ultra = 0

	def read(self, data):
		reader = PacketReader(data)
		self.raidID = reader.ReadInt()
		self.ultra = reader.ReadBoolean()

	def write(self, writer):
		writer.WriteInt(self.raidID)
		writer.WriteBoolean(self.ultra)