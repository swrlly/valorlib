from ..PacketReader import PacketReader

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