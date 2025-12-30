###Sourse : Python crash course(2nd edition) by Eric Matthes###
##cp9's 1st&2nd&4th&6th excrcise


class Restaurent:
				"""Make a instence called Restaurent."""
				
				def __init__(self,restaurent_name):
								# I didn't know the meaning of cuisine_type.So I didn't write it .
				    """Initialize name attribute."""
				    self.name = restaurent_name.title()
				    self.served = 19
				
				
				def number_served(self):
								"""Prints how many castomers were served."""
								print(f"The restaurent {self.name} served {self.served} customer.")
								
								
				def set_number_served(self,number):
								"""Set the number that how many people were served."""
								if number > self.served:
												self.served = number
								else:
												print(f"\n  !!!Please Give a Correct Number!!!")
								
				
				def increment_number_served(self,number):
								"""Add the number of served customers."""
								self.served += number
				
								
				def describe_restaurent(self):
								
				    """Describe the restaurent"""
				    print(f"This restaurent's name is {self.name}.")
				
				
				def open_restaurent(self):
								"""Simulates opening restaurent."""
								print(f"The restaurent named {self.name} is open.")




class IceCreamStand(Restaurent):
				"""Makes a instence called IceCreamStand"""
				
				
				def __init__(self,restaurent_name):
								"""Sets the attributes"""
								super().__init__(restaurent_name)
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
				
				


				








