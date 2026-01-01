###Sourse : Python crash course(2nd edition) by Eric Matthes###
##cp11's 3rd excrcise(other module = ex11_1.py)


class Employee:
				"""Makes a object called Employee """
				def __init__(self, first_name, last_name, annual_salary):
								self.first_name = first_name
								self.last_name = last_name
								self.annual_salary = annual_salary
				def give_raise(self, raise_amount=5000):
								self.annual_salary += raise_amount
								