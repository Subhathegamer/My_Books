###Sourse : Python crash course(2nd edition) by Eric Matthes###
##cp9's 1st&2nd&4th&6th excrcise


class Restaurant:
				"""Make a instence called Restaurent."""
				
				def __init__(self,restaurant_name):
								# I didn't know the meaning of cuisine_type.So I didn't write it .
				    """Initialize name attribute."""
				    self.name = restaurant_name.title()
				    self.served = 19
				
				
				def number_served(self):
								"""Prints how many castomers were served."""
								print(f"The restaurant {self.name} served {self.served} customer.")
								
								
				def set_number_served(self,number):
								"""Set the number that how many people were served."""
								if number > self.served:
												self.served = number
								else:
												print(f"\n  !!!Please Give a Correct Number!!!")
								
				
				def increment_number_served(self,number):
								"""Add the number of served customers."""
								self.served += number
				
								
				def describe_restaurant(self):
								
				    """Describe the restaurant"""
				    print(f"This restaurant's name is {self.name}.")
				
				
				def open_restaurant(self):
								"""Simulates opening restaurent."""
								print(f"The restaurant named {self.name} is open.")




class IceCreamStand(Restaurant):
				"""Makes a instence called IceCreamStand"""
				
				
				def __init__(self,restaurant_name):
								"""Sets the attributes"""
								super().__init__(restaurant_name)
								self.flavors = []
				
				
				def add_flavors(self,flavor):
								"""adds a function to add flavors easily."""
								self.flavors.append(flavor)
				
				
				def show_flavors(self):
								"""Shows the flavors"""
								if self.flavors:
												print(f"\nThe Icecreamstand named {self.name} have these flavors:")
												for flavor in self.flavors:
																print(f"\t\t-{flavor}")
								else:
												print(f"\nThe Icecreamstand named {self.name} has no flavors!")
				
				


				









