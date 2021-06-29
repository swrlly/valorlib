from ..PacketReader import PacketReader

class PlayerHit:

	"""
	Sent by client when player is hit by a bullet.

	bulletID - stands for nth bullet enemy shot
	"""

	def __init__(self):
		self.bulletID = 0
		self.objectID = 0

	def read(self, data):
		reader = PacketReader(data)
		self.bulletID = reader.ReadByte()
		self.objectID = reader.ReadInt()

	def write(self, writer):
		writer.WriteByte(self.bulletID)
		writer.WriteInt(self.objectID)

	def PrintString(self):
		print("bulletID", self.bulletID, "objectID", self.objectID)