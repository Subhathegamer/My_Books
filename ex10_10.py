###Sourse : Python crash course(2nd edition) by Eric Matthes###
##cp10's 10th excrcise
filepath = "/storage/emulated/0/python_work/Python_work_book/File_python_work_book/textfile.txt"
with open(filepath) as file:
				contents = file.read()

words = contents.lower().count("the ")
print(words)
