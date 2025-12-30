###Sourse : Python crash course(2nd edition) by Eric Matthes###
##cp10's 5th excrcise
file_path = "/storage/emulated/0/python_work/Python_work_book/File_python_work_book/programming_poll.txt"

while True:
				poll = input("Why are you learning python(To exit enter '#q'): ").strip()
				if poll == "#q":
								print("Thank you for giving the poll!")
								break
				else:
								with open(file_path, "a") as file_object:
												file_object.write(f"{poll}\n")

