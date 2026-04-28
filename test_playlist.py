from playlist import *

playlist=create_playlist()

add_song(playlist, "Since I've been loving you", "Led Zeppelin", 444, "Rock", "https://youtu.be/vcIem-L398w?si=KHNQdcdZoVc0v_Dp")
add_song(playlist, "No Quarter", "Tool", 673, "Metal", "https://www.youtube.com/watch?v=_ZKIfCJZvZo")
add_song(playlist, "46&2", "Tool", 364, "Metal", "https://www.youtube.com/watch?v=GIuZUCpm9hc")
add_song(playlist, "H.", "Tool", 713, "Metal", "https://www.youtube.com/watch?v=bg8vTSyHFkQ")
add_song(playlist, "Crystal Clear", "Ayaan Niazi", 210, "Jazz", "") 
add_song(playlist, "Radio Static", "Ayaan Niazi", 95, "Dread", "")
add_song(playlist, "Blue in Green", "Miles Davis", 337, "Jazz", "https://www.youtube.com/watch?v=TLDflhhdPCg")
add_song(playlist, "Archangel", "Burial", 240, "Ambient", "https://www.youtube.com/watch?v=E2qLD9c3Gq4")
add_song(playlist, "Near Dark", "Burial", 236, "Ambient", "https://www.youtube.com/watch?v=TK7aQmdqCj8")
add_song(playlist, "Lover you should've come over", "Jeff Buckley", 310, "Alt", "https://www.youtube.com/watch?v=HxfE6PJmGS8")
add_song(playlist, "So Real", "Jeff Buckley", 283, "Alt", "https://www.youtube.com/watch?v=EcaxrqhUJ4c")
add_song(playlist, "In my time of need", "Opeth", 356, "Metal", "https://youtu.be/razzBeBLDG4?si=54rW6vsxNwWMn79T")
add_song(playlist, "Burden", "Opeth", 461, "Metal", "https://www.youtube.com/watch?v=orwgEEaJln0")
# add_song(playlist, "Pride and Joy", "Stevie Ray Vaughan", 219, "Blues", "https://www.youtube.com/watch?v=tiSmPaRGvFg")
# add_song(playlist, "Lenny", "Stevie Ray Vaughan", 297, "Blues", "https://www.youtube.com/watch?v=1H0lGgSPCqE")
# add_song(playlist, "The Thrill is Gone", "B.B.King", 324, "Blues", "https://www.youtube.com/watch?v=oica5jG7FpU")
# add_song(playlist, "Go With The Flow", "Queens Of The Stone Age", 187, "Rock", "https://www.youtube.com/watch?v=d4aFDSEEzUc")
# add_song(playlist, "Ketamine", "Princess Goes", 306, "Alt", "https://www.youtube.com/watch?v=dummy")
# add_song(playlist, "Elaine", "ABBA", 224, "Pop", "https://www.youtube.com/watch?v=dummy")
# add_song(playlist, "Blank Fairy", "Akira Yamaoka", 72, "Ambient", "https://www.youtube.com/watch?v=dummy")
# add_song(playlist, "White Noiz", "Akira Yamaoka", 83, "Ambient", "https://www.youtube.com/watch?v=dummy")
# add_song(playlist, "Promise (Reprise)", "Akira Yamaoka", 104, "Ambient", "https://www.youtube.com/watch?v=dummy")

# menu(playlist)

display_playlist(playlist)
print('\n')

# play_song(playlist,"Near Dark")
# play_song(playlist,"Near Dark")
# play_song(playlist,"H.")
# play_song(playlist,"Near Dark")
# play_song(playlist,"H.")
# play_song(playlist,"No Quarter")

play_song(playlist, "Crystal Clear")
play_song(playlist, "Crystal Clear")
play_song(playlist, "Radio Static")
play_song(playlist, "Burden")
play_song(playlist, "Burden")
play_song(playlist, "So Real")



print('\n')
print(top_three_artists(playlist))
print('\n')
print(top_three_songs(playlist))
print('\n')
print(top_three_genres(playlist))
print('\n')
display_playlist(playlist)

