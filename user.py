###Sourse : Python crash course(2nd edition) by Eric Matthes###
##cp9



class User:
				"""Make a instence called User."""
				
				
				def __init__(self,first_name,last_name,id_number):
								"""Difine a users first and last name."""
								self.firstname = first_name.title()
								self.lastname = last_name.title()
								self.id = id_number
								self.fullname = f"{self.firstname} {self.lastname}" 
								self.login_attempts = 0
								
								
				def login_attempt(self):
								"""Prints how many times user attempted to login."""
								print(f"User attempted {self.login_attempts} logins.")
				
				
				def increment_login_attempts(self):
								"""Increments the value of login attempts by 1"""
								self.login_attempts += 1
				
				
				def reset_login_attempts(self):
								"""Resets login attempts"""
								self.login_attempts = 0
				
				
				def describe_user(self):
								"""Describes tha user """
								print(f"User {self.fullname}'s id is {self.id} ")
								
				
				def greet_user(self):
								"""Prints a greeting to user."""
								print(f"Welcome {self.firstname}!")
