from ..PacketReader import PacketReader

class ReskinUnlock:

	""" sent by server to unlock a skin """

	def __init__(self):
		self.skinID = 0

	def write(self, writer):
		writer.WriteInt(self.skinID)