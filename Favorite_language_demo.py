###Sourse : Python crash course(2nd edition) by Eric Matthes###

##example of list in dictionary.
#List as a value in dictionary
fav_lang = {
    'sanil':['C','java'],
    				'rahil':['javascript','C#'],
    								'sanny':['C++','python'],
    												'rahul':['python','C'],
    																}

#prints a massage for telling each person's favorite language(s)
for name,languages in fav_lang.items():
				  print(f"\n{name.title()}'s favorite languages are:")
				  for language in languages:
				  				  print(f"{language.title()}")

