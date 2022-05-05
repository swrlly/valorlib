from ..PacketReader import PacketReader
from ..DataStructures import WorldPosData

class EnemyShoot:

	"""
	Sent by server whenever enemy shoots
	note: if multiple shots are sent, only one packet is sent with numShots telling client how many shots enemy shot
	"""
	def __init__(self):
		
		self.bulletID = 0
		self.ownerID = 0
		self.bulletType = 0
		self.pos = WorldPosData()
		self.angle = 0
		self.damage = 0
		self.numShots = 1
		self.angleInc = 0

	def read(self, data):
		reader = PacketReader(data)
		self.bulletID = reader.ReadInt()
		self.ownerID = reader.ReadInt()
		self.bulletType = reader.ReadByte()
		self.pos.parseCoords(reader)
		self.angle = reader.ReadFloat()
		self.damage = reader.ReadShort()
		if reader.BytesLeft() > 0:
			self.numShots = reader.ReadByte()
			self.angleInc = reader.ReadFloat()
		else:
			self.numShots = 1
			self.angleInc = 0

	def write(self, writer):
		writer.WriteInt(self.bulletID)
		writer.WriteInt(self.ownerID)
		writer.WriteByte(self.bulletType)
		self.pos.write(writer)
		writer.WriteFloat(self.angle)
		writer.WriteShort(self.damage)
		writer.WriteByte(self.numShots)
		writer.WriteFloat(self.angleInc)

	def PrintString(self):
		self.pos.PrintString()
		print("bulletID", self.bulletID, "ownerID", self.ownerID, "bulletType", self.bulletType, "angle", self.angle, "damage", self.damage, "numShots", self.numShots, "angleInc", self.angleInc )
