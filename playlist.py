"""

 Pointlist - Music Playlist Manager
 Team: Ayaan Niazi, Tooba Zehra, Sayed Mustafa Hussain

"""
from DLLadt import *
import random
import webbrowser


# Each song is a node in our playlist


def create_song(title, artist, duration, genre, link=""):
    data = {
        "title": title,
        "artist": artist,
        "duration": duration,
        "genre": genre,
        "play_count": 0,
        "link": link
    }
    song = create_node(data)
    return song





# A playlist manager needs to have the ability to create a new empty playlist
def create_playlist():
    
    playlist=create_list()

    return playlist





# A playlist manager needs to have the ability to add a song:
def add_song(playlist, title, artist, duration, genre, link=""):
    new_song = create_song(title, artist, duration, genre, link)
    insertEnd(playlist, new_song["data"])
    node = playlist["tail"]
    artist_chain(playlist, node)






# A playlist manager needs to have the ability to delete songs:
def remove_song(playlist, title):
    
    
    node = search(playlist, "title", title)

    if node is None:
        
        print("Song not found")
        return

    removefromchain(playlist,node)
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






def artist_chain(playlist,node):
    
    name=node["data"]["artist"]
    
    if name in playlist["artist_head"]:
        
        node["artist_prev"]=playlist["artist_tail"][name]
        playlist["artist_tail"][name]["artist_next"]=node
        playlist["artist_tail"][name]=node 
        
    else:
        
        playlist["artist_head"][name]=node
        playlist["artist_tail"][name]=node
 
 
 
 
 

def removefromchain(playlist,node):
    
    name=node["data"]["artist"]
    
    if playlist["artist_head"][name]==playlist["artist_tail"][name]:#only song by this artist
        
        
        del playlist["artist_head"][name]
        del playlist["artist_tail"][name]
    
    
    elif node==playlist["artist_head"][name]: #if the song is the head
        
        
        playlist["artist_head"][name]["artist_next"]["artist_prev"]=None #the previous pointer of the song after head is set to None
        playlist["artist_head"][name]=playlist["artist_head"][name]["artist_next"] #the song after head becomes the new head
        
        
    elif node==playlist["artist_tail"][name]: #if the song is the tail
        
        
        playlist["artist_tail"][name]["artist_prev"]["artist_next"]=None #the next pointer of the song before tail is set to None
        playlist["artist_tail"][name]=playlist["artist_tail"][name]["artist_prev"] #the song before tail becomes the new tail
        
    else:
        
        if node["artist_prev"] is not None:
            node["artist_prev"]["artist_next"]=node["artist_next"] #the next pointer of the song before the song being removed is updated to be the song after
            
        if node["artist_next"] is not None:
            node["artist_next"]["artist_prev"]=node["artist_prev"] #the prev pointer of the song after the song being removed is updated to be the song before

    node["artist_prev"]=None
    node["artist_next"]=None






def get_artist_songs(playlist,artist):
    
    if artist not in playlist["artist_head"]:
        
        print("Artist not found")
        return
    
    current=playlist["artist_head"][artist]
    
    number=1

    while True:
        
        song=current["data"]
        mins=song["duration"]//60
        secs=song["duration"]%60
        
        print(f"{number}. {song["title"]} - {song["artist"]} | {song["genre"]} | {mins}:{secs:02d}") 

        number+=1
        if current==playlist["artist_tail"][artist]:
            break
        current=current["artist_next"]
        





def shuffle(playlist):

    arr=[]

    current=playlist["head"]

    if playlist["size"]!=0:

        while True:

            arr+=[current["data"]] 
            if current==playlist["tail"]:
                break
            current=current["next"]

        random.shuffle(arr)
        current=playlist["head"]

        for node in arr: #replacing playlist with shuffled nodes

            current["data"]=node
            if current==playlist["tail"]:
                break
            current=current["next"]

        playlist["artist_head"]={} #clearing artist chain
        playlist["artist_tail"]={}

        current=playlist["head"]
        while True:
            
            artist_chain(playlist, current) #rebuilding artist chain
            
            if current==playlist["tail"]:
                break
            current=current["next"]

    
    
    
    
    
def sortby(playlist, field, descending):

    arr=[]
    current=playlist["head"]

    if playlist["size"]!=0:

        while True:

            arr+=[current["data"]] 
            if current==playlist["tail"]:
                break
            current=current["next"]
    
    mergeSort(arr, 0, len(arr)-1, field, descending)

    current=playlist["head"]

    for node in arr: #replacing playlist with sorted nodes

        current["data"]=node
        if current==playlist["tail"]:
            break
        current=current["next"]

    playlist["artist_head"]={} #clearing artist chain
    playlist["artist_tail"]={}

    current=playlist["head"]
    while True:
        
        artist_chain(playlist, current) #rebuilding artist chain
        
        if current==playlist["tail"]:
            break
        current=current["next"]



def play_song(playlist, title):
    node=search(playlist, "title", title)
    if node is None:
        print("Song not found")
        return
    node["data"]["play_count"]+=1
    playlist["now_playing"]=node
    print(f"Now Playing: {node['data']['title']} - {node['data']['artist']}")
    webbrowser.open(node["data"]["link"])


def smart_shuffle(playlist):
    sortby(playlist, 'play_count', True) #sorts by amount of plays to predict what the user might want next


def random_skip(playlist): #skips to a random song in the playlist without changing playlist order
    
    n=random.randint(1, playlist['size'])

    if playlist['now_playing']==None: #no song playing 
        currentsong=playlist['head'] #then start from head

    else:
        currentsong=playlist['now_playing']
    
    for i in range(n):
        if currentsong['next']==None: #loop back to start if tail found
            currentsong=playlist['head']
        else:
            currentsong=currentsong['next']

    title=currentsong['data']['title']
    play_song(playlist, title) #play new song

