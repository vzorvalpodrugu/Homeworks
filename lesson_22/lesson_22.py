class Playlist:
    """
    Playlist class representing a playlist with methods for adding and removing beats.
    """
    def __init__(self, name, mood):
        """
        Initialize a playlist with a name and mood.
        """
        self.name = name
        self.mood = mood
        self.beats = []

    def __str__(self):
        beat_names = ''.join([bet.name for bet in self.beats])
        return f"Playlist name: {self.name}\nMood: {self.mood}\nQuantity beats: {len(self.beats)}\nBeats: {beat_names}"


    def __iadd__(self, other: "Beat"):
        """
        Add another Beats object to the current playlist.
        """
        self.beats.append(other)
        return self

class Beat:
    """
    Beats class representing individual beats in a playlist.
    """
    def __init__(self, name: str, author: str, bpm: int, duration: int):
        """
        Initialize a beat with a name, author, BPM, and duration.
        """
        self.name = name
        self.author = author
        self.bpm = bpm
        self.duration = duration

    def __str__(self):
        return f"Beat name: {self.name}\nAuthor: {self.author}\nBPM: {self.bpm}\nDuration: {self.duration} ms"

Sweety = Playlist("Sweety", "kind")
print(Sweety)
Sweety += Beat("Kind of Music", "Unnamed", 140, 300)
Sweety += Beat("Love is a Stranger", "Johnny Cash", 130, 400)
print(Sweety)

from dataclasses import dataclass, field

@dataclass(order=True)
class MusicComposition:
    name: str = field(compare=False)
    author: str = field(compare=False)
    bpm: int = field(compare=False)
    duration: int

track1 = MusicComposition("Baby", "Gaga", 140, 300)
track2 = MusicComposition("Crash", "Gaga", 123, 323)
track3 = MusicComposition("Ballen", "Bones", 90, 180)

track_list = [track1, track2, track3]

print(track1 > track2)
print(track3 < track1)

print(track_list)
track_list.sort(reverse=True)
print(track_list)


