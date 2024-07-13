import pafy 

url = input("Paste url here :")
video_data = pafy.new(url)
streams = video_data.streams
print(streams)
best = video_data.getbest(preftype='mp4')
best.download
