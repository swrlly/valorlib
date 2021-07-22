from ..PacketReader import PacketReader

class Hello:
	
	"""
	Sent by client to initiate the handshake to enter a new instance
	"""

	def __init__(self):
		self.buildVersion = ""
		self.gameID = 0
		self.guid = ""
		self.loginToken = ""
		self.keyTime = 0
		self.key = bytearray()
		self.mapJSON = ""
		self.cliBytes = 0

	def read(self, data):
		reader = PacketReader(data)
		self.buildVersion = reader.ReadString()
		self.gameID = reader.ReadInt()
		self.guid = reader.ReadString()
		self.loginToken = reader.ReadString()
		self.keyTime = reader.ReadInt()
		length = reader.ReadShort()
		self.key = [reader.ReadByte() for _ in range(length)]
		lengthJSON = reader.ReadInt()
		self.mapJSON = reader.ReadStringBytes(lengthJSON)
		self.cliBytes = reader.ReadInt()

	def write(self, writer):
		writer.WriteString(self.buildVersion)
		writer.WriteInt(self.gameID)
		writer.WriteString(self.guid)
		writer.WriteString(self.loginToken)
		writer.WriteInt(self.keyTime)
		writer.WriteShort(len(self.key))
		for byte in self.key:
			writer.WriteByte(byte)
		writer.WriteInt(len(self.mapJSON))
		writer.WriteStringBytes(self.mapJSON)
		writer.WriteInt(self.cliBytes)

	def PrintString(self):
		print("buildVersion", self.buildVersion, "gameID", self.gameID, "loginToken", self.loginToken,
			"keyTime", self.keyTime, "key", self.key, "mapJSON", self.mapJSON, "cliBytes", self.cliBytes)
