# File for testing 

from playlist_adt import *

playlist = create_playlist()
add_song(playlist, "Blinding Lights", "The Weeknd", 200, "Pop")
add_song(playlist, "Bohemian Rhapsody", "Queen", 354, "Rock")
add_song(playlist, "Shape of You", "Ed Sheeran", 234, "Pop")

display_playlist(playlist)

'''
Expected output:

1. Blinding Lights - The Weeknd | Pop | 3:20
2. Bohemian Rhapsody - Queen | Rock | 5:54
3. Shape of You - Ed Sheeran | Pop | 3:54
'''