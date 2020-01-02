
class Name:
	__slots__ = 'value'
	def __init__(self, value):
		if not isinstance(value, str):
			raise TypeError('value argument must be type of: {} instead of: {}'.format('str', type(value).__name__))
		self.value = value

	def __str__(self):
		return "Name({!r}".format(self.value)

class Function:
	__slots__ = 'name', 'args', 'return_type', 'body'
	def __init__(self, name, args, body, return_type = None):
		self.name = Name(name)
		self.args = args
		self.body = body
		self.return_type = return_type

	def __str__(self):
		return "Function(name={}, args={}, return_type={}, body={})".format(
			self.name, self.args, self.return_type, self.body)

class Class:
	__slots__ = 'name', 'parents', 'body'
	def __init__(self, name, parents, body):
		self.name = Name(name)
		self.parents = parents
		self.body

	def __str__(self):
		return "Class(name={}, parents={}, body={})".format(self.name, self.parents, self.body)

class If:
	__slots__ = 'test', 'body'
	def __init__(self, test, body):
		self.test = test
		self.body = body

	def __str__(self):
		return "If(test={}, body={})".format(self.test, self.body)

class While:
	__slots__ = 'test', 'body'
	def __init__(self, test, body):
		self.test = test
		self.body = body

	def __str__(self):
		return "While(test={}, body={})".format(self.test, self.body)

class For:
	__slots__ = 'name', 'iterable', 'body'
	def __init__(self, name, iterable, body):
		self.name = name
		self.iterable = iterable
		self.body = body

	def __str__(self):
		return "For(name={}, iterable={}, body={})".format(self.name, self.iterable, self.body)
