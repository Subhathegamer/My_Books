###Sourse : Python crash course(2nd edition) by Eric Matthes###
##cp10's 1st&2nd excrcise


#read and write the full file
with open("/storage/emulated/0/python_work/Python_work_book/File_python_work_book/learning_python.txt") as file_object:
				contents = file_object.read()
				print(contents.strip())

#Blank space
for _ in range(2):
				print(f"--\t--\t--\t--\t--")

#read the full file but writes line by line
with open("/storage/emulated/0/python_work/Python_work_book/File_python_work_book/learning_python.txt") as file_object:
				for line in file_object:
								print(line.strip())

#Blank space
for _ in range(2):
				print(f"--\t--\t--\t--\t--")

#read the full file but print the contents of the files outside the with command.
with open("/storage/emulated/0/python_work/Python_work_book/File_python_work_book/learning_python.txt") as file_object :
				contents = file_object.readlines()

for line in contents:
				print(line.strip())

#Blank space
for _ in range(2):
				print(f"--\t--\t--\t--\t--")

#replace the name Python to C 
for line in contents:
				print(line.replace('Python','C').strip())

				


