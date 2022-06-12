import struct

class PacketReader:

	def __init__(self, data):
		# start from the beginning, always assume no headers if you're starting to read
		self.index = 0
		self.buffer = data

	def BytesLeft(self):
		return len(self.buffer) - self.index

	def ReadByte(self):
		self.index += 1
		return self.buffer[self.index - 1]

	def ReadFloat(self):
		tmp = struct.unpack(">f", self.buffer[self.index : self.index + 4])[0]
		self.index += 4
		return tmp

	def ReadInt(self):
		tmp = struct.unpack(">i", self.buffer[self.index : self.index + 4])[0]
		self.index += 4
		return tmp

	def ReadUnsignedInt(self):
		tmp = struct.unpack(">I", self.buffer[self.index : self.index + 4])[0]
		self.index += 4
		return tmp
		
	def ReadBoolean(self):
		tmp = struct.unpack(">?", self.buffer[self.index : self.index + 1])[0]
		self.index += 1
		return tmp

	def ReadShort(self):
		tmp = struct.unpack(">h", self.buffer[self.index : self.index + 2])[0]
		self.index += 2
		return tmp

	def ReadUnsignedShort(self):
		tmp = struct.unpack(">H", self.buffer[self.index : self.index + 2])[0]
		self.index += 2
		return tmp

	# from the docs: Reads a UTF-8 string from the file stream, byte stream, or byte array. The string is assumed to be prefixed with an unsigned short indicating the length in bytes. 
	def ReadString(self):
		length = self.ReadShort()
		return self.ReadStringBytes(length)

	# this string has a length that is not a unsigned short.
	def ReadStringBytes(self, length):
		tmp = struct.unpack(">{}s".format(length), self.buffer[self.index : self.index + length])[0].decode()
		self.index += length
		return tmp

