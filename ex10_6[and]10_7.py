###Sourse : Python crash course(2nd edition) by Eric Matthes###
##cp10's 6th&7th excrcise

print(f"\t---Addition Calculator---")
print(f"\n\n\n(Enter'Quit' to exit)")

while True:
				first_number = input("\nFirst Number: ")
				if first_number == "Quit":
								print("Thank you!")
								break
				second_number = input("Second Number: ")
				if second_number == "Quit":
								print("Thank you!")
								break
				try:
								result = int(first_number)+ int(second_number)
				except ValueError:
								print("!!!Please give a valid number!!!")
				else:
								print(f"Answer: {result}")
								
