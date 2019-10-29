# !/usr/bin/python3

from tkinter import *
from tkinter.font import Font
import os
from PIL import Image, ImageTk
import numpy as np

class RPI_GUI:
    global win
    def __init__(self, win):
        self.win = win
        win_w, win_h = 640, 360
        win.geometry('{}x{}+0+0'.format(win_w, win_h)) #win_w, win_h, origin_x, origin_y
        win.attributes('-fullscreen', True)
        win.title('guiDANCE --Powered by tkinter v8.6')
        self.font = Font(family='Helvetica', size=12, weight='bold')
#        win.grid_columnconfigure(0, weight=1)
        win.grid_columnconfigure(1, weight=1)
#        win.grid_columnconfigure(2, weight=1)

        isFS = False

        self.exit = Button(win, 
                           text='Quit', 
                           font=self.font, 
                           command=self.quitPgm, 
                           bg='cyan', 
                           compound='c').grid(row=1, column=0, sticky='nsew')
        
        self.title = Label(win, 
                           text='guiDANCE (Tkinter v8.6)').grid(row=0, column=1, sticky='nsew')
        
        self.kill = Button(win, 
                           text='Kill', 
                           font=self.font, 
                           command=self.killCnfm, 
                           bg='red', 
                           compound='c').grid(row=1, column=2, sticky='nsew')
        
        self.print_cmd = Label(win,
                               borderwidth=2, 
                               relief="sunken",
                               font=self.font).grid(row=1, column=1, sticky='nsew')
        
        self.showIm = False
        self.saitama = Button(win, 
                              text='Show Saitama',  
                              font=self.font, 
                              command=self.pressButton, 
                              bg='bisque2', 
                              compound='c').grid(row=2, column=1, sticky='nsew')
    def quitPgm(self):
        self.print_cmd = Label(win,
                               text='Quitting Interface',
                               borderwidth=2, 
                               relief="sunken",
                               font=self.font).grid(row=1, column=1, sticky='nsew')
        win.destroy()
        
    def killPgm(self):
        cnfm = Label(win,
                     text='Killing Device...',
                     borderwidth=2, 
                     relief="sunken",
                     font=self.font).grid(row=1, column=1, sticky='nsew')
        print('Device Shutdown')
        #os.system('sudo shutdown -r now')
    
    def pressButton(self):
#        global disp
        if not self.showIm:
            self.print_cmd = Label(win,
                                   text='Displaying Saitama...',
                                   borderwidth=2, 
                                   relief="sunken",
                                   font=self.font).grid(row=1, column=1, sticky='nsew')
            self.showIm = True
            photo = ImageTk.PhotoImage(Image.open('saitama.jpg').resize((450,200), Image.ANTIALIAS))
            self.disp = Label(win, image=photo)
            self.disp.image = photo
            self.disp.grid(row=3, column=1, sticky='nsew') 
        else:
            self.print_cmd = Label(win,
                                   text='Removing Saitama...',
                                   borderwidth=2, 
                                   relief="sunken",
                                   font=self.font).grid(row=1, column=1, sticky='nsew')
            self.showIm = False
            self.disp.grid_forget()
            
    def killCnfm(self):
        win2=Toplevel(self.win)
        win_w, win_h = 640, 360
        win2.geometry('{}x{}+0+0'.format(win_w, win_h)) #win_w, win_h, origin_x, origin_y
        win2.attributes('-fullscreen', True)
        win2.title('guiDANCE --Powered by tkinter v8.6')
        self.font = Font(family='Helvetica', size=12, weight='bold')
        win2.grid_columnconfigure(0, weight=1)
        win2.grid_columnconfigure(1, weight=1)
        win2.grid_columnconfigure(2, weight=1)

        isFS = False
        
        self.kill = Label(win2, 
                          text='Kill', 
                          font=self.font, 
#                          borderwidth=2,
                          relief='raised',
                          bg='gray').grid(row=1, column=2, sticky='nsew')

#        self.exit = Button(win2, 
#                           text='Quit', 
#                           font=self.font, 
#                           command=self.quitPgm, 
#                           bg='cyan', 
#                           compound='c').grid(row=1, column=0, sticky='nsew')
        
        self.title = Label(win2, 
                           text='guiDANCE (Tkinter v8.6)').grid(row=0, column=1, sticky='nsew')
        
        self.print_cmd = Label(win2,
                               borderwidth=2,
                               text='Confirm Kill?',
                               relief="sunken",
                               font=self.font).grid(row=1, column=1, sticky='nsew')
        
        self.cnfmbn = Button(win2, 
                              text='Yes',  
                              font=self.font, 
                              command=self.killPgm, 
                              bg='red', 
                              compound='c').grid(row=2, column=1, rowspan=2, sticky='nsew')
        
        backbn = Button(win2, 
                        text='Back', 
                        font=self.font, 
                        command=win2.destroy, 
                        bg='blue', 
                        compound='c').grid(row=2, column=0, rowspan=2, sticky='nsew')
        
win = Tk()
my_gui = RPI_GUI(win)
win.mainloop()