from ..PacketReader import PacketReader

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