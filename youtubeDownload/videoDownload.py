# Import module pafy
import pafy

# Full video url and new video object
url = "https://www.youtube.com/watch?v=kQoxbDOWjf4"
video = pafy.new(url)

# Get all aviable video streams
streams = video.streams

print("Quality options:")
# Print every aviable video stream
for i in streams:
    print(i)

# Get the best resolution
bestRest = video.getbest()
# Print the best resolution
print(bestRest.resolution, bestRest.extension)

# Downlaod the video
bestRest.download()
# Print successfull message
print("Video downloaded successfully")