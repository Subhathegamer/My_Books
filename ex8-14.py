




def make_car(car_model, car_manufacturer, **car_info):
				"""Makes a car info in a dictionary."""
				print("Details of The Car---\n")
				car_info['Model'] = car_model
				car_info['Manufacturer'] = car_manufacturer.title()
				return car_info

car = make_car(car_model='Subaru',car_manufacturer='outback',color='Black')
print(car)
