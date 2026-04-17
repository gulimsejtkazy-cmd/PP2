import pygame
import os

class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()

        base = os.path.dirname(os.path.abspath(__file__))

        self.tracks = [
            {"name": "Mia Martina - Beast", "file": os.path.join(base, "music/track1.ogg")},
            {"name": "Tame Impala - Dracula", "file": os.path.join(base, "music/track2.ogg")},
            {"name": "Noah Cyrus - Again", "file": os.path.join(base, "music/track3.ogg")}
        ]

        self.index = 0

        self.start_time = 0
        self.length = 1  # длина трека (сек)

    def load_length(self):
        path = self.tracks[self.index]["file"]
        sound = pygame.mixer.Sound(path)
        self.length = sound.get_length()

    def get_name(self):
        return self.tracks[self.index]["name"]

    def play(self):
        path = self.tracks[self.index]["file"]

        if not os.path.exists(path):
            print("❌ FILE NOT FOUND:", path)
            return

        pygame.mixer.music.load(path)
        pygame.mixer.music.play()

        self.load_length()
        self.start_time = pygame.time.get_ticks()

    def stop(self):
        pygame.mixer.music.stop()

    def next(self):
        self.index = (self.index + 1) % len(self.tracks)
        self.play()

    def prev(self):
        self.index = (self.index - 1) % len(self.tracks)
        self.play()

    def get_progress(self):
        if self.length == 0:
            return 0

        current_time = (pygame.time.get_ticks() - self.start_time) / 1000
        return min(current_time / self.length, 1)
