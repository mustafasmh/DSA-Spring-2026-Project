# Pointlist - Music Playlist Manager

A comprehensive music playlist manager built with Python using a custom Doubly Linked List data structure. Features include song management, artist and genre tracking, playback statistics, and a graphical user interface.

---

## 📋 Project Overview

**Pointlist** is a terminal and GUI-based music playlist management system that allows users to:
- Add, remove, and update songs in a playlist
- Track songs by artist and genre using parallel linked chains
- View playback statistics (most played songs, top artists, favorite genres)
- Navigate through a visually appealing Tkinter-based interface

---

## 👥 Team

- **Ayaan Niazi**
- **Tooba Zehra**
- **Sayed Mustafa Hussain**

---

## 🏗️ Project Structure

```
DSA-Spring-2026-Project/
├── DLLadt.py          # Core Doubly Linked List ADT implementation
├── playlist.py        # Playlist management functions
├── GUI.py             # Tkinter-based graphical user interface
├── test_playlist.py   # Test file with sample data
└── README.md          # This file
```

---

## 📂 File Descriptions

### DLLadt.py - Core Data Structure
This file implements a **Doubly Linked List** from scratch, serving as the foundation of the entire playlist system.

**Key Features:**
- `create_node(data)` - Creates a new node with pointers for:
  - `prev`, `next` - Main playlist navigation
  - `artist_next` - Parallel chain for artist-based traversal
  - `genre_next` - Parallel chain for genre-based traversal
- `create_list()` - Initializes playlist with head, tail, and auxiliary chains
- `insertEnd()`, `insertStart()`, `insertMiddle()` - Various insertion methods
- `delete_node(lst, node)` - Removes a node from the list
- Helper functions like `to_seconds(minutes, seconds)` for duration conversion

**Why Doubly Linked List?**
- O(1) insertion and deletion at both ends
- Efficient backward traversal
- Enables parallel chains for artist/genre organization

---

### playlist.py - Playlist Management
This module provides high-level functions for managing the playlist.

**Key Functions:**
- `create_song(title, artist, duration, genre, link)` - Creates a song node with metadata
- `create_playlist()` - Initializes a new playlist
- `add_song(playlist, title, artist, duration, genre, link)` - Adds a song to the playlist
- `remove_song(playlist, title, artist)` - Removes a song by title and artist
- `update_song(playlist, node, field, new_value)` - Updates song fields (artist, genre, etc.)
- `display_playlist(playlist)` - Prints all songs in the playlist
- `artist_chain(playlist, node)` - Maintains parallel artist-linked chain
- `genre_chain(playlist, node)` - Maintains parallel genre-linked chain

**Data Structure for Song:**
```python
{
    "title": str,
    "artist": str,
    "duration": int (seconds),
    "genre": str,
    "play_count": int,
    "link": str (YouTube URL)
}
```

---

### GUI.py - Graphical User Interface
A Tkinter-based GUI that provides a modern, dark-themed interface for the playlist.

**Features:**
- Dark theme with purple accent colors
- Scrollable song list
- Now-playing bar at the bottom
- Dropdown menus for Playlist, Songs, Artist, and Stats
- Statistics windows showing:
  - Top 3 Songs (with fun flavor text)
  - Top 3 Artists
  - Top 3 Genres

**Color Scheme:**
- Background: `#0d0d0d` (near black)
- Sidebar: `#111111`
- Accent: `#854ef1` (purple)
- Text: `#e8e8e8`

---

### test_playlist.py - Testing & Demo
Contains sample song data for testing the playlist system.

**Sample Data Includes:**
- Led Zeppelin, Tool, Opeth (Metal)
- Miles Davis, Emily Remler (Jazz)
- Burial, Nine Inch Nails (Ambient)
- Childish Gambino, MF DOOM (R&B/Hip-Hop)
- And many more...

---

## 🚀 How to Run

### Option 1: Run the GUI
```bash
python GUI.py
```

### Option 2: Run the Test File
```bash
python test_playlist.py
```

---

## 🔧 Key Implementation Details

### Parallel Chaining
The playlist uses **parallel linked chains** to enable efficient querying by:
- **Artist**: All songs by an artist are linked via `artist_next` pointers
- **Genre**: All songs of a genre are linked via `genre_next` pointers

This allows O(n) traversal for finding all songs by a specific artist or genre without searching the entire playlist.

### Time Complexity
| Operation | Complexity |
|-----------|------------|
| Add song (end) | O(1) |
| Remove song | O(n) |
| Search by title/artist | O(n) |
| Get songs by artist | O(n) |
| Get songs by genre | O(n) |

---

## 📦 Dependencies

- Python 3.x
- Tkinter (included with Python standard library)
- webbrowser (for opening YouTube links)

---

## 🎵 Sample Songs Included

The project comes pre-loaded with songs from various genres:
- **Rock**: Led Zeppelin, John Mayer
- **Metal**: Tool, Opeth
- **Jazz**: Miles Davis, Emily Remler, Yussef Dayes
- **Ambient**: Burial, Nine Inch Nails
- **R&B**: Childish Gambino, Joji
- **Rap**: MF DOOM
- **Pop**: Fleetwood Mac, ABBA
- **Qawwali**: Nusrat Fateh Ali Khan

---

## 📝 License

This project was created for the Data Structures and Algorithms course (Spring 2026).