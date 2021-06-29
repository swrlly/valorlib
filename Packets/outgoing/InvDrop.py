from ..PacketReader import PacketReader
from ..DataStructures import SlotObjectData

class InvDrop:

	""" Sent by the client to drop an item on the ground """

	def __init__(self):
		self.slotOne = SlotObjectData()

	def read(self, data):
		reader = PacketReader(data)
		self.slotOne.parseFromInput(reader)

	def write(self, writer):
		self.slotOne.write(writer)

	def PrintString(self):
		self.slotOne.PrintString()