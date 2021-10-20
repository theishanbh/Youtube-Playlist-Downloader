from __future__ import unicode_literals
import youtube_dl
import os


def filedownloader(save_dir):
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

    print("Download started. Please be patient ...")

    # for loop downloads each link from link provided in f
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        for each in f.readlines():
            try:
                info_dict = ydl.extract_info(each, download=True)
                video_title = info_dict.get('title', None)
                print(video_title + " downloaded.")
            except:
                txtfile.write(each)
        
    print("-----------------------------------------------")
    print("-----------------------------------------------")
    print()
    print(">> All files downloaded!" )
    f.close()
    os.remove("videolinks.txt")
