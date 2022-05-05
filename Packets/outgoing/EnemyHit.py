from ..PacketReader import PacketReader

class EnemyHit:

	"""
	Sent by the client when we hit an enemy

	bulletID : bulletID of the bullet that hit the enemy
	targetID : objectID of the enemy we hit
	"""
	def __init__(self):
		self.time = 0
		self.bulletID = 0
		self.targetID = 0
		self.kill = False

	def read(self, data):
		reader = PacketReader(data)
		self.time = reader.ReadInt()
		self.bulletID = reader.ReadInt()
		self.targetID = reader.ReadInt()
		self.kill = reader.ReadBoolean()

	def write(self, writer):
		writer.WriteInt(self.time)
		writer.WriteInt(self.bulletID)
		writer.WriteInt(self.targetID)
		writer.WriteBoolean(self.kill)

	def PrintString(self):
		print("time", self.time, "bulletID", self.bulletID, "targetID", self.targetID, "kill", self.kill)
