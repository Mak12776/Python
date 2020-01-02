
class Function:
	__slots__ = 'name', 'static', 'inline'
	def __init__(self, name, storage):
		self.name = name
		self.static = 

	def __str__(self):
		return "Function()"

class Struct:
	__slots__ = 'name'
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return "Struct()"

class TypeDef:
	__slots__ = 'name', 'type'
	def __init__(self, name, type):
		self.name = name
		self.type = type

	def __str__(self):
		return "TypeDef({}, {})".format(self.name, self.type)

class VarDecl:
	__slots__ = 'name', 'type', 'value'
	def __init__(self, name, type, value = None):
		self.name = name
		self.type = type
		self.value = value

	def __str__(self):
		return "ValDecl({}, {}, {})".format(self.name, self.type, self.value)
