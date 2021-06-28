from ..PacketReader import PacketReader
from ..DataStructures import ObjectData, GroundTileData

class Update:

	""" sent by server to inform client of new tiles, objects, and drops """

	def __init__(self):
		self.tiles = []
		self.newObjects = []
		self.drops = []

	def read(self, data):
		reader = PacketReader(data)
		length = reader.ReadShort()
		for _ in range(length):
			g = GroundTileData()
			g.parseFromInput(reader)
			self.tiles.append(g)
		length = reader.ReadShort()
		for _ in range(length):
			g = ObjectData()
			g.parseFromInput(reader)
			self.newObjects.append(g)
		length = reader.ReadShort()
		for _ in range(length):
			self.drops.append(reader.ReadInt())

	def write(self, writer):
		writer.WriteShort(len(self.tiles))
		for i in self.tiles:
			i.write(writer)
		writer.WriteShort(len(self.newObjects))
		for i in self.newObjects:
			i.write(writer)
		writer.WriteShort(len(self.drops))
		for i in self.drops:
			writer.WriteInt(i)

	def PrintString(self):
		print(len(self.tiles), "tiles,", len(self.newObjects), "newObjects,", len(self.drops), "drops")
		for i in self.newObjects:
			i.PrintString()