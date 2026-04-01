"""

 Pointlist - Music Playlist Manager
 Team: Ayaan Niazi, Tooba Zehra, Sayed Mustafa Hussain

"""
from DLLadt import *


# Each song is a node in our playlist


def create_song(title,artist,duration,genre):
    
    data = {
        "title":title,
        "artist":artist,
        "duration":duration,
        "genre":genre
        }
    
    song = create_node(data)
    return song

# A playlist manager needs to have the ability to create a new empty playlist


def create_playlist():
    
    playlist=create_list()

    return playlist

# A playlist manager needs to have the ability to add a song:


def add_song(playlist, title, artist, duration, genre):
    
    new_song=create_song(title, artist, duration, genre)
    insertEnd(playlist, new_song["data"])
    node=playlist["tail"]
    artist_list(playlist, node)

# A playlist manager needs to have the ability to delete songs:


def remove_song(playlist, title):
    
    
    node = search(playlist, "title", title)

    if node is None:
        
        print("Song not found")
        return

    delete_node(playlist, node)
    print("Song removed successfully")

# A playlist manager needs to have the ability to display a playlist:


def display_playlist(playlist):
    
    
    if playlist["size"] == 0:
        
        print("Playlist is empty")
        return

    current = playlist["head"]
    number = 1

    while True:
        
        song = current["data"]
        mins = song["duration"] // 60 #
        secs = song["duration"] % 60
        
        print(f"{number}. {song["title"]} - {song["artist"]} | {song["genre"]} | {mins}:{secs:02d}") 

        number += 1
        if current == playlist["tail"]:
            break
        current = current["next"]





def artist_list(playlist,node):
    
    name=node["data"]["artist"]
    
    if name in playlist["artist_heads"]:
        
        playlist["artist_tails"][name]["artist_next"]=node
        playlist["artist_tails"][name]=node 
        
    else:
        
        playlist["artist_heads"][name]=node
        playlist["artist_tails"][name]=node
 



def get_artist_songs(playlist,artist):
    
    if artist not in playlist["artist_heads"]:
        
        print("Artist not found")
        return
    
    current=playlist["artist_heads"][artist]
    
    number=1

    while True:
        
        song=current["data"]
        mins=song["duration"]//60
        secs=song["duration"]%60
        
        print(f"{number}. {song["title"]} - {song["artist"]} | {song["genre"]} | {mins}:{secs:02d}") 

        number+=1
        if current==playlist["artist_tails"][artist]:
            break
        current=current["artist_next"]



    
    
    
    
    
    
