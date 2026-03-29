# Pointlist - Music Playlist Manager
# Team: Ayaan Niazi, Tooba Zehra, Sayed Mustafa Hussain

# Each node is a song in our playlist
def create_node(title, artist, duration, genre):
    song = {
        "title" : title,
        "artist": artist,
        "duration": duration,
        "genre": genre,
        "prev" : None,
        "next" : None
        }
    return song

# Each playlist (linked list) neeeds a first song (head) and last song (tail), and a number of songs (size)
def create_playlist():
    playlist = {
        "head" : None,
        "tail" : None,
        "size" : None
    }
    return playlist

# A playlist manager needs to have the ability to add a song:
def add_song(playlist, title, artist, duration, genre):
    new_song = create_node(title, artist, duration, genre)

    if playlist["head"] == None: #hence playlist empty
        playlist["head"] = new_song
        playlist["tail"] = new_song
    else:
        new_song["prev"] = playlist["tail"]
        playlist["tail"]["next"] = new_song
        playlist["tail"] = new_song
    
    playlist["size"] += 1


