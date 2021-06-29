from ..PacketReader import PacketReader
from ..DataStructures import WorldPosData

class Goto:

	""" Sent by server to inform which objectID will teleport to a new location """

	def __init__(self):
		self.objectID = 0
		self.pos = WorldPosData()

	def read(self, data):
		reader = PacketReader(data)
		self.objectID = reader.ReadInt()
		self.pos.parseCoords(reader)

	def write(self, writer):
		writer.WriteInt(self.objectID)
		self.pos.write(writer)

	def PrintString(self):
		self.pos.PrintString()
		print("objectID", self.objectID)	