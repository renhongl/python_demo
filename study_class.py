

# utf-8



# class Screen(object):
	
# 	def print(self):
# 		print(str(self.width) + '/' + str(self.height))

# screen = Screen()

# screen.width = 100
# screen.height = 200
# screen.print()



# class Screen(object):

# 	def __init__(self, width, height):
# 		self._width = width
# 		self._height = height

# 	def getWidth(self):
# 		return self._width

# 	def setWidth(self, width):
# 		self._width = width

# 	def getHeight(self):
# 		return self._height

# 	def setHeight(self, height):
# 		self._height = height

# 	def getResolution(self):
# 		print(str(self._width) + '/' + str(self._height))



# screen = Screen(200, 400)
# screen.getResolution()

# screen.setHeight(700)
# screen.getResolution()
# print(screen.getWidth())




class Screen(object):

	def __init__(self):
		self._width = 0;
		self._height = 0

	@property
	def width(self):
		return self._width

	@width.setter
	def width(self, width):
		if not isinstance(width, int):
			print('width not a number')
			self._width = 0
		else:
			self._width = width

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self, height):
		if not isinstance(height, int):
			print('height not a number')
			self._height = 0
		else:
			self._height = height

	def getResolution(self):
		print(str(self._width) + '/' + str(self._height))


screen = Screen()
screen.width = 100;
screen.getResolution()