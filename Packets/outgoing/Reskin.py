from ..PacketReader import PacketReader

class Reskin:

	"""
	you can send these packets, but if you don't have the skin, then does not work
	"""

	def __init__(self):
		self.skinID = 0

	def write(self, writer):
		writer.WriteInt(self.skinID)