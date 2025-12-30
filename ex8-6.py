###Sourse : Python crash course(2nd edition) by Eric Matthes###
##cp8's 6th excrcise

def city_country(city,country):
				"""Returns a string of a city and its country."""
				city_describe = f'"{city}, {country}"'
				return city_describe
massage = city_country(country='INDIA',city='Burdwan')
print(massage)

massage = city_country(country='INDIA',city='Kolkata')
print(massage)

massage = city_country(country='INDIA',city='New Delhi')
print(massage)

