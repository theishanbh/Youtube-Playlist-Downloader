from src import filedownloader
from src import linkscraper

yt_link = f"https://www.youtube.com/playlist?list=PLs8fgrGfxenIv9YudSvj046n_INuldCa2"
save_dir = 'E:\Music\speedDownload'

linkscraper.linkscraper(yt_link)
filedownloader.musicdownloader(save_dir)