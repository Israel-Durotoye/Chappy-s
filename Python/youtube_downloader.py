from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry("520x300")
root.resizable(True, True)
root.title("Youtube Video Downloader")

Label(root, text = "Youtube Video Downloader", font = "chalkboard 20 bold").pack()
link = StringVar()

Label(root, text = "Paste Link Here:", font = "chalkboard 15 bold").place(x = 160, y = 60)
link_enter = Entry(root, width = 50, textvariable = link).place(x = 32, y = 90)

def downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x = 180, y = 210)

Button(root, text = 'DOWNLOAD', font = 'arial 15 bold', bg = 'pale violet red', padx = 2, command = downloader).place(x = 180, y = 150)

root.mainloop()
