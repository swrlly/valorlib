from .PacketWriter import PacketWriter
from .PacketTypes import PacketTypes

from .incoming.__init__ import *
from .outgoing.__init__ import *

class Packet:

	def __init__(self, header, data, ID):
		self.header = header
		self.data = data
		self.ID = ID

	"""
	Converts a bytearray into the RotMG packet format. Unencrypted.
	"""
	def format(self):
		return self.header + self.data

"""
Create packet logic
"""
def CreatePacket(c) -> Packet:
	"""
	c : Instance of a particular PacketClass
	"""

	writer = PacketWriter()
	packetID = -1

	if isinstance(c, Hello):
		packetID = PacketTypes.Hello

	elif isinstance(c, EditAccountList):
		packetID = PacketTypes.EditAccountList
		
	elif isinstance(c, ChangeGuildRank):
		packetID = PacketTypes.ChangeGuildRank

	elif isinstance(c, Escape):
		packetID = PacketTypes.Escape

	elif isinstance(c, SetCondition):
		packetID = PacketTypes.SetCondition

	elif isinstance(c, PlayerHit):
		packetID = PacketTypes.PlayerHit

	elif isinstance(c, UnboxRequest):
		packetID = PacketTypes.UnboxRequest

	elif isinstance(c, Aoe):
		packetID = PacketTypes.Aoe

	elif isinstance(c, RequestGamble):
		packetID = PacketTypes.RequestGamble

	elif isinstance(c, MarkRequest):
		packetID = PacketTypes.MarkRequest

	elif isinstance(c, PotionStorageInteraction):
		packetID = PacketTypes.PotionStorageInteraction

	elif isinstance(c, PlayerText):
		packetID = PacketTypes.PlayerText

	elif isinstance(c, QoLAction):
		packetID = PacketTypes.QoLAction

	elif isinstance(c, Reskin):
		packetID = PacketTypes.Reskin

	elif isinstance(c, ReskinUnlock):
		packetID = PacketTypes.ReskinUnlock

	elif isinstance(c, NewTick):
		packetID = PacketTypes.NewTick

	elif isinstance(c, EnemyHit):
		packetID = PacketTypes.EnemyHit

	elif isinstance(c, PlayerShoot):
		packetID = PacketTypes.PlayerShoot

	elif isinstance(c, Create):
		packetID = PacketTypes.Create

	elif isinstance(c, GoToQuestRoom):
		packetID = PacketTypes.GoToQuestRoom

	elif isinstance(c, LaunchRaid):
		packetID = PacketTypes.LaunchRaid

	elif isinstance(c, UseItem):
		packetID = PacketTypes.UseItem

	elif isinstance(c, EnemyShoot):
		packetID = PacketTypes.EnemyShoot

	elif isinstance(c, GroundDamage):
		packetID = PacketTypes.GroundDamage

	elif isinstance(c, Failure):
		packetID = PacketTypes.Failure

	elif isinstance(c, ChooseName):
		packetID = PacketTypes.ChooseName

	elif isinstance(c, Text):
		packetID = PacketTypes.Text

	elif isinstance(c, QuestObjId):
		packetID = PacketTypes.QuestObjId

	elif isinstance(c, Teleport):
		packetID = PacketTypes.Teleport

	elif isinstance(c, InvResult):
		packetID = PacketTypes.InvResult

	elif isinstance(c, CheckCredits):
		packetID = PacketTypes.CheckCredits

	elif isinstance(c, Buy):
		packetID = PacketTypes.Buy

	elif isinstance(c, MarketCommand):
		packetID = PacketTypes.MarketCommand

	elif isinstance(c, MarketResult):
		packetID = PacketTypes.MarketResult

	elif isinstance(c, Ping):
		packetID = PacketTypes.Ping

	elif isinstance(c, Pong):
		packetID = PacketTypes.Pong

	elif isinstance(c, QueuePing):
		packetID = PacketTypes.QueuePing

	elif isinstance(c, QueuePong):
		packetID = PacketTypes.QueuePong

	elif isinstance(c, Load):
		packetID = PacketTypes.Load

	elif isinstance(c, UpdateAck):
		packetID = PacketTypes.UpdateAck

	elif isinstance(c, Move):
		packetID = PacketTypes.Move

	elif isinstance(c, Update):
		packetID = PacketTypes.Update

	elif isinstance(c, InvSwap):
		packetID = PacketTypes.InvSwap

	elif isinstance(c, InvDrop):
		packetID = PacketTypes.InvDrop

	elif isinstance(c, RenameItem):
		packetID = PacketTypes.RenameItem

	elif isinstance(c, RequestTrade):
		packetID = PacketTypes.RequestTrade

	elif isinstance(c, Reconnect):
		packetID = PacketTypes.Reconnect

	elif isinstance(c, ShowEffect):
		packetID = PacketTypes.ShowEffect

	elif isinstance(c, Death):
		packetID = PacketTypes.Death

	elif isinstance(c, GotoAck):
		packetID = PacketTypes.GotoAck

	elif isinstance(c, Goto):
		packetID = PacketTypes.Goto

	# write body of packet
	c.write(writer)
	# write the header
	writer.WriteHeader(packetID)

	#print("This is our unencrypted buffer:", writer.buffer)
	return Packet(writer.buffer[:5], writer.buffer[5:], packetID)