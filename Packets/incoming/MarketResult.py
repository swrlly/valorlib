from ..PacketReader import PacketReader
from ..DataStructures import PlayerShopItem

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