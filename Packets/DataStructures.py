class WorldPosData:

	"""
	A data structure representing a 2D location.
	"""

	def __init__(self):
		self.x = 0
		self.y = 0

	def parseCoords(self, reader):
		self.x = reader.ReadFloat()
		self.y = reader.ReadFloat()

	def write(self, writer):
		writer.WriteFloat(self.x)
		writer.WriteFloat(self.y)

	def PrintString(self):
		print("x:", self.x, "y:", self.y)

class GroundTileData:
	
	"""
	x : x coordinate of the tile
	y : y coordinate of the tile
	type : tile type found in GroundCXML
	"""

	def __init__(self):
		self.x = 0
		self.y = 0
		self.type = 0

	def parseFromInput(self, reader):
		self.x = reader.ReadShort()
		self.y = reader.ReadShort()
		self.type = reader.ReadUnsignedShort()

	def write(self, writer):
		writer.WriteShort(self.x)
		writer.WriteShort(self.y)
		writer.WriteUnsignedShort(self.type)

	def PrintString(self):
		print("x", self.x, "y", self.y, "type", self.type)

class ObjectData:

	"""
	Adds objectType to ObjectStatusData
	"""

	def __init__(self):
		self.objectType = 0
		self.objectStatusData = ObjectStatusData()

	def parseFromInput(self, reader):
		self.objectType = reader.ReadUnsignedShort()
		self.objectStatusData.parse(reader)

	def write(self, writer):
		writer.WriteUnsignedShort(self.objectType)
		self.objectStatusData.write(writer)

	def PrintString(self):
		print("objectType", self.objectType)
		self.objectStatusData.PrintString()

class MarketOffer:

	"""
	Data representing an offer to be put on the market.
	"""

	def __init__(self):
		self.price = 0
		self.slotObject = SlotObjectData()

	def parseFromInput(self, reader):
		self.price = reader.ReadInt()
		self.slotObject.parseFromInput(reader)

	def write(self, writer):
		writer.WriteInt(self.price)
		self.slotObject.write(writer)

	def PrintString(self):
		self.slotObject.PrintString()
		print("price", self.price)

class SlotObjectData:

	"""
	Identifying data for a slot.
	objectID: id of the individual this particular slot belongs to
	slotID: the slot ID for this slot
	itemData: a custom Valor serialized json that represents information about the object
	"""

	def __init__(self):
		self.objectID = 0
		self.slotID = 0
		self.itemData = ""

	def parseFromInput(self, reader):
		self.objectID = reader.ReadInt()
		self.slotID = reader.ReadByte()
		self.itemData = reader.ReadString()

	def write(self, writer):
		writer.WriteInt(self.objectID)
		writer.WriteByte(self.slotID)
		writer.WriteString(self.itemData)

	def PrintString(self):
		print("objectID:", self.objectID, "slotID:", self.slotID, "itemData:", self.itemData)

class StatData:

	"""
	Data structure that contains information about attributes.
	Examples include health, mana, total gold, items in inventory, account ID, name, etc..
	"""

	def __init__(self):
		self.statType = 0 #byte
		self.statValue = 0 #int
		self.strStatValue = ""

	def isStringStat(self, x):
		if x == 31 or x == 62 or x == 38 or x == 54 or x == 127 or (8 <= x <= 19) or (71 <= x <= 78) or x == 34:
			return True

	def parse(self, reader):
		self.statType = reader.ReadByte()
		# condition effect
		if not self.isStringStat(self.statType):
			self.statValue = reader.ReadInt()
		else:
			self.strStatValue = reader.ReadString()

	def write(self, writer):
		writer.WriteByte(self.statType)
		if not self.isStringStat(self.statType):
			writer.WriteInt(self.statValue)
		else:
			writer.WriteString(self.strStatValue)

	def PrintString(self):
		print("statType", self.statType, "statValue", self.statValue, "strStatValue", self.strStatValue)

class ObjectStatusData:

	"""
	Data structure that contains a list of StatData objects for a certain objectID.
	"""

	def __init__(self):
		self.objectID = 0
		self.pos = WorldPosData()
		self.stats = [] # statdata objects

	def parse(self, reader): 
		self.objectID = reader.ReadInt()
		self.pos.parseCoords(reader)
		length = reader.ReadShort()
		for _ in range(length):
			s = StatData()
			s.parse(reader)
			self.stats.append(s)

	def write(self, writer):
		writer.WriteInt(self.objectID)
		self.pos.write(writer)
		writer.WriteShort(len(self.stats))
		for s in self.stats:
			s.write(writer)
		
	def PrintString(self):
		print("objid", self.objectID, "pos", self.pos.x, self.pos.y, "len stat", len(self.stats))

class PlayerShopItem:

	""" data structure that contains information about one single item in the market """

	def __init__(self):
		self.ID = 0
		self.itemID = 0
		self.price = 0
		self.insertTime = 0
		self.count = 0
		self.isLast = False

	def parseFromInput(self, reader):
		self.ID = reader.ReadUnsignedInt()
		self.itemID = reader.ReadUnsignedShort()
		self.price = reader.ReadInt()
		self.insertTime = reader.ReadInt()
		self.count = reader.ReadInt()
		self.isLast = reader.ReadBoolean()

	def PrintString(self):
		print(
			"ID", self.ID, "itemID", self.itemID, "price", self.price,
			"insertTime", self.insertTime, "count", self.count, "isLast", self.isLast
		)

class MoveRecord:

	"""move pos @ time"""

	def __init__(self):
		self.time = 0
		self.x = 0
		self.y = 0

	def parseFromInput(self, reader):
		self.time = reader.ReadInt()
		self.x = reader.ReadFloat()
		self.y = reader.ReadFloat()

	def write(self, writer):
		writer.WriteInt(self.time)
		writer.WriteFloat(self.x)
		writer.WriteFloat(self.y)

	def PrintString(self):
		print("time:", self.time, "x:", self.x, "y:", self.y)