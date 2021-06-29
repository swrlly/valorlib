from ..PacketReader import PacketReader
from ..DataStructures import SlotObjectData

class RenameItem:

	""" Sent by the client to rename an item. """

	def __init__(self):
		self.slotOne = SlotObjectData()
		self.slotTwo = SlotObjectData()
		self.name = ""

	def read(self, data):
		reader = PacketReader(data)
		self.slotOne.parseFromInput(reader)
		self.slotTwo.parseFromInput(reader)
		self.name = ""

	def write(self, writer):
		self.slotOne.write(writer)
		self.slotTwo.write(writer)
		writer.WriteString(self.name)

	def PrintString(self):
		self.slotOne.PrintString()
		self.slotTwo.PrintString()
		print(self.name)
