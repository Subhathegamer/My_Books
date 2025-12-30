###Sourse : Python crash course(2nd edition) by Eric Matthes###
##cp9's 3rd&5th&7th&8th excrcise


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
				
				
				
				
class Admin(User):
				"""Makes an object called Admin."""
				
				
				def __init__(self,first_name,last_name,id_number='Admin_001'):
								"""Sets every new attributes"""
								super().__init__(first_name,last_name,id_number)
								self.privileges = Privileges()
								
				
				def show_admin_privileges(self):
								print(f"{self.fullname} has these Privileges:")
								self.privileges.show_privileges()
				



class Privileges():
				"""Creats a class called Privileges."""
				
				
				def __init__(self):
								"""Creats"""
								self.privileges = []
								
				
				def add_privileges(self, privilege):
								"""Adds privileges to self.privileges"""
								privilege = privilege.strip()
								if privilege and privilege not in self.privileges:
												self.privileges.append(privilege)

				
				
				
				
				def show_privileges(self):
								"""Shows the privileges"""
								for privilege in self.privileges:
												print(f"- {privilege}")









#raw data for testing 
user_1 = User('raj','roy','259-380')
user_1.describe_user()
user_1.login_attempt()
user_1.increment_login_attempts()
user_1.login_attempt()
user_1.reset_login_attempts()
user_1.login_attempt()


#Raw data for testing code
admin1 = Admin("Subhajit","Hore")
admin1.privileges.add_privileges("ADD USER")
admin1.privileges.add_privileges("REMOVE USER")
admin1.privileges.add_privileges(" ")
admin1.privileges.add_privileges("ADD POST")
admin1.privileges.add_privileges("REMOVE POST")
admin1.show_admin_privileges()
								
								
								
								
								
