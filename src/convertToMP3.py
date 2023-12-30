import subprocess
import os

#Path only necessary if ffmpeg is not in PATH environment variable
#I have ffmpeg in PATH but it still fails hence I am adding the option to manually add the path to ffmpeg
PATH = "C:\\Users\\urasa\\Documents\\ffmpeg\\bin\\ffmpeg.exe"

class ConvertToMP3:
    def __init__(self, inputFile, outputFile):
        self.inputFile = inputFile
        self.outputFile = outputFile
        self.path = PATH

        if not os.path.exists(self.inputFile):
            raise FileNotFoundError("Conversion cannot continue because input file does not exist: ", inputFile)
        
    def convert(self):
        try:
            ffmpegCommand = [
            "ffmpeg",
            '-i', self.inputFile,
            '-vn',
            '-acodec', 'libmp3lame',
            '-ab', '192k',
            '-ar', '44100',
            '-y',
            self.outputFile
        ]
            subprocess.run(ffmpegCommand, check=True)
            print("MP3 conversion complete, file saved to: ", self.outputFile)
        except:
            try:
                print("ffmpeg not found in PATH, trying to use manually added path (PATH variable in convertToMP3.py neeeds absolute path to ffmpeg.exe)")
                ffmpegCommand = [
                self.path,
                '-i', self.inputFile,
                '-vn',
                '-acodec', 'libmp3lame',
                '-ab', '192k',
                '-ar', '44100',
                '-y',
                self.outputFile
            ]
                subprocess.run(ffmpegCommand, check=True)
                print("MP3 conversion complete, file saved to: ", self.outputFile)
            except subprocess.CalledProcessError as error:
                print("Conversion failed: ", error)
            except PermissionError as error:
                print("You do not have permission to the music folder", error)




