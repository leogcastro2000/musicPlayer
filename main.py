import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os


musicplayer = tkr.Tk()
musicplayer.title("Music Player")
musicplayer.geometry('450x350')

directory = askdirectory()
os.chdir(directory)
songlist = os.listdir()
playlist = tkr.Listbox(musicplayer, font="Helvetica 12 bold", bg="silver", selectmode=tkr.SINGLE)

for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos = pos + 1

pygame.init()
pygame.mixer.init()


def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.active))
    pygame.mixer.music.play()


def exitMusicPlayer():
    pygame.mixer.music.stop()


def pause():
    pygame.mixer.music.pause()


def unpause():
    pygame.mixer.music.unpause()


Button1 = tkr.Button(musicplayer, width=5, height=3, font="Helvetica 12 bold", text="PLAY", command=play, bg="grey", fg="silver")
Button2 = tkr.Button(musicplayer, width=5, height=3, font="Helvetica 12 bold", text="STOP", command=exitMusicPlayer, bg="grey", fg="silver")
Button3 = tkr.Button(musicplayer, width=5, height=3, font="Helvetica 12 bold", text="PAUSE", command=pause, bg="grey", fg="silver")
Button4 = tkr.Button(musicplayer, width=5, height=3, font="Helvetica 12 bold", text="UNPAUSE", command=unpause, bg="grey", fg="silver")

var = tkr.StringVar
songtitle = tkr.Label(musicplayer, font="Helvetica 12 bold", textvariable=var)

songtitle.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
playlist.pack(fill="both", expand="yes")

musicplayer.mainloop()