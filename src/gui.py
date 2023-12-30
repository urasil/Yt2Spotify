import tkinter as tk
from tkinter import ttk
from youtubeDownload import YouTubeDownload
from convertToMP3 import ConvertToMP3
import getpass
import os

class YoutubeDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.videoName = ""
        self.root.title("Yt2Spotify")
        self.root.configure(bg="black")
        self.root.resizable(False, False)

        self.style = ttk.Style()
        self.style.configure("TLabel", foreground="white", background="black")
        self.style.configure("TEntry", foreground="black", background="black")
        self.style.configure("TButton", foreground="black", background="black")
        self.style.configure("TCheckbutton", foreground="white", background="black")

        self.urlLabel = ttk.Label(self.root, text="Enter YouTube URL:")
        self.urlLabel.pack(pady=10)

        self.urlEntry = ttk.Entry(self.root, width=50)
        self.urlEntry.pack(pady=10)

        self.downloadButton = ttk.Button(self.root, text="Download", command=self.downloadVideo)
        self.downloadButton.pack(pady=10)

        self.deleteVideoVar = tk.IntVar(value=0)
        self.optionalDelete = ttk.Checkbutton(self.root, text="Delete video from downloads folder within project directory", variable=self.deleteVideoVar)
        self.optionalDelete.pack(pady=10)

    def downloadVideo(self):
        Video = YouTubeDownload(self.urlEntry.get())
        windowsUser = str(getpass.getuser())
        self.videoName = Video.download()
        Converter = ConvertToMP3(f"downloads\\{self.videoName}.mp4", f"C:\\Users\\{windowsUser}\\Music\\{self.videoName}.mp3")
        Converter.convert()
        self.urlEntry.delete(0, tk.END)

        if self.deleteVideoVar.get() == 1:
            self.deleteVideo()

    def deleteVideo(self):
        if self.videoName != "":
            os.remove(f"downloads\\{self.videoName}.mp4")
            

