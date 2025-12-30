###Sourse : Python crash course(2nd edition) by Eric Matthes###
##example of a dictionary in a dictionary.
users = {'sahilXD':{'first':'sahil',
				                   'last':'roy',
				       				           'location':'kolkata',},
				        'rahilXD':{'first':'rahil',
				       				 								       'last':'das',
				       				 								       	'location':'burdwan',},
				         'rahulXD':{'first':'rahul',
				       				 								        'last':'bose',
				       				 								        				'location':'malda',},
				       				 								        								                   }

#to print users username,fullname & location
for username,user_info in users.items():
    print(f"\nUsername: {username.upper()}")
    full_name = f"{user_info['first'].upper()} {user_info['last'].upper()}"
    print(f"\tFull name: {full_name}")
    print(f"\tLocation: {user_info['location'].title()}")





