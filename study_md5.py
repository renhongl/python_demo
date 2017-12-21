

# coding: utf-8

import hashlib

class User_Collection(object):

	def __init__(self):
		self._db = {}
		self._md5 = hashlib.md5()

	def register(self, user_name, password):
		print('register md5:' + self.get_md5(password));
		if not hasattr(self._db, user_name):
			self._db[user_name] = self.get_md5(password)
		else:
			print('This user have registered, please change a user name.')

	def get_md5(self, password):
		md5 = hashlib.md5()
		md5.update(password.encode('utf-8'))
		return md5.hexdigest()

	def getDB(self):
		return str(self._db)

	def login(self, user_name, password):
		print('login md5:' + self.get_md5(password))
		if self._db[user_name] == self.get_md5(password):
			print('You have login successfully')
		else:
			print('Your user name or password is wroung')



user_collection = User_Collection()

user_collection.register('renhongl', 'lrh0000')

user_collection.login('renhongl', 'lrh0000')