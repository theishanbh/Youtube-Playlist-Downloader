from __future__ import unicode_literals
import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}

txtfile = open("unabletodownload.txt", "w")

f = open("videolinks.txt", "r")
# for loop downloads each link from link provided in f
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    for each in f.readlines():        
        try:
            ydl.download([each])
        except:
            txtfile.write(each)
    # ydl.download(["https://www.youtube.com/watch?v=Zd8D5F_tSjc"])
f.close()


# from youtube_dl import YoutubeDL
# ydl = YoutubeDL()
# ydl.add_default_info_extractors()
# info = ydl.extract_info('https://www.youtube.com/watch?v=KT3TGp5rr-o', download=True)
