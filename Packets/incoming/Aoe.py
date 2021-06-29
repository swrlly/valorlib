from ..PacketReader import PacketReader
from ..DataStructures import WorldPosData
import time

class Aoe:

	"""
	Sent by server when an AOE effect hits the ground
	damage is applied serverside

	pos: WorldPosData
	radius: float
	damage: unsigned short
	effect: unsigned byte
	duration: float
	origType: unsigned short
	"""

	def __init__(self):
		self.pos = WorldPosData()
		self.radius = 0
		self.damage = 0
		self.effect = 0
		self.duration = 0
		self.origType = 0

	def read(self, data):
		reader = PacketReader(data)
		self.pos.parseCoords(reader)
		self.radius = reader.ReadFloat()
		self.damage = reader.ReadUnsignedShort()
		self.effect = reader.ReadByte()
		self.duration = reader.ReadFloat()
		self.origType = reader.ReadUnsignedShort()

	def write(self, writer):
		self.pos.write(writer)
		writer.WriteFloat(self.radius)
		writer.WriteUnsignedShort(self.damage)
		writer.WriteByte(self.effect)
		writer.WriteFloat(self.duration)
		writer.WriteUnsignedShort(self.origType)

	def PrintString(self):
		print("Aoe", time.time(), "radius", self.radius, "damage", self.damage, "effect", self.effect, "duration", self.duration, "origType", self.origType)
		self.pos.PrintString()
