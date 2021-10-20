import os
from __future__ import unicode_literals
import youtube_dl

# takes input for saving directory
save_dir = 'E:\Music\speedDownload'
def musicdownloader(save_dir):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': save_dir + '/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }

    txtfile = open("unabletodownload.txt", "w")

    f = open("videolinks.txt", "r")
    # txt files that stores all the videolinks


    # for loop downloads each link from link provided in f
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        for each in f.readlines():        
            try:
                ydl.download([each])
            except:
                txtfile.write(each)
    os.remove("videolinks.txt")
    f.close()
