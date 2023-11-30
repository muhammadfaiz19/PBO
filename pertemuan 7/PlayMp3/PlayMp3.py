import tkinter as tk
from tkinter import filedialog
import pygame

class MP3Player:
    def __init__(self, master):
        self.master = master
        self.master.title("MP3 Player")
        self.master.geometry("300x250")
        self.master.configure(bg='#3498db')

        self.title_label = tk.Label(self.master, text="Muhammad Faiz", font=("Helvetica", 16), bg='#3498db', fg='white')
        self.title_label.pack(pady=10)

        self.current_file_label = tk.Label(self.master, text="Now Playing: ", font=("Helvetica", 12), bg='#3498db', fg='white')
        self.current_file_label.pack(pady=5)

        self.open_button = tk.Button(self.master, text="Open", command=self.open_file_dialog, bg='#2ecc71', fg='white', padx=20, pady=10)
        self.open_button.pack(pady=10)

        self.play_button = tk.Button(self.master, text="Play", command=self.play_sound, bg='#2ecc71', fg='white', padx=20, pady=10)
        self.play_button.pack(pady=5)

        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_sound, bg='#e74c3c', fg='white', padx=20, pady=10)
        self.stop_button.pack(pady=10)

        self.file_path = None

    def open_file_dialog(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        if self.file_path:
            self.current_file_label.config(text=f"Now Playing: {self.file_path}")

    def play_sound(self):
        if self.file_path:
            pygame.mixer.init()
            pygame.mixer.music.load(self.file_path)
            pygame.mixer.music.play()

    def stop_sound(self):
        pygame.mixer.music.stop()

def main():
    root = tk.Tk()
    mp3_player = MP3Player(root)
    root.mainloop()

if __name__ == "__main__":
    main()
