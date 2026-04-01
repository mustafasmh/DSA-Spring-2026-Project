# File for testing 

from playlist import *

playlist = create_playlist()
add_song(playlist, "Blinding Lights", "The Weeknd", 200, "Pop")
add_song(playlist, "Bohemian Rhapsody", "Queen", 354, "Rock")
add_song(playlist, "Shape of You", "Ed Sheeran", 234, "Pop")
add_song(playlist, "Starboy", "The Weeknd", 230, "Pop")
add_song(playlist, "Since I've Been Loving you", "Led Zeppelin", 676, "Rock")


# display_playlist(playlist)

get_artist_songs(playlist,"The Weeknd")


'''
Expected output:

1. Blinding Lights - The Weeknd | Pop | 3:20
2. Bohemian Rhapsody - Queen | Rock | 5:54
3. Shape of You - Ed Sheeran | Pop | 3:54
'''