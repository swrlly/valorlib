from ..PacketReader import PacketReader
from ..DataStructures import WorldPosData
import time

class ShowEffect:

	"""
	Sent by server to inform the client of an effect.
	Example: Medusa throwing a bomb (the throwing action is the ShowEffect)
	"""

	def __init__(self):
		self.effectType = 0
		self.targetObjectID = 0
		self.pos1 = WorldPosData()
		self.pos2 = WorldPosData()
		self.color = 0
		self.duration = 0

	def read(self, data):
		reader = PacketReader(data)
		self.effectType = reader.ReadByte()
		self.targetObjectID = reader.ReadInt()
		self.pos1.parseCoords(reader)
		self.pos2.parseCoords(reader)
		self.color = reader.ReadInt()
		self.duration = reader.ReadFloat()

	def write(self, writer):
		writer.WriteByte(self.effectType)
		writer.WriteInt(self.targetObjectID)
		self.pos1.write(writer)
		self.pos2.write(writer)
		writer.WriteInt(self.color)
		writer.WriteFloat(self.duration)

	def PrintString(self):
		print("ShowEffect", time.time(), "effectType", self.effectType, "targetObjectID", self.targetObjectID, "color", self.color, "duration", self.duration)
		self.pos1.PrintString()
		self.pos2.PrintString()