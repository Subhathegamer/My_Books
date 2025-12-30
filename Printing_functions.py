###Sourse : Python crash course(2nd edition) by Eric Matthes###
##A module for cp8's 15th excrcise


#Copied from the file named Python_work_book_modules
def print_models(unprinted_designs, printed_models):
				"""Prints massage of printing each model seperately."""
				current_designs = unprinted_designs[:]
				print("Details of printing---")
				while current_designs:
								printed_model = current_designs.pop()
								print(f"Printing: {printed_model}")
								printed_models.append(printed_model)
						


def summarize_models(printed_models):
				"""Summarize which models are printed."""
				print(f"\nCompleted Printing Models:\n ")
				current_model = printed_models[:]
				while current_model:
								printed_model = current_model.pop()
								print(f"- {printed_model}")

