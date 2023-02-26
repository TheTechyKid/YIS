# YIS

from pprint import pformat
from tkinter import *
from fast_youtube_search import search_youtube
import customtkinter as CTK
from pytube import YouTube
from os import startfile

CTK.set_appearance_mode("System")
CTK.set_default_color_theme("blue")

VIDEO_DIR = "C:\\Video"

class App(CTK.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x640")
        self.title("YI")
        
        class Url():
            def GetTitle(url):
                return YouTube(f"{url}").title
            
            def GetDes(url):
                return YouTube(f"{url}").description
            
            def GetThum(url):
                return YouTube(f"{url}").thumbnail_url
        
        def clearWin():
            for child in self.winfo_children():
                child.destroy()
        
        def onClickPlY():
            
            url = LnKVar.get().replace("https://www.youtube.com/watch?v=","")
            
            charters = ["|", "'", "?", ",", ":", "~", "#", "$", "%", "^", "/", '"']
            
            YouTube("https://www.youtube.com/watch?v="+url).streams.get_highest_resolution().download(output_path=r"C:\Video")
            title = Url.GetTitle("https://www.youtube.com/watch?v="+url)
            for x in range(len(charters)):
                title = title.replace(charters[x], "")
            print(title)
            startfile("{}\\{}.mp4".format(VIDEO_DIR, title))
            
        def onClickLnK():
            urlTitle = LnKVar.get()
            CTK.CTkLabel(master=self, text=Url.GetTitle("https://www.youtube.com/watch?v="+urlTitle), font=("Arial",25)).pack()
            DesBox.insert("0.0", Url.GetDes("https://www.youtube.com/watch?v="+urlTitle))

        def YS():
            clearWin()
            self.title("YS")
            
            def YScode():
                
                YsEntry = StringVar()
                             
                def Search():
                    YsEntryGet = YsEntry.get()
                    YsTxtBox.delete("0.0", "end")
                    search = search_youtube(YsEntryGet)
                    
                    for videos in search:
                        
                        parsed = videos
                        prettified = pformat(parsed)
                        
                        YsTxtBox.insert("0.0", prettified)
                        YsTxtBox.insert("0.0", "\n")
                        YsTxtBox.insert("0.0", "\n")
                
                # Thingy
                YsLabel = CTK.CTkLabel(master=self, text="YI", font=("Arial", 45))
                YsEntry = CTK.CTkEntry(master=self, width=300, placeholder_text="Search...", textvariable=YsEntry)
                YsBtN = CTK.CTkButton(master=self, text="Search", command=Search, width=70)
                YsTxtBox = CTK.CTkTextbox(master=self, width=760, height=420)
                YsReturnBtN = CTK.CTkButton(master=self, text="YI", command=YI)
                
                # Placement
                YsLabel.place(x=350, y=10)
                YsEntry.place(x=200, y=70)
                YsBtN.place(x=482+20, y=70)
                YsTxtBox.place(x=20, y=200)
                YsReturnBtN.place(x=10, y=10)
            
            YScode()
        
        def YI():
            self.title("YI")
            
            clearWin()
            
            global LnKVar, DesBox
            
            # The name of the vid
            LnKVar = StringVar()
            LnK = CTK.CTkEntry(master=self, width=250, textvariable=LnKVar)
            SubMitBtN = CTK.CTkButton(master=self, text="Submit", command=onClickLnK)
            
            # Leave
            GoBtN = CTK.CTkButton(master=self, text="YS", command=YS)
            
            # Description Box
            DesBox = CTK.CTkTextbox(master=self, width=350, height=320)
            
            # Play
            PlayBtN = CTK.CTkButton(master=self, text="Play", command=onClickPlY, width=760)
            
            # The placement
            LnK.place(x=270, y=50)
            SubMitBtN.place(x=325, y=50+30)
            DesBox.place(x=20, y=300)
            PlayBtN.place(x=20, y=250)
            GoBtN.place(x=640, y=595)
        
        YI()

if __name__ == "__main__":
    app = App()
    app.mainloop()
