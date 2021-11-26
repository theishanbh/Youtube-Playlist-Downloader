import PySimpleGUI as sg
sg.theme('DarkBlue3')

availableFormats = ["mp3", "wav","mp4"]

class GUI:
    def __init__(self):
        self.layout = [
            # first row
            [sg.Text('Enter playlist link',size=(10,1)),
             sg.Input('https://www.youtube.com/playlist?list=',size=(68,1),key='playlistLink'),
             sg.Combo(availableFormats,'mp3', size=(8,1), key='format'),
             sg.Button("Exit",size=(8,1))],
            # second row
            [sg.Text('Root Path',size=(10,1)), 
             sg.Input('C:/',size=(55,1),key='PATH'), 
             sg.FolderBrowse('Browse Folder',size=(15,1)), 
             sg.Button("Download",size=(15,1),bind_return_key=True)],
            # third row
            [sg.Output(size=(100,30))]
        ]
        self.window = sg.Window('Youtube Downloader').Layout(self.layout)
