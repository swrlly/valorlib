from ..PacketReader import PacketReader

class Text:

	""" sent by server to display a message sent from the server """

	def __init__(self):
		self.name = ""
		self.objectID = 0
		self.numStars = 0
		self.admin = 0
		self.bubbleTime = 0
		self.recipient = ""
		self.text = ""
		self.cleanText = ""
		self.nameColor = 0
		self.textColor = 0

	def read(self, data):
		reader = PacketReader(data)
		self.name = reader.ReadString()
		self.objectID = reader.ReadInt()
		self.numStars = reader.ReadInt()
		self.admin = reader.ReadInt()
		self.bubbleTime = reader.ReadByte()
		self.recipient = reader.ReadString()
		self.text = reader.ReadString()
		self.cleanText = reader.ReadString()
		self.nameColor = reader.ReadInt()
		self.textColor = reader.ReadInt()

	def write(self, writer):
		writer.WriteString(self.name)
		writer.WriteInt(self.objectID)
		writer.WriteInt(self.numStars)
		writer.WriteInt(self.admin)
		writer.WriteByte(self.bubbleTime)
		writer.WriteString(self.recipient)
		writer.WriteString(self.text)
		writer.WriteString(self.cleanText)
		writer.WriteInt(self.nameColor)
		writer.WriteInt(self.textColor)

	def PrintString(self):
		print(
			"name", self.name, "objectID", self.objectID, "numStars", self.numStars, "admin", self.admin,
			"bubbleTime", self.bubbleTime, "recipient", self.recipient, "text", self.text, "cleanText", self.cleanText,
			"nameColor", self.nameColor, "textColor", self.textColor
		)