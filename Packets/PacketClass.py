from .DataStructures import *

import time

from .PacketReader import PacketReader

class InvResult:

	""" sent by server to inform the client on success after invswap / invdrop """

	def __init__(self):
		self.result = 0

	def read(self, data):
		reader = PacketReader(data)
		self.result = reader.ReadInt()

	def write(self, writer):
		writer.WriteInt(self.result)

	def PrintString(self):
		print("result:", self.result)

class GotoAck:

	def __init__(self):
		self.time = 0

	def read(self, data):
		reader = PacketReader(data)
		self.time = reader.ReadInt()

	def write(self, writer):
		writer.WriteInt(self.time)

	def PrintString(self):
		print("time", self.time)

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

class PlayerShoot():

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
		self.numShots = 1
		self.angleInc = 0

	def read(self, data):
		reader = PacketReader(data)
		self.bulletID = reader.ReadByte()
		self.ownerID = reader.ReadInt()
		self.bulletType = reader.ReadByte()
		self.pos.parseCoords(reader)
		self.angle = reader.ReadFloat()
		self.damage = reader.ReadShort()
		if reader.BytesLeft() > 0:
			self.numShots = reader.ReadByte()
			self.angleInc = reader.ReadFloat()
		else:
			self.numShots = 1
			self.angleInc = 0

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

	""" Sent by server when the player first loads in into a new instance """

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

	""" Sent by client to buy an item from the marketplace """

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

class Goto:

	""" Sent by server to inform which objectID will teleport to a new location """

	def __init__(self):
		self.objectID = 0
		self.pos = WorldPosData()

	def read(self, data):
		reader = PacketReader(data)
		self.objectID = reader.ReadInt()
		self.pos.parseCoords(reader)

	def write(self, writer):
		writer.WriteInt(self.objectID)
		self.pos.write(writer)

	def PrintString(self):
		self.pos.PrintString()
		print("objectID", self.objectID)	

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

	def PrintString(self):
		print("text", self.text)



class Escape:

	"""
	Unused packet in pservers. For prod, it's to prompt server for a Reconnect packet for the Nexus
	"""

	def __init__(self):
		pass

	def read(self, data):
		pass

	def write(self, writer):
		pass

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

	"""
	Sent by client to launch a raid.
	"""

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

	"""
	Sent by client to request a gamble with another person.
	"""

	def __init__(self):
		self.name = ""
		self.amount = 0

	def write(self, writer):
		writer.WriteString(self.name)
		writer.WriteInt(self.amount)

class MarkRequest:

	"""
	Sent by user to request activating a mark
	"""

	def __init__(self):
		self.id = 0

	def write(self, writer):
		writer.WriteInt(self.id)

class PotionStorageInteraction:

	"""
	type
	0 - life
	1 - mana
	2 - lexiographic order in the pot UI.

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

	""" sent by client to request a trade with a player """

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
		self.statuses = [] 

	def read(self, data):
		reader = PacketReader(data)
		self.tickID = reader.ReadInt()
		self.tickTime = reader.ReadInt()
		length = reader.ReadShort()
		for _ in range(length):
			o = ObjectStatusData()
			o.parse(reader)
			self.statuses.append(o)

	def write(self, writer):
		writer.WriteInt(self.tickID)
		writer.WriteInt(self.tickTime)
		writer.WriteShort(len(self.statuses))
		for o in self.statuses:
			o.write(writer)

	def PrintString(self):
		print("tickid", self.tickID, "ticktime", self.tickTime, "len statuses / num objs", len(self.statuses))

class Death:

	"""
	Sent by server to inform client that you have died.
	"""

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
