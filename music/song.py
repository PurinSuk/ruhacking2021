class Song:
    def __init__(self):
        self.allSongs = []

    def addSong(self, arr):
        self.allSongs.append(arr)

    def getCurrentNote(self, songIndex, noteIndex):
        return self.allSongs[songIndex][noteIndex]

    def currentSongLength(self, songIndex):
        return len(self.allSongs[songIndex])

    def numberSongs(self):
        return len(self.allSongs)