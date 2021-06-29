from ..PacketReader import PacketReader

class AccountList:

	"""
	sent by server to tell you what accounts you've locked and ignored
	accountlistID: 0 is locked, 1 is ignored
	"""

	def __init__(self):
		self.accountListID = 0
		self.numAccounts = 0
		self.accountList = []
		self.lockAction = 0

	def read(self, data):
		reader = PacketReader(data)
		self.accountListID = reader.ReadInt()
		self.numAccounts = reader.ReadShort()
		self.accountList = [reader.ReadString() for _ in range(self.numAccounts)]
		self.lockAction = reader.ReadInt()

	def PrintString(self):
		print("accountListID", self.accountListID, "numAccounts", self.numAccounts, "accountList", self.accountList, "lock", self.lockAction)
