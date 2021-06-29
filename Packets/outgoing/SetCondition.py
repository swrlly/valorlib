from ..PacketReader import PacketReader

class SetCondition:

	"""
	Unknown. Auto-DCs on valor.
	"""

	def __init__(self):
		self.conditionEffect = 0
		self.conditionDuration = 0

	def read(self, data):
		reader = PacketReader(data)
		self.conditionEffect = reader.ReadByte()
		self.conditionDuration = reader.ReadFloat()

	def write(self, writer):
		writer.WriteByte(self.conditionEffect)
		writer.WriteFloat(self.conditionDuration)

	def PrintString(self):
		print("conditionEffect", self.conditionEffect, "conditionDuration", self.conditionDuration)
