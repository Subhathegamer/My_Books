###Sourse : Python crash course(2nd edition) by Eric Matthes###
##cp10's 8th excrcise

filepath_cat = "/storage/emulated/0/python_work/Python_work_book/File_python_work_book/cats.txt"
filepath_dog = "/storage/emulated/0/python_work/Python_work_book/File_python_work_book/dogs.txt"

try:
				with open(filepath_cat) as file_cat:
								contents = file_cat.read().strip()
except FileNotFoundError:
				pass
else:
								print(f"\t--Cat names--")
								print(contents)

try:
				with open(filepath_dog) as file_dog:
								contents = file_dog.read().strip()
except FileNotFoundError:
				print("The file that contents dogs names not found!!")
else:
				print(f"\t--Dog names--")
				print(contents)