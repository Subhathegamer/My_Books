###Sourse : Python crash course(2nd edition) by Eric Matthes###
##cp6's 8th excrcise
pet_1 = {'pet':'cat',
				             'owner':'akash',
				             				}
pet_2 = {'pet':'dog',
				             'owner':'harsh',
				             				}
pets = []
pets.append(pet_1)
pets.append(pet_2)
for pet in pets:
				  print(f"This is a {pet['pet']}.\nHis owner is {pet['owner']}\n")



