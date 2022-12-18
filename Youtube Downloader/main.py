from pytube import YouTube
def Download(link):
  youtubeObject = YouTube(link)
  youtubeObject = youtubeObject.streams.get_highest_resolution()
  try:
      youtubeObject.download()
  except:
    print("Got an error in downloading your youtube video")
  print("Download is completed ! Enjoy !")

link = input("Enter your Youtube link here !!  URL: ")
Download(link)