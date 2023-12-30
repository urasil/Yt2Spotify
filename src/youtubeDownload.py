from pytube import YouTube
import os
from customExceptions import VideoException, DownloadException

class YouTubeDownload:
    def __init__(self, link):
        self.link = link
        try:
            self.video = YouTube(self.link)
        except:
            raise VideoException("Video does not exist")
    def download(self):
        videoStream = self.video.streams.get_lowest_resolution()
        videoName = self.handleVideoName(str(videoStream.title))
        try:
            videoStream.download(output_path="downloads", filename=f"{videoName}.mp4")
        except:
            raise DownloadException("The video exists however the download failed")
        return videoName

    def handleVideoName(self, videoName):
        videoName = videoName.replace(" ", "_")
        return videoName

