from tkinter import messagebox
import os
from tkinter import *
import threading
from tkinter import ttk
from pytube.__main__ import YouTube
import pyttsx3


def speaker(text):
    audio = pyttsx3.init()
    audio.say(text)
    audio.runAndWait()


root = Tk()
root.title("YouTube Downloader 0.0.1")
root.geometry("400x150")
root.minsize(400, 150)
root.maxsize(400, 150)


def Popup():
    PATH = os.getcwd()
    messagebox.showinfo("Download Completed", f"File Location:{PATH}")


pb = ttk.Progressbar(
    root,
    orient='horizontal',
    mode='indeterminate',
    length=280
)


def download():
    label2.grid(row=3, column=0)
    pb.grid(column=1, row=3, columnspan=2, padx=10, pady=20)
    url = input_url.get()
    if url == "":
        messagebox.showinfo("Warning", "Enter The URL")
        pb.destroy()
        speaker("Please Enter The URL")
        label2.destroy()
    else:
        youtube = YouTube(url)
        video =  youtube.streams.get_highest_resolution()
        PATH = os.getcwd()
        video.download(PATH)
        if video.on_progress:
            Popup()
            root.destroy()
            pb.destroy()
            speaker("Exiting")


def thread():
    t1 = threading.Thread(target=download)
    t1.start()
    pb.start()


label1 = Label(root, text='Video URL : ')
label1.grid(row=0, column=0, padx=10, pady=10)


input_url = Entry(root, width=45)
input_url.grid(row=0, column=1)


download_button = Button(root, text='Download', width=25, command=thread)
download_button.grid(row=2, column=1, padx=10, pady=10)


label2 = Label(root, text='Progress : ')

root.mainloop()
