from ..PacketReader import PacketReader

class MarketCommand:

	"""
	sent by client to perform certain market actions 
	"""

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