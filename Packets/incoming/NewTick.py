from ..PacketReader import PacketReader
from ..DataStructures import ObjectStatusData

class NewTick:

	"""
	Sent by server to
	- Update locations of other players, enemies, or certain objects like portals
	- Inform client of statdatas for each player, enemy, etc.
	- Update rotating objects (such as marketplace items)
	- Tell the client where the server thinks you are
	- Tell the client stats about yourself:
		- total fame on account
		- total gold on account
		- fortune_token_stat ? 
		- total onrane on account
		- total kantos
		- total trial tokens
		- hp
		- prot, etc.

	"""

	def __init__(self):
		self.tickID = 0
		self.tickTime = 0
		self.statuses = [] 

	def read(self, data):
		reader = PacketReader(data)
		self.tickID = reader.ReadInt()
		self.tickTime = reader.ReadInt()
		length = reader.ReadShort()
		for _ in range(length):
			o = ObjectStatusData()
			o.parse(reader)
			self.statuses.append(o)

	def write(self, writer):
		writer.WriteInt(self.tickID)
		writer.WriteInt(self.tickTime)
		writer.WriteShort(len(self.statuses))
		for o in self.statuses:
			o.write(writer)

	def PrintString(self):
		print("tickid", self.tickID, "ticktime", self.tickTime, "len statuses / num objs", len(self.statuses))