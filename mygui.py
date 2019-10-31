# !/usr/bin/python3

from tkinter import *
from tkinter.font import Font
import os
from PIL import Image, ImageTk
import numpy as np
import datetime

class RPI_GUI:
    global win, CoreTempVar
    def __init__(self, win):
        self.win = win
        win_w, win_h = 640, 360
        self.win.geometry('{}x{}+0+0'.format(win_w, win_h)) #win_w, win_h, origin_x, origin_y
#        self.win.attributes('-fullscreen', True)
        self.win.title('guiDANCE --Powered by tkinter v8.6')
        self.font = Font(family='Helvetica', size=12, weight='bold')
        self.win.grid_columnconfigure(0, weight=1)
        self.win.grid_columnconfigure(1, weight=1)
        self.win.grid_columnconfigure(2, weight=1)
        self.win.grid_columnconfigure(3, weight=1)
        self.win.grid_columnconfigure(4, weight=1)
#        self.win.grid_rowconfigure(0, weight=1)
#        self.win.grid_rowconfigure(1, weight=1)
        self.win.grid_rowconfigure(2, weight=1)
        self.win.grid_rowconfigure(3, weight=1)
        self.win.grid_rowconfigure(4, weight=1)

        self.title = Label(self.win, 
                           text='guiDANCE (Tkinter v8.6)').grid(row=0, columnspan=3, sticky='nse')
        self.datetime = Label(self.win,
                              text=str(datetime.datetime.now()).split('.')[0]).grid(row=0, column=3, columnspan=2, sticky='nse')
        
        # temp code exit button used during testing
#        self.exit = Button(self.win, 
#                           text='Quit', 
#                           font=self.font, 
#                           command=self.quitPgm,
#                           bg='cyan', 
#                           compound='c').grid(row=1, column=0, sticky='nsew')
        self.top_left = Label(self.win,
                              text='       ').grid(row=1, column=0, sticky='nsew')
        
        self.kill = Button(self.win, 
                           text='Kill', 
                           font=self.font, 
                           command=self.killCnfm, 
                           bg='red', 
                           compound='c').grid(row=1, column=4, sticky='nsew')
        
        # commands printed here
        self.print_cmd = Label(self.win,
                               borderwidth=2,
                               text='Monitoring RPI stats...',
                               relief="sunken",
                               font=self.font).grid(row=1, column=1, columnspan=3, sticky='nsew')
        
        self.center_margin = Label(self.win,
                                   borderwidth=2).grid(row=2, column=2, rowspan=3, sticky='nsew')
        # display monitor labels
        self.CoreTemp = Label(self.win,
                              text='Core Temp:',
                              borderwidth=2,
#                              relief='sunken',
                              font=self.font).grid(row=2, column=1, sticky='nsew')
        self.CPUusage = Label(self.win,
                              text='CPU Usage:',
                              borderwidth=2,
#                              relief='sunken',
                              font=self.font).grid(row=3, column=1, sticky='nsew')
        self.Diskusage = Label(self.win,
                               text='Disk Usage:',
                               borderwidth=2,
#                               relief='sunken',
                               font=self.font).grid(row=4, column=1, sticky='nsew')
        
        # display live monitor values
        self.CoreTemp = Label(self.win,
#                              text='{0:.3f}'.format(np.random.randn(1).item()),
                              text=os.popen('vcgencmd measure_temp').readline().replace('temp=',''),
                              borderwidth=2,
                              font=self.font).grid(row=2, column=3, sticky='nsew')
        self.CPUusage = Label(self.win,
#                              text='{0:.3f}'.format(np.random.randn(1).item()),
                              text=str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip('\n')),
                              borderwidth=2,
                              font=self.font).grid(row=3, column=3, sticky='nsew')
        self.Diskusage = Label(self.win,
                               text='{0:.3f}'.format(np.random.randn(1).item()),
                               borderwidth=2,
                               font=self.font).grid(row=4, column=3, sticky='nsew')
        # temp image button to be removed
#        self.showIm = False
#        self.saitama = Button(self.win, 
#                              text='Show Saitama',  
#                              font=self.font, 
#                              command=self.pressButton, 
#                              bg='bisque2', 
#                              compound='c').grid(row=2, column=1, columnspan=3, sticky='nsew')
        win.after(1, self.updateLiveData)

    def updateLiveData(self):
        self.datetime = Label(self.win,
                              text=str(datetime.datetime.now(),
                                       borderwidth=2).split('.')[0]).grid(row=0, column=3, columnspan=2, sticky='nse')
        self.CoreTemp = Label(self.win,
#                              text='{0:.3f}'.format(np.random.randn(1).item()),
                              text=os.popen('vcgencmd measure_temp').readline().replace('temp=','').replace('\n',''),
                              borderwidth=2,
                              font=self.font).grid(row=2, column=3, sticky='nsew')
        self.CPUusage = Label(self.win,
#                              text='{0:.3f}'.format(np.random.randn(1).item()),
                              text=str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip('\n')),
                              borderwidth=2,
#                              relief='sunken',
                              font=self.font).grid(row=3, column=3, sticky='nsew')
        self.Diskusage = Label(self.win,
                               text='{0:.3f}'.format(np.random.randn(1).item()),
                               borderwidth=2,
#                               relief='sunken',
                               font=self.font).grid(row=4, column=3, sticky='nsew')
        win.after(1000, self.updateLiveData)
        
        
#    def readCoreTemp(self):
#        return '{0:.3f}'.format(np.random.randn(1).item())
            
#    def quitPgm(self):
#        self.print_cmd = Label(self.win,
#                               text='Quitting Interface',
#                               borderwidth=2, 
#                               relief="sunken",
#                               font=self.font).grid(row=1, column=1, columnspan=3, sticky='nsew')
#        self.win.destroy()
        
    def killPgm(self):
        cnfm = Label(self.win,
                     text='Killing Device...',
                     borderwidth=2, 
                     relief="sunken",
                     font=self.font).grid(row=1, column=1, columnspan=3, sticky='nsew')
        print('Device Shutdown')
        self.win2.destroy()
        self.win.destroy()
        #os.system('sudo shutdown -r now')
    
    def pressButton(self):
#        global disp
        if not self.showIm:
            self.print_cmd = Label(self.win,
                                   text='Displaying Saitama...',
                                   borderwidth=2, 
                                   relief="sunken",
                                   font=self.font).grid(row=1, column=1, columnspan=3, sticky='nsew')
            self.showIm = True
            photo = ImageTk.PhotoImage(Image.open('saitama.jpg').resize((450,200), Image.ANTIALIAS))
            self.disp = Label(self.win, image=photo)
            self.disp.image = photo
            self.disp.grid(row=3, column=1, sticky='nsew') 
        else:
            self.print_cmd = Label(self.win,
                                   text='Removing Saitama...',
                                   borderwidth=2, 
                                   relief="sunken",
                                   font=self.font).grid(row=1, column=1, columnspan=3, sticky='nsew')
            self.showIm = False
            self.disp.grid_forget()
            
    def killCnfm(self):
        self.win2=Toplevel(self.win)
        win_w, win_h = 640, 360
        self.win2.geometry('{}x{}+0+0'.format(win_w, win_h)) #win_w, win_h, origin_x, origin_y
#        self.win2.attributes('-fullscreen', True)
        self.win2.title('Kill program confirm')
        self.font = Font(family='Helvetica', size=12, weight='bold')
        self.win2.grid_columnconfigure(0, weight=1)
        self.win2.grid_columnconfigure(1, weight=1)
        self.win2.grid_columnconfigure(2, weight=1)
        self.win2.grid_columnconfigure(3, weight=1)
        self.win2.grid_columnconfigure(4, weight=1)
#        self.win2.grid_rowconfigure(0, weight=1)
#        self.win2.grid_rowconfigure(1, weight=1)
        self.win2.grid_rowconfigure(2, weight=1)
        self.win2.grid_rowconfigure(3, weight=1)
        self.win2.grid_rowconfigure(4, weight=1)
        
        self.title = Label(self.win2, 
                           text='guiDANCE (Tkinter v8.6)').grid(row=0, columnspan=5, sticky='nsew')
        
        self.print_cmd = Label(self.win2,
                               borderwidth=2,
                               text='Confirm Kill?',
                               relief="sunken",
                               font=self.font).grid(row=1, column=1, columnspan=3, sticky='nsew')
        
        self.cnfmbn = Button(self.win2, 
                              text='Yes',  
                              font=self.font, 
                              command=self.killPgm, 
                              bg='red', 
                              compound='c').grid(row=2, column=3, sticky='nsew')
        
        backbn = Button(self.win2, 
                        text='Go Back', 
                        font=self.font, 
                        command=self.abort_kill, 
                        bg='cyan', 
                        compound='c').grid(row=2, column=1, sticky='nsew')
        
        self.bottom_margin = Label(self.win2,
                                   borderwidth=2).grid(row=3, columnspan=2, sticky='nsew')
        
        self.left_margin = Label(self.win2,
                                 borderwidth=2).grid(column=0, rowspan=3, sticky='nsew')
        
        self.right_margin = Label(self.win2,
                                  borderwidth=2).grid(column=4, rowspan=3, sticky='nsew')
        
        self.center_margin = Label(self.win2,
                                  borderwidth=2).grid(column=2, rowspan=3, sticky='nsew')
    def abort_kill(self):
        self.win2.destroy()
        self.print_cmd = Label(win,
                               text='Aborted Kill Process',
                               borderwidth=2, 
                               relief="sunken",
                               font=self.font).grid(row=1, column=1, columnspan=3, sticky='nsew')

win = Tk()
CoreTempVar = StringVar(value='XXXXX')
my_gui = RPI_GUI(win)      
win.mainloop()