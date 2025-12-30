###Sourse : Python crash course(2nd edition) by Eric Matthes###
##cp8's 9th&10th&11th excrcise


def sent_massage(massages):
				"""Prints every massage"""
				sent_massages = massages[:]
				while sent_massages:
								current_massage = sent_massages.pop()
								print(current_massage)


def show_massage(massages):
				"""Prints every massage"""
				copy_massages = massages[:]
				while copy_massages:
								current_massage = copy_massages.pop()
								print(current_massage)

massages = ['Hello python!','Hi Pero!','My favorite language is python',]
massages_copy = massages[:]
sent_massage(massages)
print(massages)
print(massages_copy)