###Sourse : Python crash course(2nd edition) by Eric Matthes###
##cp8's 7th&8th excrcise

def make_album(title, artist, number=None):
				"""Writes a album title,its artist&number of songs it have."""
				album = {'Title':title.title(),'Artist':artist.title()}
				if number:
								album['Number of songs'] = number
				return album

while True:
				print(f"\n---ALBUM MAKER-------")
				print(f"\nPlease fullfill the followings---\n(To exit enter q)")
				title_input = input("Name of the album: ")
				if title_input == 'q':
								break
				artist_input = input("Name of the artist: ")
				if artist_input == 'q':
								break
				number_input = input("Number of song the album have: ")
				if number_input == 'q':
								break
		

				album_output = make_album(title=title_input, artist=artist_input,number=number_input)
				print(album_output)
				