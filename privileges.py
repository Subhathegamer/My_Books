###Sourse : Python crash course(2nd edition) by Eric Matthes###
##cp9


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












