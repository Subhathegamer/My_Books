###Sourse : Python crash course(2nd edition) by Eric Matthes###
##cp8's 12th excrcise

def build_profile(first, last, **user_info):
				"""Creats a dictionary of a user's info and returns it."""
				user_info['first_name'] = first.title()
				user_info['last_name'] = last.title()
				return user_info

user_profile = build_profile('subhajit','hore',country='INDIA',state='WB',learning=)

