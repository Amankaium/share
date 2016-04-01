#coding: utf-8
import sys

class House:
	def __init__(self, x):
		self.walls = x
		print "\nВ доме %s стен\n" % self.walls
	def houseOnFire (self):
		self.walls-=1
		if self.walls==0:
			sys.exit("\nДом сгорел!\n") 
		else:
			print "\nДом горит, в доме осталось %s стен \n" % self.walls

class Cat:
	def catsInHouse(self, y):
		self.day = y
		print "\nДень %sй\n" % self.day
		c = int(input("Сколько кошек в доме?\n"))
		if c == 0:
			house.houseOnFire()
		elif c < 0:
			print "Вводите НЕотрицательное число!\n"

h = int (input("Сколько стен?\n"))
house = House(h)
d=0
cat = Cat()
while house.walls > 0:
	d+=1;
	cat.catsInHouse(d)



	





