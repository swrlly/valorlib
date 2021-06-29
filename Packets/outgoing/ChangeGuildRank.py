from ..PacketReader import PacketReader

class ChangeGuildRank:

	"""
	Sent by client when player changes the rank of someone in the guild.

	initiate : rank 0
	member : rank 10
	officer : 20
	leader : 30
	"""

	def __init__(self):
		self.name = ""
		self.guildRank = 0

	def read(self, data):
		reader = PacketReader(data)
		self.name = reader.ReadString()
		self.guildRank = reader.ReadInt()

	def write(self, writer):
		writer.WriteString(self.name)
		writer.WriteInt(self.guildRank)

	def PrintString(self):
		print("name", self.name, "rank", self.guildRank)
