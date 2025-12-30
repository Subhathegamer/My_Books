###START###
rivers = {'Nile':'Egypt',                              #Dictionary of rivers and countries
			         'Ganga':'India',
				         				'Bramha putra':'Indo-Chin',
				         				
				         				}

for r,c in rivers.items():
				  print(f"{r.title()}:{c.title()}")                         #prints each river with its country				  
print()				  	                                          #prints a blank line for smoother experince
for r,c in rivers.items():
    print(f"The {r.title()} runs through {c}.")     #prints a sentance for each river and country
print()                                                #prints a blank line for smoother experince
for r,c in rivers.items():
    print(f"{r.upper()}")                           #prints each countries name in Upper case 
print()                                                #prints a blank line for smoother experince
for r,c in rivers.items():
    print(f"{c.upper()}")


