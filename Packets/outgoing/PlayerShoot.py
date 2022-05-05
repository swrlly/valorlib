from ..PacketReader import PacketReader
from ..DataStructures import WorldPosData

class PlayerShoot:

	"""
	Sent by the client when we shoot a bullet
	"""

	def __init__(self):
		self.time = 0
		self.bulletID = 0
		self.containerType = 0
		self.pos = WorldPosData()
		self.angle = 0

	def read(self, data):
		reader = PacketReader(data)
		self.time = reader.ReadInt()
		self.bulletID = reader.ReadInt()
		self.containerType = reader.ReadShort()
		self.pos.parseCoords(reader)
		self.angle = reader.ReadFloat()

	def write(self, writer):
		writer.WriteInt(self.time)
		writer.WriteInt(self.bulletID)
		writer.WriteShort(self.containerType)
		self.pos.write(writer)
		writer.WriteFloat(self.angle)

	def PrintString(self):
		self.pos.PrintString()
		print("time", self.time, "bulletID", self.bulletID, "containerType", self.containerType, "angle", self.angle)
