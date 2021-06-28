from ..PacketReader import PacketReader

class BuyResult:

	""" sent by server to inform client what happened after sending Buy packet """

	def __init__(self):
		self.result = 0
		self.resultString = ""

	def read(self, data):
		reader = PacketReader(data)
		self.result = reader.ReadInt()
		self.resultString = reader.ReadString()

	def PrintString(self):
		print("result", self.result, "resultString", self.resultString)