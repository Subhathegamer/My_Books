###Sourse : Python crash course(2nd edition) by Eric Matthes###

fav_lang = {                                   #dictionary of friends name and their favorite language.
    'sanil':'c',
    				'rahil':'html',
    								'sanny':'java',
    												'rahul':'python',
    																}
people = ['sanil','rahil','sarash','rohit','kyro',]         #List of some people names.

for p in people:                 #for loop for turning each people as p temporary.
    if p in fav_lang:           #if statement to find if the p is in fav_lang.
				  				  print(f"{p.title()}, thank you for taking the poll.")		  				      # Writes a greetings for those who took the poll already.
    else:                                                   #else: connects to if statement of line 12 as if-else chain.
      				print(f"{p.title()} please take the poll.")                        #Writes a massage for taking the poll who did't took the poll before.



