from .PacketTypes import PacketTypes
from .PacketReader import PacketReader

import time

class GroundTileData:
	
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

class Update:

	""" sent by server to inform client of new tiles, objects, and drops """

	def __init__(self):
		self.tiles = []
		self.newObjects = []
		self.drops = []

	def read(self, data):
		reader = PacketReader(data)
		length = reader.ReadShort()
		for _ in range(length):
			g = GroundTileData()
			g.parseFromInput(reader)
			self.tiles.append(g)
		length = reader.ReadShort()
		for _ in range(length):
			g = ObjectData()
			g.parseFromInput(reader)
			self.newObjects.append(g)
		length = reader.ReadShort()
		for _ in range(length):
			self.drops.append(reader.ReadInt())

	def write(self, writer):
		writer.WriteShort(len(self.tiles))
		for i in self.tiles:
			i.write(writer)
		writer.WriteShort(len(self.newObjects))
		for i in self.newObjects:
			i.write(writer)
		writer.WriteShort(len(self.drops))
		for i in self.drops:
			writer.WriteInt(i)

	def PrintString(self):
		print(len(self.tiles), "tiles,", len(self.newObjects), "newObjects,", len(self.drops), "drops")
		for i in self.newObjects:
			i.PrintString()

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


class WorldPosData:

	"""x and y coords, floats"""

	def __init__(self):
		self.x = 0
		self.y = 0

	def parseCoords(self, reader):
		"""
		data is the packet buffer
		"""
		self.x = reader.ReadFloat()
		self.y = reader.ReadFloat()

	def write(self, writer):

		writer.WriteFloat(self.x)
		writer.WriteFloat(self.y)

	def PrintString(self):
		print("x:", self.x, "y:", self.y)

class SlotObjectData:

	"""object data for a slot"""

	def __init__(self):
		self.objectID = 0
		self.slotID = 0
		self.itemData = ""

	def parseFromInput(self, reader):
		"""
		data is the packet buffer
		"""
		self.objectID = reader.ReadInt()
		self.slotID = reader.ReadByte()
		self.itemData = reader.ReadString()

	def write(self, writer):

		writer.WriteInt(self.objectID)
		writer.WriteByte(self.slotID)
		writer.WriteString(self.itemData)

	def PrintString(self):
		print("objectID:", self.objectID, "slotID:", self.slotID, "itemData:", self.itemData)

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

class BuyResult:

	""" sent by server to inform client what happened after sending Buy packet """

	def __init__(self):
		self.result = 0
		self.resultString = ""

	def read(self, data):
		reader = PacketReader(data)
		self.result = reader.ReadInt()
		self.resultString = reader.ReadString()

	def PrintString(self):
		print("result", self.result, "resultString", self.resultString)

class InvSwap:

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

class RenameItem:

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

class InvDrop:

	def __init__(self):
		self.slotOne = SlotObjectData()

	def read(self, data):
		reader = PacketReader(data)
		self.slotOne.parseFromInput(reader)

	def write(self, writer):
		self.slotOne.write(writer)

	def PrintString(self):
		self.slotOne.PrintString()

class InvResult:

	""" sent by server to ? """

	def __init__(self):
		self.result = 0

	def read(self, data):
		reader = PacketReader(data)
		self.result = reader.ReadInt()

	def write(self, writer):
		writer.WriteInt(self.result)

	def PrintString(self):
		print("result:", self.result)

class UpdateAck:

	def __init__(self):
		pass

	def read(self, data):
		pass
	
	def write(self, writer):
		pass

class Hello:

	def __init__(self):
		self.buildVersion = ""
		self.gameID = 0
		self.guid = ""
		self.password = ""
		self.secret = ""
		self.keyTime = 0
		self.key = bytearray()
		self.mapJSON = ""
		self.cliBytes = 0

	def read(self, data):
		reader = PacketReader(data)
		self.buildVersion = reader.ReadString()
		self.gameID = reader.ReadInt()
		self.guid = reader.ReadString()
		self.password = reader.ReadString()
		self.secret = reader.ReadString()
		self.keyTime = reader.ReadInt()
		length = reader.ReadShort()
		self.key = [reader.ReadByte() for _ in range(length)]
		lengthJSON = reader.ReadInt()
		self.mapJSON = reader.ReadStringBytes(lengthJSON)
		self.cliBytes = reader.ReadInt()

	def write(self, writer):
		writer.WriteString(self.buildVersion)
		writer.WriteInt(self.gameID)
		writer.WriteString(self.guid)
		writer.WriteString(self.password)
		writer.WriteString(self.secret)
		writer.WriteInt(self.keyTime)
		writer.WriteShort(len(self.key))
		for byte in self.key:
			writer.WriteByte(byte)
		writer.WriteInt(len(self.mapJSON))
		writer.WriteStringBytes(self.mapJSON)
		writer.WriteInt(self.cliBytes)

	def PrintString(self):
		print("buildVersion", self.buildVersion, "gameID", self.gameID, "guid", self.guid, "password", self.password,
			"secret", self.secret, "keyTime", self.keyTime, "key", self.key, "mapJSON", self.mapJSON, "cliBytes", self.cliBytes)

class QueuePing:

	def __init__(self):
		self.serial = 0
		self.position = 0
		self.count = 0

	def read(self, data):
		reader = PacketReader(data)
		self.serial = reader.ReadInt()
		self.position = reader.ReadInt()
		self.count = reader.ReadInt()

	def PrintString(self):
		print("serial", self.serial, "position", self.position, "count", self.count)

class QueuePong:

	def __init__(self):
		self.serial = 0
		self.time = 0

	def read(self, data):
		reader = PacketReader(data)
		self.serial = reader.ReadInt()
		self.time = reader.ReadInt()

	def write(self, writer):
		writer.WriteInt(self.serial)
		writer.WriteInt(self.time)

	def PrintString(self):
		print("serial", self.serial, "time", self.time)	

class Ping:

	def __init__(self):
		self.serial = 0

	def read(self, data):
		reader = PacketReader(data)
		self.serial = reader.ReadInt()

	def PrintString(self):
		print("serial", self.serial)

class Pong:

	def __init__(self):
		self.serial = 0
		self.time = 0

	def read(self, data):
		reader = PacketReader(data)
		self.serial = reader.ReadInt()
		self.time = reader.ReadInt()

	def write(self, writer):
		writer.WriteInt(self.serial)
		writer.WriteInt(self.time)

	def PrintString(self):
		print("serial", self.serial, "time", self.time)

class Aoe:

	"""
	Sent by server when an AOE bullet hits the ground

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

class GroundDamage:

	"""
	Sent by client when client takes ground damage (like lava)
	"""

	def __init__(self):
		self.time = 0
		self.pos = WorldPosData()

	def read(self, data):
		reader = PacketReader(data)
		self.time = reader.ReadInt()
		self.pos.parseCoords(reader)

	def write(self, writer):
		writer.WriteInt(self.time)
		self.pos.write(writer)

class PlayerShoot:

	"""
	Sent by the client when we shoot a bullet
	"""

	def __init__(self):
		self.time = 0
		self.bulletID = 0
		self.containerType = 0
		self.pos = WorldPosData()
		self.angle = 0

	def read(self, data):
		reader = PacketReader(data)
		self.time = reader.ReadInt()
		self.bulletID = reader.ReadByte()
		self.containerType = reader.ReadShort()
		self.pos.parseCoords(reader)
		self.angle = reader.ReadFloat()

	def write(self, writer):
		writer.WriteInt(self.time)
		writer.WriteByte(self.bulletID)
		writer.WriteShort(self.containerType)
		self.pos.write(writer)
		writer.WriteFloat(self.angle)

	def PrintString(self):
		self.pos.PrintString()
		print("time", self.time, "bulletID", self.bulletID, "containerType", self.containerType, "angle", self.angle)

class EnemyHit:

	"""
	Sent by the client when we hit an enemy

	bulletID : bulletID of the bullet that hit the enemy
	targetID : objectID of the enemy we hit
	"""
	def __init__(self):
		self.time = 0
		self.bulletID = 0
		self.targetID = 0
		self.kill = False

	def read(self, data):
		reader = PacketReader(data)
		self.time = reader.ReadInt()
		self.bulletID = reader.ReadByte()
		self.targetID = reader.ReadInt()
		self.kill = reader.ReadBoolean()

	def write(self, writer):
		writer.WriteInt(self.time)
		writer.WriteByte(self.bulletID)
		writer.WriteInt(self.targetID)
		writer.WriteBoolean(self.kill)

	def PrintString(self):
		print("time", self.time, "bulletID", self.bulletID, "targetID", self.targetID, "kill", self.kill)

class EnemyShoot:

	"""
	Sent by server whenever enemy shoots
	"""
	def __init__(self):
		
		self.bulletID = 0
		self.ownerID = 0
		self.bulletType = 0
		self.pos = WorldPosData()
		self.angle = 0
		self.damage = 0
		self.numShots = 0
		self.angleInc = 0

	def read(self, data):
		reader = PacketReader(data)
		self.bulletID = reader.ReadByte()
		self.ownerID = reader.ReadInt()
		self.bulletType = reader.ReadByte()
		self.pos.parseCoords(reader)
		self.angle = reader.ReadFloat()
		self.damage = reader.ReadShort()
		self.numShots = reader.ReadByte()
		self.angleInc = reader.ReadFloat()

	def write(self, writer):
		writer.WriteByte(self.bulletID)
		writer.WriteInt(self.ownerID)
		writer.WriteByte(self.bulletType)
		self.pos.write(writer)
		writer.WriteFloat(self.angle)
		writer.WriteShort(self.damage)
		writer.WriteByte(self.numShots)
		writer.WriteFloat(self.angleInc)

	def PrintString(self):
		self.pos.PrintString()
		print("bulletID", self.bulletID, "ownerID", self.ownerID, "bulletType", self.bulletType, "angle", self.angle, "damage", self.damage, "numShots", self.numShots, "angleInc", self.angleInc )


class Reconnect:

	def __init__(self):
		self.name = ""
		self.host = ""
		self.port = 0
		self.gameID = 0
		self.keyTime = 0
		self.key = bytearray()
		self.isFromArena = False

	def read(self, data):
		reader = PacketReader(data)
		self.name = reader.ReadString()
		self.host = reader.ReadString()
		self.port = reader.ReadInt()
		self.gameID = reader.ReadInt()
		self.keyTime = reader.ReadInt()
		self.isFromArena = reader.ReadBoolean()

		length = reader.ReadShort()
		self.key = [reader.ReadByte() for _ in range(length)]

	def write(self, writer):
		writer.WriteString(self.name)
		writer.WriteString(self.host)
		writer.WriteInt(self.port)
		writer.WriteInt(self.gameID)
		writer.WriteInt(self.keyTime)
		writer.WriteBoolean(self.isFromArena)
		writer.WriteShort(len(self.key))
		for byte in self.key:
			writer.WriteByte(byte)

	def PrintString(self):
		print(
			"name:", self.name, "host", self.host, "port", self.port, "gameID", self.gameID,
			"keyTime", self.keyTime, "key", self.key, "isFromArena", self.isFromArena
		)

class AccountList:

	"""
	sent by server to tell you what accounts you've locked and ignored

	accountlistID 0 is locked, accountlistID 1 is ignored

	"""

	def __init__(self):
		self.accountListID = 0
		self.numAccounts = 0
		self.accountList = []
		self.lockAction = 0

	def read(self, data):
		reader = PacketReader(data)
		self.accountListID = reader.ReadInt()
		self.numAccounts = reader.ReadShort()
		self.accountList = [reader.ReadString() for _ in range(self.numAccounts)]
		self.lockAction = reader.ReadInt()

	def PrintString(self):
		print("accountListID", self.accountListID, "numAccounts", self.numAccounts, "accountList", self.accountList, "lock", self.lockAction)

class Load: 

	""" sent by client to load a character """

	def __init__(self):
		self.charID = 0
		self.isFromArena = False

	def read(self, data):
		reader = PacketReader(data)
		self.charID = reader.ReadInt()
		self.isFromArena = reader.ReadBoolean()

	def write(self, writer):
		writer.WriteInt(self.charID)
		writer.WriteBoolean(self.isFromArena)

	def PrintString(self):
		print("charID", self.charID, "isFromArena", self.isFromArena)

class CreateSuccess:

	"""
	Sent by server when the player first loads in.
	"""

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

class Buy:

	""" sent by client to buy an item from the marketplace """

	def __init__(self):
		self.objectID = 0
		self.quantity = 0
		self.marketID = 0
		self.type = 0

	def read(self, data):
		reader = PacketReader(data)
		self.objectID = reader.ReadInt()
		self.quantity = reader.ReadInt()
		self.marketID = reader.ReadUnsignedInt()
		self.type = reader.ReadInt()

	def write(self, writer):
		writer.WriteInt(self.objectID)
		writer.WriteInt(self.quantity)
		writer.WriteUnsignedInt(self.marketID)
		writer.WriteInt(self.type)

	def PrintString(self):
		print(
			"objectID", self.objectID, "quantity", self.quantity,
			"marketID", self.marketID, "type", self.type
		)


class MarketOffer:

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


class MarketCommand:

	""" sent by client to perform certain market actions """

	def __init__(self):
		self.commandID = 0
		self.offerID = 0
		self.newOffers = []

	def read(self, data):

		reader = PacketReader(data)
		self.commandID = reader.ReadByte()
		print(self.commandID)

		# request my own items
		if self.commandID == 0:
			return
			
		# send a(n) offer(s) to the server
		elif self.commandID == 1:
			numOffers = reader.ReadInt()
			for _ in range(numOffers):
				offer = MarketOffer()
				offer.parseFromInput(reader)
				self.newOffers.append(offer)

		elif self.commandID == 2:
			self.offerID = reader.ReadUnsignedInt()

		# initial request for items
		elif self.commandID == 3:
			return
		
	def write(self, writer):

		writer.WriteByte(self.commandID)
		
		if self.commandID == 0:
			return

		elif self.commandID == 1:
			writer.WriteInt(len(self.newOffers))
			for offer in self.newOffers:
				offer.write(writer)

		elif self.commandID == 2:
			writer.WriteUnsignedInt(self.offerID)

		elif self.commandID == 3:
			return

	def PrintString(self):

		print("commandID", self.commandID, "offerID", self.offerID)

		if len(self.newOffers) > 0:
			for i in range(len(self.newOffers)):
				print("offer {}".format(i))
				self.newOffers[i].PrintString()
		else:
			print("no offers")

class PlayerShopItem:

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

class MarketResult:

	""" sent by server to respond to MarketCommand """

	def __init__(self):
		self.commmandID = 0
		self.message = ""
		self.error = False
		self.items = []

	def read(self, data):

		reader = PacketReader(data)
		self.commandID = reader.ReadByte()

		if self.commandID == 0:
			return

		elif self.commandID == 1:
			self.message = reader.ReadString()
			self.error = self.commandID == 0

		elif self.commandID == 2:
			self.numItems = reader.ReadInt()
			for _ in range(self.numItems):
				p = PlayerShopItem()
				p.parseFromInput(reader)
				self.items.append(p)

	def PrintString(self):
		print("commandID", self.commandID, "message", self.message, "error", self.error)
		if len(self.items) == 0:
			print("no items")
			return
		else:
			for i in range(len(self.items)):
				print("item {}".format(i))
				self.items[i].PrintString()


class CheckCredits:

	def __init__(self):
		pass

	def read(self, data):
		pass
	
	def write(self, writer):
		pass

class EditAccountList:

	def __init__(self):
		self.accountListID = 0
		self.add = False
		self.objectID = 0

	def read(self, data):
		reader = PacketReader(data)
		self.accountListID = reader.ReadInt()
		self.add = reader.ReadBoolean()
		self.objectID = reader.ReadInt()

	def write(self, writer):
		writer.WriteInt(self.accountListID)
		writer.WriteBoolean(self.add)
		writer.WriteInt(self.objectID)
		#writer.WriteHeader(PacketTypes.EditAccountList)

	def PrintString(self):
		print(
			"accountListID:", self.accountListID, "add", self.add, "objectID", self.objectID
		)

class ChangeGuildRank:

	"""

	Sent by client when player changes the rank of someone in the guild.

	initiate : rank 0
	member : rank 10
	officer : 20
	leader : 30
	"""

	def __init__(self):
		self.name = ""
		self.guildRank = 0

	def read(self, data):
		reader = PacketReader(data)
		self.name = reader.ReadString()
		self.guildRank = reader.ReadInt()

	def write(self, writer):
		writer.WriteString(self.name)
		writer.WriteInt(self.guildRank)
		#writer.WriteHeader(PacketTypes.ChangeGuildRank)

	def PrintString(self):
		print("name", self.name, "rank", self.guildRank)

class PlayerText:

	"""
	Sent by client when player types a message in chat
	"""

	def __init__(self):
		self.text = ""

	def read(self, data):
		reader = PacketReader(data)
		self.text = reader.ReadString()

	def write(self, writer):
		writer.WriteString(self.text)
		#writer.WriteHeader(PacketTypes.PlayerText)

	def PrintString(self):
		print("text", self.text)



class Escape:

	"""
	Unknown.
	"""

	def __init__(self):
		pass

	def read(self, data):
		pass

	def write(self, writer):
		pass
		#writer.WriteHeader(PacketTypes.Escape)

class SetCondition:

	"""
	Unknown. Auto-DCs on valor.
	"""

	def __init__(self):
		# byte
		self.conditionEffect = 0
		# float
		self.conditionDuration = 0

	def read(self, data):
		reader = PacketReader(data)
		self.conditionEffect = reader.ReadByte()
		self.conditionDuration = reader.ReadFloat()

	def write(self, writer):
		print(writer.buffer)
		writer.WriteByte(self.conditionEffect)
		print(writer.buffer)
		writer.WriteFloat(self.conditionDuration)
		print(writer.buffer)

	def PrintString(self):
		print("conditionDurationnditionEffect", self.conditionEffect, "conditionDuration", self.conditionDuration)

class PlayerHit:

	"""
	Sent by client when player is hit by a bullet.

	bulletID - stands for nth bullet enemy shot
	"""

	def __init__(self):
		self.bulletID = 0
		self.objectID = 0

	def read(self, data):
		reader = PacketReader(data)
		self.bulletID = reader.ReadByte()
		self.objectID = reader.ReadInt()

	def write(self, writer):
		writer.WriteByte(self.bulletID)
		writer.WriteInt(self.objectID)

	def PrintString(self):
		print("bulletID", self.bulletID, "objectID", self.objectID)

class GoToQuestRoom:

	"""
	Sent by client. Unknown purpose tho
	"""

	def __init__(self):
		pass

	def write(self, writer):
		pass

	def read(self, data):
		pass

class LaunchRaid:

	def __init__(self):
		self.raidID = 0
		self.ultra = 0

	def read(self, data):
		reader = PacketReader(data)
		self.raidID = reader.ReadInt()
		self.ultra = reader.ReadBoolean()

	def write(self, writer):
		writer.WriteInt(self.raidID)
		writer.WriteBoolean(self.ultra)

class UnboxRequest:

	"""
	Sent by client when player requests to unbox a lootbox.
	"""

	def __init__(self):
		self.lootboxType = 0

	def read(self, data):
		reader = PacketReader(data)
		self.lootboxType = reader.ReadInt()

	def write(self, writer):
		writer.WriteInt(self.lootboxType)

class Create:
	"""
	Sent by client to create a new character
	"""

	def __init__(self):
		self.classType = 0
		self.skinType = 0

	def read(self, data):
		reader = PacketReader(data)
		self.classType = reader.ReadShort()
		self.skinType = reader.ReadShort()

	def write(self, writer):
		writer.WriteShort(self.classType)
		writer.WriteShort(self.skinType)

	def PrintString(self):
		print("classType", self.classType, "skinType", self.skinType)

class RequestGamble:

	def __init__(self):
		self.name = ""
		self.amount = 0

	def write(self, writer):
		writer.WriteString(self.name)
		writer.WriteInt(self.amount)

class MarkRequest:

	def __init__(self):
		self.id = 0

	def write(self, writer):
		writer.WriteInt(self.id)

class PotionStorageInteraction:

	"""
	type
	0 - life

	action
	0 - deposit
	1 - withdraw
	"""

	def __init__(self):
		self.type = 0
		self.action = 0

	def write(self, writer):
		writer.WriteByte(self.type)
		writer.WriteByte(self.action)

class QoLAction:

	"""
	1: construct sor crystal w 50 fragments
	"""

	def __init__(self):
		self.action = 0

	def write(self, writer):
		writer.WriteInt(self.action)

class Reskin:
	"""
	you can send these packets, but if you don't have the skin, then does not work
	"""

	def __init__(self):
		self.skinID = 0

	def write(self, writer):
		writer.WriteInt(self.skinID)

class ReskinUnlock:

	def __init__(self):
		self.skinID = 0

	def write(self, writer):
		writer.WriteInt(self.skinID)


class WorldPosData:

	"""x and y coords, floats"""

	def __init__(self):
		self.x = 0
		self.y = 0

	def parseCoords(self, reader):
		"""
		data is the packet buffer
		"""
		self.x = reader.ReadFloat()
		self.y = reader.ReadFloat()

	def write(self, writer):

		writer.WriteFloat(self.x)
		writer.WriteFloat(self.y)

	def PrintString(self):
		print("x:", self.x, "y:", self.y)

class Failure:

	""" sent by server to indicate some type of failure """

	def __init__(self):
		self.errorID = 0
		self.errorDescription = ""

	def read(self, data):
		reader = PacketReader(data)
		self.errorID = reader.ReadInt()
		self.errorDescription = reader.ReadString()

	def write(self, writer):
		writer.WriteInt(self.errorID)
		writer.WriteString(self.errorDescription)

	def PrintString(self):
		print("errorID", self.errorID, "errorDescription", self.errorDescription)

class ChooseName:

	""" sent by client to choose a name """

	def __init__(self):
		self.name = ""

	def read(self, data):
		reader = PacketReader(data)
		self.name = reader.ReadString()

	def write(self, writer):
		writer.WriteString(self.name)

class QuestObjId:

	""" sent by server to display latest quest on map """

	def __init__(self):
		self.objectID = 0

	def read(self, data):
		reader = PacketReader(data)
		self.objectID = reader.ReadInt()

	def write(self, writer):
		writer.WriteInt(self.objectID)

class Teleport:

	""" sent by client to teleport to a certain object ID """

	def __init__(self):
		self.objectID = 0

	def read(self, data):
		reader = PacketReader(data)
		self.objectID = reader.ReadInt()

	def write(self, writer):
		writer.WriteInt(self.objectID)

class RequestTrade:

	def __init__(self):
		self.name = ""

	def read(self, data):
		reader = PacketReader(data)
		self.name = reader.ReadString()

	def write(self, writer):
		writer.WriteString(self.name)


class Text:

	""" sent by server to display a message sent from the server """

	def __init__(self):
		self.name = ""
		self.objectID = 0
		self.numStars = 0
		self.admin = 0
		self.bubbleTime = 0
		self.recipient = ""
		self.text = ""
		self.cleanText = ""
		self.nameColor = 0
		self.textColor = 0

	def read(self, data):
		reader = PacketReader(data)
		self.name = reader.ReadString()
		self.objectID = reader.ReadInt()
		self.numStars = reader.ReadInt()
		self.admin = reader.ReadInt()
		self.bubbleTime = reader.ReadByte()
		self.recipient = reader.ReadString()
		self.text = reader.ReadString()
		self.cleanText = reader.ReadString()
		self.nameColor = reader.ReadInt()
		self.textColor = reader.ReadInt()

	def write(self, writer):
		writer.WriteString(self.name)
		writer.WriteInt(self.objectID)
		writer.WriteInt(self.numStars)
		writer.WriteInt(self.admin)
		writer.WriteByte(self.bubbleTime)
		writer.WriteString(self.recipient)
		writer.WriteString(self.text)
		writer.WriteString(self.cleanText)
		writer.WriteInt(self.nameColor)
		writer.WriteInt(self.textColor)

	def PrintString(self):
		print(
			"name", self.name, "objectID", self.objectID, "numStars", self.numStars, "admin", self.admin,
			"bubbleTime", self.bubbleTime, "recipient", self.recipient, "text", self.text, "cleanText", self.cleanText,
			"nameColor", self.nameColor, "textColor", self.textColor
		)

class StatData:

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

	def __init__(self):
		self.objectID = 0
		self.pos = WorldPosData()
		self.stats = [] # statdata objects

	def parse(self, reader): 
		self.objectID = reader.ReadInt()
		self.pos.parseCoords(reader)

		# num statdata objects
		length = reader.ReadShort()
		#print(length, "statdatas")
		for _ in range(length):
			s = StatData()
			s.parse(reader)
			self.stats.append(s)
			#s.PrintString()

		#print("new objstatusdata parsed")


	def write(self, writer):
		writer.WriteInt(self.objectID)
		self.pos.write(writer)
		writer.WriteShort(len(self.stats))
		for s in self.stats:
			s.write(writer)
		
	def PrintString(self):
		print("objid", self.objectID, "pos", self.pos.x, self.pos.y, "len stat", len(self.stats))

class ShowEffect:

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

class NewTick:

	"""
	Sent by server to
	- Update locations of other players, enemies, or certain objects like portals
	- Inform client of statdatas for each player, enemy, etc.
	- Update rotating objects (such as marketplace items)
	- Tell the client where the server thinks you are
	- Tell the client stats about yourself:
		- total fame on account
		- total gold on account
		- fortune_token_stat ? 
		- total onrane on account
		- total kantos
		- total trial tokens
		- hp
		- prot, etc.

	"""

	def __init__(self):
		self.tickID = 0
		self.tickTime = 0
		self.statuses = [] #objectstatus data objects

	def read(self, data):
		reader = PacketReader(data)
		self.tickID = reader.ReadInt()
		self.tickTime = reader.ReadInt()

		# num statuses 
		length = reader.ReadShort()
		#print(length, "objects")
		# bunch of ObjectStatusData objects
		for _ in range(length):
			#print("parsing new objstatusdata")
			o = ObjectStatusData()
			o.parse(reader)
			self.statuses.append(o)
			#o.PrintString()

	def write(self, writer):
		writer.WriteInt(self.tickID)
		writer.WriteInt(self.tickTime)
		writer.WriteShort(len(self.statuses))
		for o in self.statuses:
			o.write(writer)

	def PrintString(self):
		print("tickid", self.tickID, "ticktime", self.tickTime, "len statuses / num objs", len(self.statuses))

class Death:

	def __init__(self):
		self.accountID = ""
		self.charID = 0
		self.killedBy = ""
		self.zombieID = 0
		self.zombieType = 0
		self.isZombie = False
	
	def read(self, data):
		reader = PacketReader(data)
		self.accountID = reader.ReadString()
		self.charID = reader.ReadInt()
		self.killedBy = reader.ReadString()
		self.zombieType = reader.ReadInt()
		self.zombieID = reader.ReadInt()

	def write(self, writer):
		writer.WriteString(self.accountID)
		writer.WriteInt(self.charID)
		writer.WriteString(self.killedBy)
		writer.WriteInt(self.zombieType)
		writer.WriteInt(self.zombieID)

	def PrintString(self):
		print("Death", time.time(), "accountID", self.accountID, "charID", self.charID, "killedBy", self.killedBy)
