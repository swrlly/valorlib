from ..PacketReader import PacketReader
import time

class Death:

	"""
	Sent by server to inform client that you have died.
	"""

	def __init__(self):
		self.accountID = ""
		self.charID = 0
		self.killedBy = ""
		self.zombieID = 0
		self.zombieType = 0
		self.isZombie = False
	
	def read(self, data):
		reader = PacketReader(data)
		self.accountID = reader.ReadString()
		self.charID = reader.ReadInt()
		self.killedBy = reader.ReadString()
		self.zombieType = reader.ReadInt()
		self.zombieID = reader.ReadInt()

	def write(self, writer):
		writer.WriteString(self.accountID)
		writer.WriteInt(self.charID)
		writer.WriteString(self.killedBy)
		writer.WriteInt(self.zombieType)
		writer.WriteInt(self.zombieID)

	def PrintString(self):
		print("Death", time.time(), "accountID", self.accountID, "charID", self.charID, "killedBy", self.killedBy)