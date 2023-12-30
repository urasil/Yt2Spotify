class VideoException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class DownloadException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)