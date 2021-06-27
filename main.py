import sys
import os
import keyboard
from music import song, sheets
from playsound import playsound

# Global variables
# number of characters in a file
numChars = 0
# the read_key is detecting the pressed moment
pressed = True
# which note in a current song will be played
currentNoteIndex = 0
# which song will be played
currentSongIndex = 0
# create object holding all songs
# LIMITATION: songs have to be manually created at the moment
allSongs = song.Song()
allSongs.addSong(sheets.happyBirthDay)
allSongs.addSong(sheets.marysLamb)

# LIMITATION: a sound is played wherever we type (not just terminal)
def pressKey(outputFile, key):
    global numChars, currentNoteIndex, currentSongIndex
    outputFile.write(key)
    print(key, flush=True, end="")
    numChars += 1
    # play new sound
    playsound(os.path.abspath("music/notes/" + allSongs.getCurrentNote(currentSongIndex, currentNoteIndex) + ".mp3"))
    if currentNoteIndex == allSongs.currentSongLength(songIndex=currentSongIndex) - 1:
        currentSongIndex = 0 if currentSongIndex + 1 == allSongs.numberSongs() else currentSongIndex + 1
        currentNoteIndex = 0
    else:
        currentNoteIndex += 1

def pressBackSpace(outputFile):
    global numChars
    if numChars > 0:
        outputFile.truncate(numChars - 1)
        numChars -= 1
        print("\b", flush=True, end="")
        print(" ", flush=True, end="")
        print("\b", flush=True, end="")
    playsound(os.path.abspath("music/beep.mp3"))

# LIMITATION: typing speed cannot be too fast or the key is not correctly detected
# LIMITATION: shift key is not implemented yet
def checkKey(outputFile):
    global pressed
    key = keyboard.read_key()
    if pressed:
        if key == "esc":
            print("")
            return closeFile()
        elif key == "backspace":
            pressBackSpace(outputFile)
        elif key == "space":
            pressKey(outputFile, " ")
        elif key == "enter":
            pressKey(outputFile, "\n")
        elif key == "tab":
            pressKey(outputFile, "\t")
        else:
            pressKey(outputFile, key)
        pressed = False
    else:
        pressed = True
    return False

def closeFile():
    close = input("Close the file (y/n): ")
    while (close.lower() != "y" and close.lower() != "n"):
        print("Invalid! Please enter y or n")
        close = input("Close the file (y/n): ")
    return close.lower() == 'y'

def main():
    # input command
    if len(sys.argv) != 2:
        print("Expect 2 arguments!")
    else:
        global numChars
        # output text file
        outputFileName = sys.argv[1]
        outputFile = open(outputFileName, "a")
        numChars = os.path.getsize(outputFileName)
        # LIMITATION: We can only create a file in the current directory at the moment
        # LIMITATION: This program can only be run on Windows OS
        close = False
        while not close:
            close = checkKey(outputFile)
        # Close the file and display the result file
        outputFile.close()
        os.startfile(outputFileName)

if __name__ == "__main__":
    main()