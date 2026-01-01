###Sourse : Python crash course(2nd edition) by Eric Matthes###
##cp11's 1st&2nd excrcise

#python library's module
import unittest
#own module
from city_country import city_country

class TestCityCountry(unittest.TestCase):
				"""Tests the city_country function if it works"""
				
				def test_city_country(self):
								"""tests the citycountry"""
								citycountry = city_country("kolkata", "india")
								self.assertEqual(citycountry, "Kolkata, India")
				
				def test_city_country_population(self):
								"""Tests the citycountry with population"""
								citycountry = city_country("kolkata","india",20500000)
								self.assertEqual(citycountry, "Kolkata, India - population 20500000")



if __name__ == "__main__":
				unittest.main()