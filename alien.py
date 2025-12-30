###Sourse : Python crash course(2nd edition) by Eric Matthes###


aliens = []                        #creates a blank list as aliens.
for alien_number in range(30):             #tells how many times it have to repeat.
				  alien_data = {'color':'green','speed':'slow','points':5}           #makes a dictionary of alien data.
				  aliens.append(alien_data)                     #add alien data into a list named aliens.

for alien_number in range(5):             #tells how many times it have to repeat.
				  alien_data = {'color':'yellow','speed':'medium','points':10}           #makes a dictionary of alien data.
				  aliens.append(alien_data)

for alien in aliens[:3]:
				  if alien['color'] == 'green':
				  				  alien['color'] = 'yellow'
				  				  alien['speed'] = 'medium'
				  				  alien['points'] = '10'
for alien in aliens[30:36]:			  				  
				  if alien['color'] == 'yellow':
				  				  alien['color'] = 'red'
				  				  alien['speed'] = 'fast'
				  				  alien['points'] = '15'

for alien in aliens[:]:                   #uses for loop to tells how many times it have to repeat.
				  print(alien)                 
print("...")

print(f"The total number of aliens are {len(aliens)}.")			             #it prints how many aliens are there.				  



