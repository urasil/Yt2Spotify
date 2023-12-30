from gui import YoutubeDownloaderApp
import tkinter as tk

#TODO:: create a .exe using pyinstaller
def main():
    root = tk.Tk()
    #https://www.youtube.com/watch?v=OrGWNwhs5gA
    window_width = 400
    window_height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    YoutubeDownloaderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
