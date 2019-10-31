# !/usr/bin/python3

from tkinter import *
from tkinter.font import Font
import os
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import numpy as np
import datetime

class RPI_GUI:
    global win, CoreTempVar
    def __init__(self, win):
        # Win
        self.win = win
        win_w, win_h = 480, 320
        self.win.geometry('{}x{}+0+0'.format(win_w, win_h)) #win_w, win_h, origin_x, origin_y
        self.win.attributes('-fullscreen', True)
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
        print('W:{}, H:{}'.format(win.winfo_screenwidth(), win.winfo_screenheight()))

        self.kill = Button(self.win, 
                           text='Kill', 
                           font=self.font, 
                           command=self.killCnfm, 
                           bg='red', 
                           compound='c')
        self.kill.grid(row=0, column=0, sticky='nsew')
        
        # commands printed here
        self.print_cmd = Label(self.win,
                               borderwidth=2,
                               text='Monitoring RPI stats...',
                               relief="sunken",
                               font=self.font)
        self.print_cmd.grid(row=1, column=1, columnspan=3, sticky='nsew')
        
        # Dynamic variable labels
        self.CoreTempLabel = Label(self.win,
                              text='Core Temp:',
                              borderwidth=2,
                              font=self.font)
        self.CoreTempLabel.grid(row=2, column=0, sticky='nsw')
        
        self.CPUusageLabel = Label(self.win,
                              text='CPU Usage:',
                              borderwidth=2,
                              font=self.font)
        self.CPUusageLabel.grid(row=3, column=0, sticky='nsw')
        
        self.DiskusageLabel = Label(self.win,
                               text='Disk Usage:',
                               borderwidth=2,
                               font=self.font)
        self.DiskusageLabel.grid(row=4, column=0, sticky='nsw')
        
        self.time=[]
        self.tempPlot=[]
        self.useRam=[]
        self.freeRam=[]
        
        
        win.after(1, self.updateLiveData)

    def updateLiveData(self):
        # Win
        # Top title
        time = str(datetime.datetime.now()).split('.')[0]
        self.title = Label(self.win, 
                           text='guiDANCE (Tkinter v8.6)                      '+time)
        self.title.grid(row=0, column=1, columnspan=4, sticky='nse')
        self.time.append(time.split(' ')[1])
        
        # Dynamic variable readings
        try: coreTemp1 = os.popen('vcgencmd measure_temp').readlines()[0].strip('temp=').strip('\'C\\n')
        except: coreTemp1 = '{0:.3f}'.format(np.random.randn(1).item())
        self.CoreTemp = Label(self.win,
                              text=coreTemp1+"'C",
                              font=self.font)
        self.CoreTemp.grid(row=2, column=1, sticky='nsw')
        self.tempPlot.append(float(coreTemp1))
        
        self.CPUusage = Label(self.win,
                              text=str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip('\n'))+' %',
                              font=self.font)
        self.CPUusage.grid(row=3, column=1, sticky='nsw')
        
        self.Diskusage = Label(self.win,
                               text='{0:.3f}'.format(np.random.randn(1).item()),
                               font=self.font)
        self.Diskusage.grid(row=4, column=1, sticky='nsw')
        
        try:
            ramUse1 = float(os.popen('free -h').readlines()[1].split()[2].strip('M'))
            ramUse2 = float(os.popen('free -h').readlines()[1].split()[3].strip('M'))
        except:
            ramUse1 = np.random.randn(1).item()
            ramUse2 = np.random.randn(1).item()
        self.useRam.append(ramUse1)
        self.freeRam.append(ramUse2)
        
        if len(self.time)>20:
            self.time = self.time[-20:]
            self.tempPlot = self.tempPlot[-20:]
            self.useRam = self.useRam[-20:]
            self.freeRam = self.freeRam[-20:]
            
        self.dataPlot()
        
        win.after(1000, self.updateLiveData)
    
    def dataPlot(self):
        plt.clf()
        
        plt.subplot(2,1,1)
        plt.plot(self.time, self.tempPlot, '-*', label='Temp')
        plt.ylabel('Temp (\'C)')
        plt.legend()
#        plt.grid(True)
        plt.xticks([])
        
        plt.subplot(2,1,2)
        plt.plot(self.time, self.useRam, '-*', label='Used RAM')
        plt.plot(self.time, self.freeRam, '-*', label='Free RAM')
        plt.ylabel('RAM Stats (MB)')
        plt.xlabel('Time')
        plt.xticks(self.time, rotation='vertical')
#        plt.grid(True)
        plt.legend()
        
#        plt.show()
        plt.savefig('plot.png')
        photo = ImageTk.PhotoImage(Image.open('plot.png').resize((300,250), Image.ANTIALIAS))
        self.disp = Label(self.win, image=photo)
        self.disp.image = photo
        self.disp.grid(row=2, column=2, rowspan=3, columnspan=4, sticky='nsew') 
        
    def killPgm(self):
        # Win
        cnfm = Label(self.win,
                     text='Killing Device...',
                     borderwidth=2, 
                     relief="sunken",
                     font=self.font).grid(row=1, column=1, columnspan=3, sticky='nsew')
        print('Device Shutdown')
        self.win2.destroy()
        self.win.destroy()
        #os.system('sudo shutdown -r now')
    
#    def pressButton(self):
##        global disp
#        if not self.showIm:
#            self.print_cmd = Label(self.win,
#                                   text='Displaying Saitama...',
#                                   borderwidth=2, 
#                                   relief="sunken",
#                                   font=self.font).grid(row=1, column=1, columnspan=3, sticky='nsew')
#            self.showIm = True
#            photo = ImageTk.PhotoImage(Image.open('saitama.jpg').resize((450,200), Image.ANTIALIAS))
#            self.disp = Label(self.win, image=photo)
#            self.disp.image = photo
#            self.disp.grid(row=3, column=1, sticky='nsew') 
#        else:
#            self.print_cmd = Label(self.win,
#                                   text='Removing Saitama...',
#                                   borderwidth=2, 
#                                   relief="sunken",
#                                   font=self.font).grid(row=1, column=1, columnspan=3, sticky='nsew')
#            self.showIm = False
#            self.disp.grid_forget()
            
    def killCnfm(self):
        # Win2
        self.win2=Toplevel(self.win)
        win_w, win_h = 480, 320
        self.win2.geometry('{}x{}+0+0'.format(win_w, win_h)) #win_w, win_h, origin_x, origin_y
        self.win2.attributes('-fullscreen', True)
        self.win2.title('Kill program confirm')
        self.font = Font(family='Helvetica', size=12, weight='bold')
        self.win2.grid_columnconfigure(0, weight=1)
        self.win2.grid_columnconfigure(1, weight=1)
        self.win2.grid_columnconfigure(2, weight=1)
        self.win2.grid_columnconfigure(3, weight=1)
        self.win2.grid_columnconfigure(4, weight=1)

        self.win2.grid_rowconfigure(2, weight=1)
        self.win2.grid_rowconfigure(3, weight=1)
        self.win2.grid_rowconfigure(4, weight=1)
        
        self.title = Label(self.win2, 
                           text='guiDANCE (Tkinter v8.6)')
        self.title.grid(row=0, columnspan=5, sticky='nsew')
        
        self.print_cmd = Label(self.win2,
                               borderwidth=2,
                               text='Confirm Kill?',
                               relief="sunken",
                               font=self.font)
        self.print_cmd.grid(row=1, column=1, columnspan=3, sticky='nsew')
        
        self.cnfmbn = Button(self.win2, 
                              text='Yes',  
                              font=self.font, 
                              command=self.killPgm, 
                              bg='red', 
                              compound='c')
        self.cnfmbn.grid(row=2, column=3, sticky='nsew')
        
        self.backbn = Button(self.win2, 
                        text='Go Back', 
                        font=self.font, 
                        command=self.abort_kill, 
                        bg='cyan', 
                        compound='c')
        self.backbn.grid(row=2, column=1, sticky='nsew')
        
        self.bottom_margin = Label(self.win2,
                                   borderwidth=2)
        self.bottom_margin.grid(row=3, columnspan=2, sticky='nsew')
        
        self.left_margin = Label(self.win2,
                                 borderwidth=2)
        self.left_margin.grid(column=0, rowspan=3, sticky='nsew')
        
        self.right_margin = Label(self.win2,
                                  borderwidth=2)
        self.right_margin.grid(column=4, rowspan=3, sticky='nsew')
        
        self.center_margin = Label(self.win2,
                                   borderwidth=2)
        self.center_margin.grid(column=2, rowspan=3, sticky='nsew')
        
    def abort_kill(self):
        # Win2
        self.win2.destroy()
        self.print_cmd = Label(win,
                               text='Aborted Kill Process',
                               borderwidth=2, 
                               relief="sunken",
                               font=self.font)
        self.print_cmd.grid(row=1, column=1, columnspan=3, sticky='nsew')

win = Tk()
CoreTempVar = StringVar(value='XXXXX')
my_gui = RPI_GUI(win)      
win.mainloop()
