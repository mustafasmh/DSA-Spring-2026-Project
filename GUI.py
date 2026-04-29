import tkinter as tk
from tkinter import simpledialog, messagebox
from playlist import *
import random
from DLLadt import to_seconds

# playlist

playlist=create_playlist()

add_song(playlist, "Since I've been loving you", "Led Zeppelin", 445, "Rock", "https://youtu.be/vcIem-L398w?si=KHNQdcdZoVc0v_Dp")
add_song(playlist, "No Quarter", "Tool", 688, "Metal", "https://www.youtube.com/watch?v=_ZKIfCJZvZo")
add_song(playlist, "46&2", "Tool", 364, "Metal", "https://www.youtube.com/watch?v=GIuZUCpm9hc")
add_song(playlist, "H.", "Tool", 366, "Metal", "https://www.youtube.com/watch?v=bg8vTSyHFkQ")
add_song(playlist, "Crystal Clear", "Ayaan Niazi", 210, "Jazz", "")
add_song(playlist, "Radio Static", "Ayaan Niazi", 95, "Ambient", "")
add_song(playlist, "Blue in Green", "Miles Davis", 339, "Jazz", "https://www.youtube.com/watch?v=TLDflhhdPCg")
add_song(playlist, "Archangel", "Burial", 240, "Ambient", "https://www.youtube.com/watch?v=E2qLD9c3Gq4")
add_song(playlist, "Near Dark", "Burial", 236, "Ambient", "https://www.youtube.com/watch?v=TK7aQmdqCj8")
add_song(playlist, "Lover you should've come over", "Jeff Buckley", 405, "Alt", "https://www.youtube.com/watch?v=HxfE6PJmGS8")
add_song(playlist, "So Real", "Jeff Buckley", 279, "Alt", "https://www.youtube.com/watch?v=EcaxrqhUJ4c")
add_song(playlist, "In my time of need", "Opeth", 349, "Metal", "https://youtu.be/razzBeBLDG4?si=54rW6vsxNwWMn79T")
add_song(playlist, "Burden", "Opeth", 462, "Metal", "https://www.youtube.com/watch?v=orwgEEaJln0")

# colors 

BG="#0d0d0d"
SIDEBAR="#111111"
ACCENT="#854ef1"
TEXT="#e8e8e8"
SUBTEXT="#888888"
STATTEXT="#CCC6C6"
ROW_A="#161616"
ROW_B="#111111"
NOW_BG="#111111"
FONT_MAIN=("Courier New", 11)
FONT_HEAD=("Courier New", 13, "bold")
FONT_STATS_HEAD=("Courier New", 12, "bold")
FONT_STATS=("Courier New", 12, "bold")
FONT_NOW=("Courier New", 10)
FONT_TIME=("Courier New", 28, "bold")






# Phrases

top_artist_phrases=[
    "You basically lived in their discography this year.",
    "This was your clear #1. Not even close.",
    "You played them so much it's actually a little concerning.",
    "Your top artist. You clearly don't get tired of this sound.",
    "The data says you're obsessed. We're just reporting it."
]

second_artist_phrases=[
    "Always in rotation. A solid backup for when the #1 was on pause.",
    "They took up a massive chunk of your airtime.",
    "The runners-up. Still heavy hitters in your queue.",
    "You clearly vibe with this. They stayed in the top three for a reason."
]

third_artist_phrases=[
    "Coming in at #3. They held their own against the heavy hitters.",
    "The bronze medalist of your 2026 queue.",
    "A frequent guest in your rotation. They rounded out your top three.",
    "They secured the final spot on your podium.",
    "You listened to them enough to put them here, but not enough to beat the others."
]

top_song_phrases=[
    "This song stayed with you the most.",
    "Your #1 track. You hit the replay button until it gave up.",
    "The soundtrack to your year. You never seemed to get tired of it.",
    "If your 2026 has a theme song, this is definitely it.",
    "You and this track were inseparable. The data doesn't lie."
]

second_song_phrases=[
    "Your silver medalist. It kept your top song on its toes.",
    "Always a vibe. You turned to this one more than almost anything else.",
    "A high-rotation staple. It defined a huge part of your listening.",
    "You clearly had this one on loop for a significant chunk of the year."
]

third_song_phrases=[
    "Coming in at #3. It secured a solid spot in your top rotation.",
    "The final piece of your top three. A heavy hitter in its own right.",
    "You kept coming back to this one. It rounded out your year perfectly.",
    "It didn't quite hit #1, but it was never far from the play button.",
    "A frequent favorite that held its own against the top two."
]

top_genre_phrases=[
    "Your absolute go-to. If your year had a flavor profile, this was it.",
    "You didn't just listen to this genre; you made it your entire personality.",
    "The undisputed heavyweight champion of your library.",
    "You spent more time here than anywhere else.",
    "The data is in: you are officially a disciple of this sound."
]

second_genre_phrases=[
    "The silver medalist. It kept your main vibe from getting too predictable.",
    "A massive part of your sonic identity this year. Always in the mix.",
    "Your secondary obsession. You strayed from the #1 spot, but usually ended up here.",
    "The runner-up. It dominated your speakers whenever you needed a change of pace.",
    "Solidly in second. This genre was the backbone of your daily rotation."
]

third_genre_phrases=[
    "Coming in at #3. It provided the perfect counter-balance to your top two.",
    "The bronze medalist. It held its own against the heavy hitters.",
    "Rounding out your top three. You clearly have a soft spot for this sound.",
    "It didn't take the crown, but it definitely stayed in your weekly rotation.",
    "The final piece of your musical puzzle. It kept things interesting."
]






# window 

window=tk.Tk()
window.title("Pointlist")
window.geometry("1000x640")
window.configure(bg=BG)
window.resizable(True, True)



# header 

header=tk.Frame(window, bg=BG, pady=10)
header.pack(fill="x", padx=20)
tk.Label(header, text="◈ POINTLIST", bg=BG, fg=ACCENT, font=("Courier New", 20, "bold")).pack(side="left")



# dropdown menu bar 

menubar=tk.Menu(window, bg=SIDEBAR, fg=TEXT, activebackground=ACCENT, activeforeground=BG, font=FONT_MAIN, bd=0, tearoff=0)
window.config(menu=menubar)

playlist_menu=tk.Menu(menubar, bg=SIDEBAR, fg=TEXT, activebackground=ACCENT, activeforeground=BG, font=FONT_MAIN, tearoff=0)
songs_menu=tk.Menu(menubar, bg=SIDEBAR, fg=TEXT, activebackground=ACCENT, activeforeground=BG, font=FONT_MAIN, tearoff=0)
artist_menu=tk.Menu(menubar, bg=SIDEBAR, fg=TEXT, activebackground=ACCENT, activeforeground=BG, font=FONT_MAIN, tearoff=0)
stats_menu=tk.Menu(menubar, bg=SIDEBAR, fg=TEXT, activebackground=ACCENT, activeforeground=BG, font=FONT_MAIN, tearoff=0)

menubar.add_cascade(label="Playlist", menu=playlist_menu)
menubar.add_cascade(label="Songs", menu=songs_menu)
menubar.add_cascade(label="Artist", menu=artist_menu)
menubar.add_cascade(label="Stats", menu=stats_menu)



# song list area

list_outer=tk.Frame(window, bg=BG)
list_outer.pack(fill="both", expand=True, padx=20, pady=(0, 5))

canvas=tk.Canvas(list_outer, bg=BG, highlightthickness=0)
scrollbar=tk.Scrollbar(list_outer, orient="vertical", command=canvas.yview)
list_frame=tk.Frame(canvas, bg=BG)

def update_scroll(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

list_frame.bind("<Configure>", update_scroll)
canvas_window=canvas.create_window((0, 0), window=list_frame, anchor="nw")

def on_canvas_resize(event):
    canvas.itemconfig(canvas_window, width=event.width)

canvas.bind("<Configure>", on_canvas_resize)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")
canvas.configure(yscrollcommand=scrollbar.set)



# now-playing bar 

now_bar=tk.Frame(window, bg=NOW_BG, pady=8)
now_bar.pack(fill="x", side="bottom")

now_label=tk.Label(now_bar, text="♪  Nothing selected", bg=NOW_BG, fg=ACCENT, font=FONT_HEAD)
now_label.pack(pady=(2, 4))

ctrl_frame=tk.Frame(now_bar, bg=NOW_BG)
ctrl_frame.pack()

def keep_flat(event):
    event.widget.config(relief="flat")

def make_btn(parent, text, cmd):
    btn=tk.Button(parent, text=text, command=cmd, bg=SIDEBAR, fg=TEXT, activebackground=ACCENT, activeforeground=BG, font=FONT_MAIN, relief="flat", padx=14, pady=4, cursor="hand2", takefocus=0)
    btn.bind("<ButtonPress-1>", keep_flat)
    btn.bind("<ButtonRelease-1>", keep_flat)
    return btn



# Top Stats

def give_song_stats():
    
    songs=top_three_songs(playlist)
    
    if songs is None:
        messagebox.showerror("Pointlist", "Not enough songs played. Play at least 3 different songs first.")
        return
    
    songs=list(songs)
    
    artists=top_three_artists(playlist)
    
    if artists is None:
        messagebox.showerror("Pointlist", "Not enough artists played. Play songs from at least 3 different artists first.")
        return
    
    artists=list(artists)

    statwin=tk.Toplevel(window)
    statwin.title("Top Songs")
    statwin.geometry("800x320")
    statwin.configure(bg=BG)

    tk.Label(statwin, text="Your Top 3 Songs", bg=BG, fg=ACCENT, font=FONT_HEAD).pack(pady=(16, 10))

    statframe=tk.Frame(statwin, bg=BG)
    statframe.pack(fill="both", expand=True, padx=20)

    phrase_lists=[top_song_phrases, second_song_phrases, third_song_phrases]
    ranking=["  #1", "  #2", "  #3"]

    for i in range(3):
        
        phrase=random.choice(phrase_lists[i])

        if i==0:
            row_bg=ACCENT
            row_fg=BG
            
        else:
            row_bg=ROW_A
            row_fg=TEXT
       
            
        current_artist=search(playlist,"title",songs[i])['data']['artist']
        tk.Label(statframe, text=f"{ranking[i]}  {songs[i]}  —  {current_artist}", bg=row_bg, fg=row_fg, font=FONT_HEAD, anchor="w", padx=10, pady=8).pack(fill="x")
        tk.Label(statframe, text=f"       {phrase}", bg=BG, fg=STATTEXT, font=FONT_STATS, anchor="w", padx=10, pady=4).pack(fill="x")



def give_artist_stats():
    
    artists=top_three_artists(playlist)
    
    if artists is None:
        messagebox.showerror("Pointlist", "Not enough artists played. Play songs from at least 3 different artists first.")
        return
    
    artists=list(artists)

    astatwin=tk.Toplevel(window)
    astatwin.title("Top Artists")
    astatwin.geometry("800x320")
    astatwin.configure(bg=BG)

    tk.Label(astatwin, text="Your Top 3 Artists", bg=BG, fg=ACCENT, font=FONT_HEAD).pack(pady=10)

    astatframe=tk.Frame(astatwin, bg=BG)
    astatframe.pack(fill="both", expand=True, padx=15)

    phrase_lists=[top_artist_phrases, second_artist_phrases, third_artist_phrases]
    ranking=["  #1", "  #2", "  #3"]

    for i in range(len(artists)):
        
        phrase=random.choice(phrase_lists[i])

        if i==0:
            row_bg=ACCENT
            row_fg=BG
            
        else:
            row_bg=ROW_A
            row_fg=TEXT


        tk.Label(astatframe, text=f"{ranking[i]}  {artists[i]}", bg=row_bg, fg=row_fg, font=FONT_HEAD, anchor="w", padx=10, pady=8).pack(fill="x")
        tk.Label(astatframe, text=f"       {phrase}", bg=BG, fg=STATTEXT, font=FONT_STATS, anchor="w", padx=10, pady=4).pack(fill="x")



def give_genre_stats():
    
    genres=top_three_genres(playlist)
    
    if genres is None:
        messagebox.showerror("Pointlist", "Not enough genres played. Play songs from at least 3 different artists/genres first.")
        return
    
    genres=list(genres)

    gstatwin=tk.Toplevel(window)
    gstatwin.title("Top Genres")
    gstatwin.geometry("800x320")
    gstatwin.configure(bg=BG)

    tk.Label(gstatwin, text="Your Top 3 Genres", bg=BG, fg=ACCENT, font=FONT_HEAD).pack(pady=10)

    gstatframe=tk.Frame(gstatwin, bg=BG)
    gstatframe.pack(fill="both", expand=True, padx=15)

    phrase_lists=[top_genre_phrases, second_genre_phrases, third_genre_phrases]
    ranking=["  #1", "  #2", "  #3"]

    for i in range(len(genres)):
        
        phrase=random.choice(phrase_lists[i])

        if i==0:
            row_bg=ACCENT
            row_fg=BG
            
        else:
            row_bg=ROW_A
            row_fg=TEXT

        tk.Label(gstatframe, text=f"{ranking[i]}  {genres[i]}", bg=row_bg, fg=row_fg, font=FONT_HEAD, anchor="w", padx=10, pady=8).pack(fill="x")
        tk.Label(gstatframe, text=f"       {phrase}", bg=BG, fg=STATTEXT, font=FONT_STATS, anchor="w", padx=10, pady=4).pack(fill="x")



def time_spent():
    
    gstatwin=tk.Toplevel(window)
    gstatwin.title("Time Spent")
    gstatwin.geometry("500x180")
    gstatwin.configure(bg=BG)

    minutes=listening_minutes(playlist)

    gstatframe=tk.Frame(gstatwin, bg=BG)
    gstatframe.pack(expand=True)


    tk.Label(gstatframe, text="You spent a total of", bg=BG, fg=STATTEXT, font=FONT_STATS).pack()
    tk.Label(gstatframe, text=f"{minutes} minutes", bg=BG, fg=ACCENT, font=FONT_TIME).pack()
    tk.Label(gstatframe, text="being pointlist.", bg=BG, fg=STATTEXT, font=FONT_STATS).pack()



stats_menu.add_command(label="Top Songs", command=give_song_stats)
stats_menu.add_command(label="Top Artists", command=give_artist_stats)
stats_menu.add_command(label="Top Genre", command=give_genre_stats)
stats_menu.add_command(label="Total Time Spent", command=time_spent)






# helpers

def refresh():
    
    for w in list_frame.winfo_children():
        w.destroy()


    if playlist["size"]==0:
        tk.Label(list_frame, text="Playlist is empty", bg=BG, fg=SUBTEXT, font=FONT_MAIN).pack(pady=20)
        return


    current=playlist["head"]
    number=1
    
    header_text=(f"   #   {'Title':<38}" f"{'Artist':<28}" f"{'Genre':<12}" f"{'Time':<7}" f"{'Plays'}")

    tk.Label(list_frame, text=header_text, bg=ROW_A, fg=ACCENT, font=FONT_NOW, anchor="w", padx=6, pady=6).pack(fill="x")
    
    while True:
        song=current["data"]
        mins=song["duration"]//60
        secs=song["duration"]%60
        plays=song["play_count"]
        duration=f"{mins}:{secs:02d}"
        
        
        text=(f"  {number:>2}.  {song['title']:<38}" f"{song['artist']:<28}" f"{song['genre']:<12}" f"{duration:<7}" f"🎵 {plays}")

        is_now=(playlist["now_playing"] is not None and playlist["now_playing"] is current)

        if is_now:
            row_bg=ACCENT
            
        else:
            if number%2==0:
                row_bg=ROW_A
                
            else:
                row_bg=ROW_B

        if is_now:
            row_fg=BG
            
        else:
            row_fg=TEXT

        tk.Label(list_frame, text=text, bg=row_bg, fg=row_fg, font=FONT_NOW, anchor="w", padx=6, pady=5).pack(fill="x")

        number+=1
        
        if current==playlist["tail"]:
            break
        current=current["next"]



def ask(prompt, cast=str):
    
    val=simpledialog.askstring("Pointlist", prompt, parent=window)
    
    if val is None:
        return None
    
    if cast==int:
        if not val.strip().lstrip('-').isdigit():
            messagebox.showerror("Error", f"Expected a number for: {prompt}")
            return None
        return int(val)
    
    return val



def pick_song_number(title="Pick a song"):
    refresh()
    return ask(f"{title}\nEnter song number:", int)


def ask_duration():
    mins=ask("Minutes:", int)
    if mins is None:
        return None
    secs=ask("Seconds:", int)
    if secs is None:
        return None
    return to_seconds(mins, secs)


# playlist menu actions

def do_shuffle():
    
    if playlist["now_playing"]:
        current_title=playlist["now_playing"]["data"]["title"]
        current_artist=playlist["now_playing"]["data"]["artist"]
        
    else:
        current_title=None
        current_artist=None
    shuffle(playlist)
    
    if current_title:
        playlist["now_playing"]=search_title_artist(playlist, current_title,current_artist)
        
    refresh()
    messagebox.showinfo("Pointlist", "Playlist shuffled.")

def do_smart_shuffle():
    
    if playlist["now_playing"]:
        current_title=playlist["now_playing"]["data"]["title"]
        current_artist=playlist["now_playing"]["data"]["artist"]
        
    else:
        current_title=None
        current_artist=None
        
    smart_shuffle(playlist)
    
    if current_title:
        playlist["now_playing"]=search_title_artist(playlist,current_title,current_artist)
        
    refresh()
    messagebox.showinfo("Pointlist", "Playlist smart shuffled.")

def do_sortby():
    
    choice=simpledialog.askstring("Sort By", "Sort by:\n1. Title\n2. Artist\n3. Duration\n4. Genre\n5. Play Count", parent=window)
    fields={"1": "title", "2": "artist", "3": "duration", "4": "genre", "5": "play_count"}
    
    if choice in fields:
        order=simpledialog.askstring("Order", "Order:\n1. Ascending\n2. Descending", parent=window)
        
        if order not in ("1", "2"):
            return
        
        if order=="2":
            descending=True
            
        else:
            descending=False
            
            
        if playlist["now_playing"]:
            current_title=playlist["now_playing"]["data"]["title"]
            
        else:
            current_title=None
            
        sortby(playlist, fields[choice], descending)
        
        if current_title:
            playlist["now_playing"]=search(playlist, "title", current_title)
            
            
        refresh()
        
        if descending==True:
            messagebox.showinfo("Pointlist", f"Sorted by {fields[choice]} (descending).")
        else:
            messagebox.showinfo("Pointlist", f"Sorted by {fields[choice]} (ascending).")

playlist_menu.add_command(label="Shuffle", command=do_shuffle)
playlist_menu.add_command(label="Sort By", command=do_sortby)






# songs menu actions 

def do_add():
    
    title=ask("Song title:")
    
    if title is None:
        return
    
    artist=ask("Artist:")
    
    if artist is None:
        return
    
    node=search(playlist, "title", title)
    
    if node is not None and node["data"]["artist"]==artist:
        messagebox.showerror("Pointlist", f"'{title}' by {artist} already exists.")
        return
    
    duration=ask_duration()
    
    if duration is None:
        return
    
    genre=ask("Genre:")
    
    if genre is None:
        return
    
    link=ask("YouTube link (leave blank to skip):")
    
    if link is None:
        link=""
        
    add_song(playlist, title, artist, duration, genre, link)
    refresh()
    
    messagebox.showinfo("Pointlist", f"Added: {title}")



def do_update():
    
    title=ask("Song title to update:")
    
    if title is None:
        return
    
    artist=ask("Artist:")
    
    if artist is None:
        return
    
    node=search_title_artist(playlist, title, artist)
    
    
    if node is None:
        messagebox.showerror("Pointlist", "Song not found.")
        return
    
    field=ask("What to update?\n1. Title\n2. Artist\n3. Duration\n4. Genre\n5. Link")
    
    fields={"1": "title", "2": "artist", "3": "duration", "4": "genre", "5": "link"}
    
    if field not in fields:
        return
    
    if fields[field]=="duration":
        new_value=ask_duration()
        
    else:     
        new_value=ask("New value:")
        
    if new_value is None:
        return

    if fields[field]=="title":
        
        existing=search_title_artist(playlist, new_value, node["data"]["artist"])
        
        if existing is not None:
            messagebox.showerror("Pointlist", f"'{new_value}' by {node['data']['artist']} already exists.")
            return
        
    if fields[field]=="artist":
        
        existing=search_title_artist(playlist, node["data"]["title"], new_value)
        
        if existing is not None:
            messagebox.showerror("Pointlist", f"'{node['data']['title']}' by {new_value} already exists.")
            return
    
    
    
    update_song(playlist, node, fields[field], new_value)
    refresh()
    
    messagebox.showinfo("Pointlist", "Song updated.")



def do_remove():
    
    title=ask("Song title to remove:")
    
    if title is None:
        return
    
    artist=ask("Artist:")
    
    if artist is None:
        return
    
    node=search_title_artist(playlist, title, artist)
    
    
    if node is None:
        messagebox.showerror("Pointlist", "Song not found.")
        return
    
    if playlist["now_playing"] is node:
        playlist["now_playing"]=None
        now_label.config(text="♪  Nothing selected")
    
    remove_song(playlist, title, artist)
    refresh()
    
    messagebox.showinfo("Pointlist", f"Removed: {title}")



songs_menu.add_command(label="Add Song", command=do_add)
songs_menu.add_command(label="Remove Song", command=do_remove)
songs_menu.add_command(label="Update Song", command=do_update)






# artist menu actions

def do_artist():
    
    artist=ask("Artist name:")
    
    if artist is None:
        return
    
    if artist not in playlist["artist_head"]:
        messagebox.showerror("Pointlist", "Artist not found.")
        return

    win=tk.Toplevel(window)
    win.title(artist)
    win.geometry("700x400")
    win.configure(bg=BG)

    tk.Label(win, text=artist, bg=BG, fg=ACCENT, font=FONT_HEAD).pack(pady=10)

    frame=tk.Frame(win, bg=BG)
    frame.pack(fill="both", expand=True, padx=15)

    current=playlist["artist_head"][artist]
    nodes=[]
    number=1
    
    
    while True:
        
        song=current["data"]
        mins=song["duration"]//60
        secs=song["duration"]%60
        duration=f"{mins}:{secs:02d}"
        
        
        text=(f"  {number}.  {song['title']:<38}{song['genre']:<12}{duration:<7}🎵 {song['play_count']}")
        if number%2==0:
            tk.Label(frame, text=text, bg=ROW_A, fg=TEXT, font=FONT_NOW, anchor="w", padx=6, pady=5).pack(fill="x")
            
        else:
            tk.Label(frame, text=text, bg=ROW_B, fg=TEXT, font=FONT_NOW, anchor="w", padx=6, pady=5).pack(fill="x")
        nodes.append(current)
        number+=1
        
        if current==playlist["artist_tail"][artist]:
            break
        
        current=current["artist_next"]

    def play_from_artist():
        
        num=simpledialog.askinteger("Pointlist", "Enter song number to play:", parent=win)
        
        if num is None or num<1 or num>len(nodes):
            return
        
        win.destroy()
        _play_node(nodes[num-1])
        

    make_btn(win, "▶ Play a Song", play_from_artist).pack(pady=10)



def do_genre():
    genre=ask("Genre name:")
    
    if genre is None:
        return
    
    if genre not in playlist["genre_head"]:
        messagebox.showerror("Pointlist", "Genre not found.")
        return

    win=tk.Toplevel(window)
    win.title(genre)
    win.geometry("700x400")
    win.configure(bg=BG)

    tk.Label(win, text=genre, bg=BG, fg=ACCENT, font=FONT_HEAD).pack(pady=10)

    frame=tk.Frame(win, bg=BG)
    frame.pack(fill="both", expand=True, padx=15)

    current=playlist["genre_head"][genre]
    nodes=[]
    number=1
    
    def play_from_genre():
        
        num=simpledialog.askinteger("Pointlist", "Enter song number to play:", parent=win)
        
        if num is None or num<1 or num>len(nodes):
            return
        
        win.destroy()
        _play_node(nodes[num-1])
        

    
    
    
    while True:
        
        song=current["data"]
        mins=song["duration"]//60
        secs=song["duration"]%60
        duration=f"{mins}:{secs:02d}"
        
        
        text=(f"  {number}.  {song['title']:<38}{song['genre']:<12}{duration:<7}🎵 {song['play_count']}")
        if number%2==0:
            tk.Label(frame, text=text, bg=ROW_A, fg=TEXT, font=FONT_NOW, anchor="w", padx=6, pady=5).pack(fill="x")
            
        else:
            tk.Label(frame, text=text, bg=ROW_B, fg=TEXT, font=FONT_NOW, anchor="w", padx=6, pady=5).pack(fill="x")
        nodes.append(current)
        number+=1
        
        if current==playlist["genre_tail"][genre]:
            break
        
        current=current["genre_next"]


    make_btn(win, "▶ Play a Song", play_from_genre).pack(pady=10)
    


def do_recommended():
    recs=recommended_songs(playlist)
    
    if recs is None:
        messagebox.showerror("Pointlist", "Play some songs first so we can learn your taste.")
        return

    songs=recs[0]
    top_genre=recs[1]

    win=tk.Toplevel(window)
    win.title("Recommended")
    win.geometry("700x400")
    win.configure(bg=BG)

    tk.Label(win, text=f"Because you love {top_genre}", bg=BG, fg=ACCENT, font=FONT_HEAD).pack(pady=10)

    frame=tk.Frame(win, bg=BG)
    frame.pack(fill="both", expand=True, padx=15)

    nodes=[]
    number=1
    
    for current in songs:
        
        song=current["data"]
        mins=song["duration"]//60
        secs=song["duration"]%60
        duration=f"{mins}:{secs:02d}"
        
        text=(f"  {number}.  {song['title']:<38}{duration:<7}🎵 {song['play_count']}")
        
        if number%2==0:
            tk.Label(frame, text=text, bg=ROW_A, fg=TEXT, font=FONT_NOW, anchor="w", padx=6, pady=5).pack(fill="x")
            
        else:
            tk.Label(frame, text=text, bg=ROW_B, fg=TEXT, font=FONT_NOW, anchor="w", padx=6, pady=5).pack(fill="x")
                
        nodes.append(current)
        number+=1

    def play_recommended():
        
        num=simpledialog.askinteger("Pointlist", "Enter song number to play:", parent=win)
        
        if num is None or num<1 or num>len(nodes):
            return
        
        win.destroy()
        _play_node(nodes[num-1])

    make_btn(win, "▶ Play a Song", play_recommended).pack(pady=10)


artist_menu.add_command(label="Get Artist Songs", command=do_artist)
artist_menu.add_command(label="Get Genre Songs", command=do_genre)
artist_menu.add_command(label="Recommended", command=do_recommended)






# playback 

def _play_node(node):
    
    play_song(playlist, node["data"]["title"])
    now_label.config(text=f"♪  {node['data']['title']}  —  {node['data']['artist']}")
    refresh()



def do_play():
    
    num=ask("Enter song number to play:", int)
    
    if num is None or num<1 or num>playlist["size"]:
        return
    
    current=playlist["head"]
    
    for i in range(num-1):
        
        current=current["next"]
    _play_node(current)



def do_random_skip():
    
    song=random_skip(playlist)
    _play_node(song)



def do_next():
    
    np=playlist["now_playing"]
    
    if np and np["next"]:
        next=np["next"]
        
    else:
        next=playlist["head"]
        
    playlist["now_playing"]=next
    
    
    now_label.config(text=f"♪  {next['data']['title']}  —  {next['data']['artist']}")
    refresh()



def do_prev():
    
    np=playlist["now_playing"]
    
    if np and np["prev"]:
        prev=np["prev"]
        
    else:
        
        prev=playlist["tail"]
        
    playlist["now_playing"]=prev
    
    
    now_label.config(text=f"♪  {prev['data']['title']}  —  {prev['data']['artist']}")
    refresh()



def do_play_current():
    
    if playlist["now_playing"] is None:
        playlist["now_playing"]=playlist["head"]
        
        
    _play_node(playlist["now_playing"])



make_btn(ctrl_frame, "🔍  Specific Song", do_play).pack(side="left", padx=8)
make_btn(ctrl_frame, "⏮  Prev", do_prev).pack(side="left", padx=8)
make_btn(ctrl_frame, "▶  Play", do_play_current).pack(side="left", padx=8)
make_btn(ctrl_frame, "⏭  Next", do_next).pack(side="left", padx=8)
make_btn(ctrl_frame, "🎲 Random Skip", do_random_skip).pack(side="left", padx=8)






refresh()
window.mainloop()