# Import module pafy
import pafy

# Full video url and new video object
# https://www.youtube.com/watch?v=kQoxbDOWjf4
def download():
    url = input("Enter url from video: ")

    video = pafy.new(url)

    # Get all aviable video streams
    streams = video.allstreams

    print("Quality options:")
    # Print every aviable video stream
    for i, e in enumerate(streams):
        print(f"Stream {i}: {str(e).split('@')[1]}")
    choice = input("Choose video stream: ")
    # Get the best resolution
    #res = video.getbest()

    res = streams[int(choice)]
    # Print the best resolution
    print(res.resolution, res.extension)

    # Downlaod the video
    res.download()
    # Print successfull message
    print("Video downloaded successfully")

    t = input("Do you want to download another video? y/n [n] ")
    if t == "y" or t == "Y":
        download()
    else: exit()


download()