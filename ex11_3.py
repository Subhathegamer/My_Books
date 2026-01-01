###Sourse : Python crash course(2nd edition) by Eric Matthes###
##cp11's 1st&2nd excrcise
import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
				"""Tests the employee class"""
				def setUp(self):
								"""Setup the attributes"""
								self.first_name = "Subhajit"
								self.last_name = "Hore"
								self.salary = 50000
				
				def test_give_default_raise(self):
								"""test the default salary raise"""
								employee = Employee(self.first_name, self.last_name, self.salary)
								employee.give_raise()
								self.assertNotEqual(employee.annual_salary, self.salary)

				def test_give_custom_raise(self):
								"""test the Employee class with a custom raise amount"""
								employee = Employee(self.first_name, self.last_name, self.salary)
								employee.give_raise(10000)
								self.assertEqual(employee.annual_salary, 60000)
				

if __name__ == "__main__":
				unittest.main()