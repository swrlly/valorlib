from ..PacketReader import PacketReader

class UpdateAck:

	""" 
	sent by the client to acknowledge receiving an update packet
	dc's after 30 seconds if you do not ack
	dc's immediately on prod if you don't ack
	"""

	def __init__(self):
		pass

	def read(self, data):
		pass
	
	def write(self, writer):
		pass