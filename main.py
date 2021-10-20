from src.filedownloader import *
from src.linkscraper import *
from src.gui import *

def main():
    g = GUI();
    while True:
        event, values = g.window.Read()
        if(event == sg.WIN_CLOSED or event == 'Exit'):
            break
        linkscraper(values['playlistLink'])
        filedownloader(values['PATH'])
main()