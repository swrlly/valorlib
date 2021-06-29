from ..PacketReader import PacketReader

class QoLAction:

	"""
	1: construct sor crystal w 50 fragments
	"""

	def __init__(self):
		self.action = 0

	def write(self, writer):
		writer.WriteInt(self.action)