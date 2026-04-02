# File for testing 

from playlist import *

# playlist = create_playlist()
# add_song(playlist, "Blinding Lights", "The Weeknd", 200, "Pop")
# add_song(playlist, "Bohemian Rhapsody", "Queen", 354, "Rock")
# add_song(playlist, "Shape of You", "Ed Sheeran", 234, "Pop")
# add_song(playlist, "Starboy", "The Weeknd", 230, "Pop")
# add_song(playlist, "Since I've Been Loving you", "Led Zeppelin", 676, "Rock")


# # display_playlist(playlist)

# get_artist_songs(playlist,"The Weeknd")


# '''
# Expected output:

# 1. Blinding Lights - The Weeknd | Pop | 3:20
# 2. Bohemian Rhapsody - Queen | Rock | 5:54
# 3. Shape of You - Ed Sheeran | Pop | 3:54
# '''


playlist = create_playlist()
add_song(playlist, "Blinding Lights", "The Weeknd", 200, "Pop")
add_song(playlist, "Bohemian Rhapsody", "Queen", 354, "Rock")
add_song(playlist, "Shape of You", "Ed Sheeran", 234, "Pop")
add_song(playlist, "Starboy", "The Weeknd", 230, "Pop")
add_song(playlist, "Save Your Tears", "The Weeknd", 195, "Pop")

# should show all 5
print("\n")
print("\n")
display_playlist(playlist)
print("\n")
print("\n")
shuffle(playlist)
display_playlist(playlist)
print("\n")
print("\n")
# should show 3 Weeknd songs
get_artist_songs(playlist, "The Weeknd")
print("\n")
print("\n")
# delete middle of artist chain
remove_song(playlist, "Starboy")
get_artist_songs(playlist, "The Weeknd")  # should show Blinding Lights, Save Your Tears
print("\n")
print("\n")
# delete head of artist chain
remove_song(playlist, "Blinding Lights")
get_artist_songs(playlist, "The Weeknd")  # should show Save Your Tears
print("\n") 
print("\n")
# delete only remaining song by artist
remove_song(playlist, "Save Your Tears")
get_artist_songs(playlist, "The Weeknd")  # should print Artist not found


print("\n")
print("\n")
# delete only remaining song by artist
remove_song(playlist, "Save Your Tears")
get_artist_songs(playlist, "The Weeknd")  # should print Artist not found
