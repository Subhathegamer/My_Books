###Sourse : Python crash course(2nd edition) by Eric Matthes###
##cp10's 3rd&4th excrcise
file_path = "/storage/emulated/0/python_work/Python_work_book/File_python_work_book/guest_book.txt"
filepath = "/storage/emulated/0/guest.txt"


prompt = "Please tell your name(Enter '#q' to exit): "


while True:
				guest_name = input(prompt)
				if guest_name == "#q":
								print("Thank You!!")
								break
				else:
								with open(file_path,'a') as file_object:
												file_object.write(f"Guest name: {guest_name.title()}\n")
												print(f"{guest_name} successfully updated to Guest Book!")
												
												



