###Sourse : Python crash course(2nd edition) by Eric Matthes###
##cp11's 1st excrcise(other module = ex11_1.py)

def city_country(city, country,population=""):
				"""write a small sentence about a city."""
				if population:
								sentence = f"{city.title()}, {country.title()} - population {population}"
				else:
								sentence = f"{city.title()}, {country.title()}"
				return sentence



