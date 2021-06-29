from ..PacketReader import PacketReader

class MarkRequest:

	"""
	Sent by user to request activating a mark
	"""

	def __init__(self):
		self.id = 0

	def write(self, writer):
		writer.WriteInt(self.id)