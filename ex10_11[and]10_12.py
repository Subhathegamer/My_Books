###Sourse : Python crash course(2nd edition) by Eric Matthes###
##cp10's 11th&12th excrcise
import json
filepath = "/storage/emulated/0/python_work/Python_work_book/File_python_work_book/favorite_number.json"
def stored_number():
				try:
								with open(filepath) as fp:
												favorite_number = fp.read()
				except FileNotFoundError:
								new_number()
				else:
								print(f"I know your favorite number is {favorite_number} ." )


def new_number():
				number = input("What is your favorite number: ")
				print("I will remenber it.")
				try:
								number = int(number)
				except ValueError:
								print("Please enter a Valid number!")
								new_number()
				else:
								with open(filepath,"w") as fp:
												json.dump(number, fp)


stored_number()
