
from ..PacketReader import PacketReader
from ..DataStructures import WorldPosData

class GroundDamage:

	"""
	Sent by client when client takes ground damage (like lava)
	"""

	def __init__(self):
		self.time = 0
		self.pos = WorldPosData()

	def read(self, data):
		reader = PacketReader(data)
		self.time = reader.ReadInt()
		self.pos.parseCoords(reader)

	def write(self, writer):
		writer.WriteInt(self.time)
		self.pos.write(writer)