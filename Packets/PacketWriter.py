import struct

class PacketWriter:

	def __init__(self):
		self.buffer = bytearray()

	def WriteByte(self, data):
		self.buffer += struct.pack(">B", data)

	def WriteInt(self, data):
		self.buffer += struct.pack(">i", data)

	def WriteUnsignedInt(self, data):
		self.buffer += struct.pack(">I", data)

	def WriteShort(self, data):
		self.buffer += struct.pack(">h", data)

	def WriteUnsignedShort(self, data):
		self.buffer += struct.pack(">H", data)

	def WriteBoolean(self, data):
		self.buffer += struct.pack(">?", data)

	def WriteFloat(self, data):
		self.buffer += struct.pack(">f", data)

	def WriteString(self, data):
		# sanitize data against unicode
		self.WriteShort(len(data))
		if type(data) == str:
			self.buffer += struct.pack(">{}s".format(len(data)), bytearray([ord(x) if 0 <= ord(x) <= 255 else 32 for x in data]))
		else:
			self.buffer += struct.pack(">{}s".format(len(data)), data)

	def WriteStringBytes(self, data):
		# sanitize data against unicode
		if type(data) == str:
			self.buffer += struct.pack(">{}s".format(len(data)), bytearray([ord(x) if 0 <= ord(x) <= 255 else 32 for x in data]))
		else:
			self.buffer += struct.pack(">{}s".format(len(data)), data)

	def WriteHeader(self, id):
		self.buffer = bytearray(struct.pack(">i", len(self.buffer) + 5)) + self.buffer
		self.buffer.insert(4, id)
