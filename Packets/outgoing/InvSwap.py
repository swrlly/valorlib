from ..PacketReader import PacketReader
from ..DataStructures import WorldPosData, SlotObjectData

class InvSwap:

	""" Sent by the client to swap items in two slots, with slotOne being the source slot """

	def __init__(self):
		self.time = 0
		self.position = WorldPosData()
		self.slotOne = SlotObjectData()
		self.slotTwo = SlotObjectData()

	def read(self, data):
		reader = PacketReader(data)
		self.time = reader.ReadInt()
		self.position.parseCoords(reader)
		self.slotOne.parseFromInput(reader)
		self.slotTwo.parseFromInput(reader)

	def write(self, writer):
		writer.WriteInt(self.time)
		self.position.write(writer)
		self.slotOne.write(writer)
		self.slotTwo.write(writer)

	def PrintString(self):
		print(
			"time", self.time, 
		)
		self.position.PrintString()
		self.slotOne.PrintString()
		self.slotTwo.PrintString()