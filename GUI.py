import tkinter as tk

window = tk.Tk()
window.title("Pointlist")
window.geometry("900x600")

# Top bar
top_frame = tk.Frame(window, bg="navy", height=50)
top_frame.pack(fill="x")

#title label
title_label = tk.Label(top_frame, text="🎵 Pointlist", bg="navy", fg="white", font=("Arial", 18, "bold"))
title_label.pack(side="left", padx=15, pady=10)

# Song list
list_frame = tk.Frame(window, bg="black")
list_frame.pack(fill="both", expand=True)

# Bottom bar
bottom_frame = tk.Frame(window, bg="navy", height=100)
bottom_frame.pack(fill="x")

#now playing
now_playing_label = tk.Label(bottom_frame, text="Now Playing: Nothing", bg="navy", fg="white", font=("Arial", 12))
now_playing_label.pack(pady=(10, 5))

#buttons
controls_frame = tk.Frame(bottom_frame, bg="navy")
controls_frame.pack()

prev_button = tk.Button(controls_frame, text="⏮ Prev", width=10)
prev_button.pack(side="left", padx=10)

play_button = tk.Button(controls_frame, text="▶ Play", width=10)
play_button.pack(side="left", padx=10)

next_button = tk.Button(controls_frame, text="⏭ Next", width=10)
next_button.pack(side="left", padx=10)

window.mainloop()