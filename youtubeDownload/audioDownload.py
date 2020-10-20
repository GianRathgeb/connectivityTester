# Import module pafy
import pafy

# Get url and create new video object
url = "https://www.youtube.com/watch?v=kQoxbDOWjf4"
video = pafy.new(url)

# Get the best audio from the video
bestAudio = video.getbestaudio()

# Download the audio
bestAudio.download()