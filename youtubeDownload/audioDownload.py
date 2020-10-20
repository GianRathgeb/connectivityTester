# Import module pafy
import pafy

# Get url and create new video object
url = "https://www.youtube.com/watch?v=RxabLA7UQ9k"
video = pafy.new(url)

# Get the best audio from the video
bestAudio = video.getbestaudio()

# Download the audio
bestAudio.download()
print("Downlaoded successfully")