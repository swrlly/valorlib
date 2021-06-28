from ..PacketReader import PacketReader

class Reconnect:

	"""
	Sent by the server to inform the client of the data used in the next map entry's handshake.
	"""

	def __init__(self):
		self.name = ""
		self.host = ""
		self.port = 0
		self.gameID = 0
		self.keyTime = 0
		self.key = bytearray()
		self.isFromArena = False

	def read(self, data):
		reader = PacketReader(data)
		self.name = reader.ReadString()
		self.host = reader.ReadString()
		self.port = reader.ReadInt()
		self.gameID = reader.ReadInt()
		self.keyTime = reader.ReadInt()
		self.isFromArena = reader.ReadBoolean()

		length = reader.ReadShort()
		self.key = [reader.ReadByte() for _ in range(length)]

	def write(self, writer):
		writer.WriteString(self.name)
		writer.WriteString(self.host)
		writer.WriteInt(self.port)
		writer.WriteInt(self.gameID)
		writer.WriteInt(self.keyTime)
		writer.WriteBoolean(self.isFromArena)
		writer.WriteShort(len(self.key))
		for byte in self.key:
			writer.WriteByte(byte)

	def PrintString(self):
		print(
			"name:", self.name, "host", self.host, "port", self.port, "gameID", self.gameID,
			"keyTime", self.keyTime, "key", self.key, "isFromArena", self.isFromArena
		)