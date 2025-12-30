###Sourse : Python crash course(2nd edition) by Eric Matthes###
##cp9's 13th excrcise
from random import randint

class Dice:
				"""Makes a object called dice"""
				
				
				def __init__(self,sides=6):
								"""init function"""
								self.sides = sides
				
				
				def roll_dice(self):
								"""rolls the dice with the help of module random"""
								print(randint(1,self.sides))
								
				
				def set_sides(self,sides):
								"""sets the number of sides"""
								self.sides = sides
								


#raw data to test code 
my_dice = Dice()
for times in range(10):
				my_dice.roll_dice()
print("")
my_dice.set_sides(10)
for times in range(10):
				my_dice.roll_dice()
print("")
my_dice.set_sides(20)
for times in range(10):
				my_dice.roll_dice()
