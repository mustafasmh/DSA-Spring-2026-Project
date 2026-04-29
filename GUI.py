import tkinter as tk
from tkinter import simpledialog, messagebox
from playlist import *

# ── playlist ──────────────────────────────────────────────────────────────────
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

# ── colors ───────────────────────────────────────────────────────────────────
BG="#0d0d0d"
SIDEBAR="#111111"
ACCENT="#854ef1"
TEXT="#e8e8e8"
SUBTEXT="#888888"
ROW_A="#161616"
ROW_B="#111111"
NOW_BG="#111111"
FONT_MAIN=("Courier New", 11)
FONT_HEAD=("Courier New", 13, "bold")
FONT_NOW=("Courier New", 10)

# ── window ────────────────────────────────────────────────────────────────────
window=tk.Tk()
window.title("Pointlist")
window.geometry("1000x640")
window.configure(bg=BG)
window.resizable(True, True)

# ── header ────────────────────────────────────────────────────────────────────
header=tk.Frame(window, bg=BG, pady=10)
header.pack(fill="x", padx=20)
tk.Label(header, text="◈ POINTLIST", bg=BG, fg=ACCENT, font=("Courier New", 20, "bold")).pack(side="left")

# ── dropdown menu bar ─────────────────────────────────────────────────────────
menubar=tk.Menu(window, bg=SIDEBAR, fg=TEXT, activebackground=ACCENT, activeforeground=BG, font=FONT_MAIN, bd=0, tearoff=0)
window.config(menu=menubar)

playlist_menu=tk.Menu(menubar, bg=SIDEBAR, fg=TEXT, activebackground=ACCENT, activeforeground=BG, font=FONT_MAIN, tearoff=0)
songs_menu=tk.Menu(menubar, bg=SIDEBAR, fg=TEXT, activebackground=ACCENT, activeforeground=BG, font=FONT_MAIN, tearoff=0)
artist_menu=tk.Menu(menubar, bg=SIDEBAR, fg=TEXT, activebackground=ACCENT, activeforeground=BG, font=FONT_MAIN, tearoff=0)

menubar.add_cascade(label="Playlist", menu=playlist_menu)
menubar.add_cascade(label="Songs", menu=songs_menu)
menubar.add_cascade(label="Artist", menu=artist_menu)

# ── song list area ────────────────────────────────────────────────────────────
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

# ── now-playing bar ───────────────────────────────────────────────────────────
now_bar=tk.Frame(window, bg=NOW_BG, pady=8)
now_bar.pack(fill="x", side="bottom")

now_label=tk.Label(now_bar, text="♪  Nothing playing", bg=NOW_BG, fg=ACCENT, font=FONT_HEAD)
now_label.pack(pady=(2, 4))

ctrl_frame=tk.Frame(now_bar, bg=NOW_BG)
ctrl_frame.pack()

def make_btn(parent, text, cmd):
    return tk.Button(parent, text=text, command=cmd, bg=SIDEBAR, fg=TEXT, activebackground=ACCENT, activeforeground=BG, font=FONT_MAIN, relief="flat", padx=14, pady=4, cursor="hand2")


# ── helpers ───────────────────────────────────────────────────────────────────
def refresh():
    for w in list_frame.winfo_children():
        w.destroy()

    if playlist["size"]==0:
        tk.Label(list_frame, text="Playlist is empty", bg=BG, fg=SUBTEXT, font=FONT_MAIN).pack(pady=20)
        return

    current=playlist["head"]
    number=1
    while True:
        song=current["data"]
        mins=song["duration"]//60
        secs=song["duration"]%60
        plays=song["play_count"]
        duration=f"{mins}:{secs:02d}"
        text=(f"  {number:>2}.  {song['title']:<38}"
              f"{song['artist']:<28}"
              f"{song['genre']:<12}"
              f"{duration:<7}"
              f"▶ {plays}")

        is_now=(playlist["now_playing"] is not None and playlist["now_playing"] is current)
        row_bg=ACCENT if is_now else (ROW_A if number%2==0 else ROW_B)
        row_fg=BG if is_now else TEXT

        tk.Label(list_frame, text=text, bg=row_bg, fg=row_fg, font=FONT_NOW, anchor="w", padx=6, pady=5).pack(fill="x")

        number+=1
        if current==playlist["tail"]:
            break
        current=current["next"]


def ask(prompt, cast=str):
    val=simpledialog.askstring("Pointlist", prompt, parent=window)
    if val is None:
        return None
    try:
        return cast(val)
    except ValueError:
        messagebox.showerror("Error", f"Expected a number for: {prompt}")
        return None


def pick_song_number(title="Pick a song"):
    refresh()
    return ask(f"{title}\nEnter song number:", int)


# ── playlist menu actions ─────────────────────────────────────────────────────
def do_shuffle():
    if playlist["now_playing"]:
        current_title=playlist["now_playing"]["data"]["title"]
    else:
        current_title=None
    shuffle(playlist)
    if current_title:
        playlist["now_playing"]=search(playlist, "title", current_title)
    refresh()
    messagebox.showinfo("Pointlist", "Playlist shuffled.")

def do_smart_shuffle():
    if playlist["now_playing"]:
        current_title=playlist["now_playing"]["data"]["title"]
    else:
        current_title=None
    smart_shuffle(playlist)
    if current_title:
        playlist["now_playing"]=search(playlist, "title", current_title)
    refresh()
    messagebox.showinfo("Pointlist", "Playlist smart shuffled.")

def do_sortby():
    choice=simpledialog.askstring("Sort By", "Sort by:\n1. Title\n2. Artist\n3. Duration\n4. Genre", parent=window)
    fields={"1": "title", "2": "artist", "3": "duration", "4": "genre"}
    if choice in fields:
        order=simpledialog.askstring("Order", "Order:\n1. Ascending\n2. Descending", parent=window)
        if order not in ("1", "2"):
            return
        descending=order=="2"
        if playlist["now_playing"]:
            current_title=playlist["now_playing"]["data"]["title"]
        else:
            current_title=None
        sortby(playlist, fields[choice], descending)
        if current_title:
            playlist["now_playing"]=search(playlist, "title", current_title)
        refresh()
        messagebox.showinfo("Pointlist", f"Sorted by {fields[choice]} ({'descending' if descending else 'ascending'}).")

playlist_menu.add_command(label="Shuffle", command=do_shuffle)
playlist_menu.add_command(label="Smart Shuffle", command=do_smart_shuffle)
playlist_menu.add_command(label="Sort By", command=do_sortby)


# ── songs menu actions ────────────────────────────────────────────────────────
def do_add():
    title=ask("Song title:")
    if title is None:
        return
    artist=ask("Artist:")
    if artist is None:
        return
    duration=ask("Duration (seconds):", int)
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

def do_remove():
    title=ask("Song title to remove:")
    if title is None:
        return
    node=search(playlist, "title", title)
    if node is None:
        messagebox.showerror("Pointlist", "Song not found.")
        return
    removefromchain(playlist, node)
    delete_node(playlist, node)
    refresh()
    messagebox.showinfo("Pointlist", f"Removed: {title}")

songs_menu.add_command(label="Add Song", command=do_add)
songs_menu.add_command(label="Remove Song", command=do_remove)

# ── artist menu actions ───────────────────────────────────────────────────────
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
        text=(f"  {number}.  {song['title']:<38}{song['genre']:<12}{duration:<7}▶ {song['play_count']}")
        tk.Label(frame, text=text, bg=ROW_A if number%2==0 else ROW_B, fg=TEXT, font=FONT_NOW, anchor="w", padx=6, pady=5).pack(fill="x")
        nodes.append(current)
        number+=1
        if current==playlist["artist_tail"][artist]:
            break
        current=current["artist_next"]

    def play_from_artist():
        num=ask("Enter song number to play:", int)
        if num is None or num<1 or num>len(nodes):
            return
        _play_node(nodes[num-1])
        win.destroy()

    make_btn(win, "▶ Play a Song", play_from_artist).pack(pady=10)

artist_menu.add_command(label="Get Artist Songs", command=do_artist)

# ── playback ──────────────────────────────────────────────────────────────────
def _play_node(node):
    node["data"]["play_count"]+=1
    playlist["now_playing"]=node
    now_label.config(text=f"♪  {node['data']['title']}  —  {node['data']['artist']}")
    if node["data"]["link"]:
        webbrowser.open(node["data"]["link"])
    refresh()

def do_play():
    num=ask("Enter song number to play:", int)
    if num is None or num<1 or num>playlist["size"]:
        return
    current=playlist["head"]
    for _ in range(num-1):
        current=current["next"]
    _play_node(current)

def do_random_skip():
    song=random_skip(playlist)
    _play_node(song)

def do_next():
    np=playlist["now_playing"]
    nxt=np["next"] if (np and np["next"]) else playlist["head"]
    playlist["now_playing"]=nxt
    now_label.config(text=f"♪  {nxt['data']['title']}  —  {nxt['data']['artist']}")
    refresh()

def do_prev():
    np=playlist["now_playing"]
    prv=np["prev"] if (np and np["prev"]) else playlist["tail"]
    playlist["now_playing"]=prv
    now_label.config(text=f"♪  {prv['data']['title']}  —  {prv['data']['artist']}")
    refresh()

def do_play_current():
    if playlist["now_playing"] is None:
        playlist["now_playing"]=playlist["head"]
    _play_node(playlist["now_playing"])

make_btn(ctrl_frame, "▶  Play Song", do_play).pack(side="left", padx=8)
make_btn(ctrl_frame, "⏮  Prev", do_prev).pack(side="left", padx=8)
make_btn(ctrl_frame, "▶  Play", do_play_current).pack(side="left", padx=8)
make_btn(ctrl_frame, "⏭  Next", do_next).pack(side="left", padx=8)
make_btn(ctrl_frame, "▶  Random Skip", do_random_skip).pack(side="left", padx=8)

# ── init ──────────────────────────────────────────────────────────────────────
refresh()
window.mainloop()