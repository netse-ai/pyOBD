class ELM327Error(Exception):
	def __init__(self, value):
		self.value = value
		Exception.__init__(self, value)

	def __str__(self):
		print self.value