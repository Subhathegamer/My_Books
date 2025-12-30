fav_lang = {
    'sanil':'c',
    				'rahil':'html',
    								'sanny':'java',
    												'rahul':'python',
    																}
friends = ['phil', 'sanny']
for n in fav_lang.keys():
				  print(f"Hi,{n.title()}")
				  
				  if n in friends:
				      print(f"\tHi,{n}!I see you learning {fav_lang[n]}")
print(f"\n")
for name in sorted(fav_lang.keys(),reverse=True): 
				  print(f"\t\t{name.title()}, thank you for taking the poll.")



