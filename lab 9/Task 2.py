import tkinter as tk
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Keyboard Music Player")
        self.current_track = 0
        self.tracks = ["Ariana_Grande_-_7_rings_61522506.mp3", "Ariana_Grande_Mac_Miller_Alex_Ghenea_-_Into_You_70561185.mp3", "The_Weeknd_-_Die_For_You_47829086.mp3"]  # Replace with your music file paths

        self.setup_ui()
        self.setup_audio()

    def setup_ui(self):
        self.play = tk.Button(self.root, text="Play", command=self.play_music)
        self.play.pack()

        self.stop = tk.Button(self.root, text="Stop", command=self.stop_music)
        self.stop.pack()

        self.previous = tk.Button(self.root, text="Previous", command=self.previous_track)
        self.previous.pack()

        self.next = tk.Button(self.root, text="Next", command=self.next_track)
        self.next.pack()

        self.root.bind("<KeyPress>", self.key_pressed)

    def setup_audio(self):
        pygame.mixer.init()
        self.load_track()
    def load_track(self):
        pygame.mixer.music.load(self.tracks[self.current_track])
    def play_music(self):
        pygame.mixer.music.play()
    def stop_music(self):
        pygame.mixer.music.stop()
    def previous_track(self):
        self.current_track -= 1
        if self.current_track < 0:
            self.current_track = len(self.tracks) - 1
        self.load_track()
        self.play_music()
    def next_track(self):
        self.current_track += 1
        if self.current_track >= len(self.tracks):
            self.current_track = 0
        self.load_track()
        self.play_music()
    def key_pressed(self, event):
        key = event.keysym
        if key == "Up":
            self.play_music()
        elif key == "Down":
            self.stop_music()
        elif key == "Left":
            self.previous_track()
        elif key == "Right":
            self.next_track()
def main():
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
if __name__ == "__main__":
    main()
