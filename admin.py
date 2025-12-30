###Sourse : Python crash course(2nd edition) by Eric Matthes###
##cp9
from user import User
from privileges import Privileges

class Admin(User):
				"""Makes an object called Admin."""
				
				
				def __init__(self,first_name,last_name,id_number):
								"""Sets every new attributes"""
								super().__init__(first_name,last_name,id_number)
								self.privileges = Privileges()
								
				
				def show_admin_privileges(self):
								print(f"{self.fullname} has these Privileges:")
								self.privileges.show_privileges()