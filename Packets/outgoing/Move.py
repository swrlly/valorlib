from ..PacketReader import PacketReader
from ..DataStructures import WorldPosData, MoveRecord

class Move:

	""" sent by client to move the character """

	def __init__(self):
		self.objectID = 0
		self.tickID = 0
		self.time = 0
		self.newPosition = WorldPosData()
		self.records = []

	def read(self, data):
		reader = PacketReader(data)
		self.objectID = reader.ReadInt()
		self.tickID = reader.ReadInt()
		self.time = reader.ReadInt()
		self.newPosition.parseCoords(reader)
		length = reader.ReadShort()

		for _ in range(length):
			m = MoveRecord()
			m.parseFromInput(reader)
			self.records.append(m)

	def write(self, writer):
		writer.WriteInt(self.objectID)
		writer.WriteInt(self.tickID)
		writer.WriteInt(self.time)
		self.newPosition.write(writer)
		writer.WriteShort(len(self.records))
		for i in self.records:
			i.write(writer)

	def PrintString(self):
		self.newPosition.PrintString()
		print("objectID", self.objectID, "tickID", self.tickID, "time", self.time)
		print("records:")
		for i in self.records:
			i.PrintString()