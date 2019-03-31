from pytube import YouTube
import os
path = os.getcwd()
YouTube('https://www.youtube.com/watch?v=Py5WNFpT5F4').streams.first().download(output_path=path+'\Playlist')
