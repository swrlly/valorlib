from ..PacketReader import PacketReader
from ..DataStructures import WorldPosData, SlotObjectData

class UseItem:

	"""sent by client when an item is used, like a spell"""

	def __init__(self):
		self.time = 0
		self.slotObject = SlotObjectData()
		self.itemUsePos = WorldPosData()
		self.useType = 0

	def read(self, data):
		reader = PacketReader(data)
		self.time = reader.ReadInt()
		self.slotObject.parseFromInput(reader)
		self.itemUsePos.parseCoords(reader)
		self.useType = reader.ReadByte()

	def write(self, writer):
		writer.WriteInt(self.time)
		self.slotObject.write(writer)
		self.itemUsePos.write(writer)
		writer.WriteByte(self.useType)

	def PrintString(self):
		self.slotObject.PrintString()
		self.itemUsePos.PrintString()
		print("time", self.time, "useType", self.useType)