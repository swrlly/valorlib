from ..PacketReader import PacketReader

class CreateSuccess:

	""" Sent by server when the player first loads in into a new instance and their character has been succesfully created as an object """

	def __init__(self):
		self.objectID = 0
		self.charID = 0

	def read(self, data):
		reader = PacketReader(data)
		self.objectID = reader.ReadInt()
		self.charID = reader.ReadInt()

	def write(self, writer):
		pass

	def PrintString(self):
		print("objectID:", self.objectID, "charID", self.charID)