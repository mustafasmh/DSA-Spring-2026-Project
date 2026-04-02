# File for testing 

from playlist import *



playlist=create_playlist()

"""

SONGS GO HERE:
  
  
"""

add_song(playlist, "Since I've been loving you", "Led Zeppelin", 444, "Rock")
add_song(playlist, "No Quarter", "Tool", 673, "Metal")
add_song(playlist, "46&2", "Tool", 364, "Metal")
add_song(playlist, "Pneuma", "Tool", 713, "Metal")
add_song(playlist, "Crystal Clear", "Ayaan Niazi", 210, "Jazz")
add_song(playlist, "Radio Static", "Ayaan Niazi", 95, "Dread")
add_song(playlist, "Blue in Green", "Miles Davis", 337, "Jazz")
add_song(playlist, "Archangel", "Burial", 240, "Ambient")
add_song(playlist, "Near Dark", "Burial", 236, "Ambient")
add_song(playlist, "Glory Box", "Portishead", 308, "Alt")
add_song(playlist, "Lover you should've come over", "Jeff Buckley", 310, "Alt")
add_song(playlist, "So Real", "Jeff Buckley", 283, "Alt")
add_song(playlist, "In my time of need", "Opeth", 356, "Metal")
add_song(playlist, "Burden", "Opeth", 461, "Metal")
add_song(playlist, "Pride and Joy", "Stevie Ray Vaughan", 219, "Blues")
add_song(playlist, "Lenny", "Stevie Ray Vaughan", 297, "Blues")
add_song(playlist, "The Thrill is Gone", "B.B.King", 324, "Blues")
add_song(playlist, "Go With The Flow", "Queens Of The Stone Age", 187, "Rock")
add_song(playlist, "Ketamine", "Princess Goes", 306, "Alt")
add_song(playlist, "Elaine", "ABBA", 224, "Pop")
add_song(playlist, "Pneuma", "Tool", 544, "Metal")
add_song(playlist, "Blank Fairy", "Akira Yamaoka", 72, "Ambient")
add_song(playlist, "White Noiz", "Akira Yamaoka", 83, "Ambient")
add_song(playlist, "Promise (Reprise)", "Akira Yamaoka", 104, "Ambient")


"""


FUNCTION CALLS GO HERE:

  
"""


print("\n")
print("\n")
print("Will show in order of Insertion")
print("\n")
display_playlist(playlist)
print("\n")
print("\n")
print("Will show Shuffled playlist")
print("\n")
shuffle(playlist)
display_playlist(playlist)
print("\n")
print("\n")
sortby(playlist, "artist")
print("Will show playlist sorted Artist Alphabetically")
print("\n")
display_playlist(playlist)
print("\n")
print("\n")
get_artist_songs(playlist, "Ayaan Niazi")
print("\n")
print("\n")
get_artist_songs(playlist, "Stevie Ray Vaughan")
print("\n")
remove_song(playlist,"Lenny")
get_artist_songs(playlist, "Stevie Ray Vaughan")
print("\n")
print("\n")

get_artist_songs(playlist, "Akira Yamaoka")
print("\n")
print("\n")