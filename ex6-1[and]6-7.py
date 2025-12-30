###Sourse : Python crash course(2nd edition) by Eric Matthes###
##cp6's 7th excrcise
#dictonary of some people
people_1 = {'first_name':'rahul',
				           'last_name':'roy',
				           				'location':'kolkata',
				           								'age':25,        
				           								         }

people_2 = {'first_name':'sahil',
				           'last_name':'das',
				           				'location':'burdwan',
				           								'age':29,
				           										'relation':'he is my friend',		           
				           								           }

people_3 = {'first_name':'rahul',
				           'last_name':'roy',
				           				'location':'kolkata',
				           						'age':27				           										           
				           								           }

#list to store all people name
many_people = []
many_people.append(people_1)
many_people.append(people_2)
many_people.append(people_3)

#
for people in many_people:
				  print(f"{people['first_name'].title()} {people['last_name'].title()} lives in {people['location'].title()}.")
				  if 'relation' in people:
				  				   print(f"His age is {people['age']}")
				  				   print(f"{people['relation']}.\n")
				  else:
    				     print(f"His age is {people['age']}\n")



