###Sourse : Python crash course(2nd edition) by Eric Matthes###
##cp7's 3rd excrcise
#prompt
prompt = "If you write a  number below I will show you that is it multiple of 10"
prompt += f"\nwrite the number: "
#input and int
number = input(prompt)
number = int(number)

if number % 10 == 0:
				print(f"{number} is a multiple of 10")
else:
				print(f"{number} is not a multiple of 10")



