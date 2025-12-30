###Sourse : Python crash course(2nd edition) by Eric Matthes###
##cp6's 2nd&10th excrcise
fav_numbers = {'anil':[45,92],
    		                     		'rahil':[56,89],
    					                  			'sanny':[40,35],
    									              			'kyro':[66,20],
    															             	}
for name,fav_nums in fav_numbers.items():
				print(f"{name.title()}'s favorite numbers are {fav_nums[0]},{fav_nums[1]}")