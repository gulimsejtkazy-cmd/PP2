import pygame
import os

class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()

        base_path = os.path.dirname(os.path.abspath(__file__))
        self.music_folder = os.path.join(base_path, "music")

        self.playlist = self.load_music()
        self.index = 0

        print("Playlist:", self.playlist)

    def load_music(self):
        files = []

        for file in os.listdir(self.music_folder):
            if file.endswith(".wav") or file.endswith(".mp3"):
                files.append(os.path.join(self.music_folder, file))

        files.sort()
        return files

    def play(self):
        if not self.playlist:
            print("No music found")
            return

        pygame.mixer.music.load(self.playlist[self.index])
        pygame.mixer.music.play()
        print("Playing:", self.get_name())

    def stop(self):
        pygame.mixer.music.stop()
        print("Stopped")

    def next(self):
        if not self.playlist:
            return

        self.index = (self.index + 1) % len(self.playlist)
        self.play()

    def prev(self):
        if not self.playlist:
            return

        self.index = (self.index - 1) % len(self.playlist)
        self.play()

    def get_name(self):
        if not self.playlist:
            return "No music"
        return os.path.basename(self.playlist[self.index])