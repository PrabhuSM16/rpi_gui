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



#win = Tk()
#win.attributes('-fullscreen', True)
#win_w = win.winfo_screenwidth()
#win_h = win.winfo_screenheight()
#print('Original window size: w={}, h={}'.format(win_w, win_h))

#def pressButton():
# global showIm, disp
# if not showIm:
#  showIm = True
#  photo = ImageTk.PhotoImage(Image.open('saitama.jpg').resize((450,200), Image.ANTIALIAS))
#  disp = Label(win, image=photo)
#  disp.image = photo
#  disp.grid(row=3, columnspan=3, sticky='nsew')
# else:
#  showIm = False
#  disp.grid_forget()
#
#def exitPgm():
# print('Quit guiDANCE')
# win.quit()
#
#def killPgm():
# print('Device Shutdown')
# #os.system('sudo shutdown -r now')
#
#def CPUtemp():
# temps = os.popen('vcgencmd measure_temp').readline()
# return(temps.replace('temp=','').replace("'C\n",''))
#
#def RAMuse():
# p = os.popen('free')
# i=0
# while 1:
#  i+=1
#  line = p.readline()
#  if i==2:
#   return(line.split()[1:4])
#
#def CPUuse():
# return(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip('\n')))
#
#def DISKuse():
# p = os.popen('df -h /')
# i=0
# while 1:
#  i+=1
#  line = p.readline()
#  if i==2:
#   return(line.split()[1:5])
#
#button1 = Button(win, text='Show Saitama',  font=myFont, command=pressButton, bg='bisque2', compound='c')
#win.grid_columnconfigure(0, weight=1)
#button1.grid(row=1, columnspan=3, sticky='nsew')
#
#exitButton = Button(win, text='Quit', font=myFont, command=win.destroy, bg='cyan', compound='c')
#win.grid_columnconfigure(1, weight=1)
#exitButton.grid(row=0, sticky='w')
#
#offButton = Button(win, text='Kill', font=myFont, command=killPgm, bg='red', compound='c')
#offButton.grid(row=0, column=2, sticky='e')
#
#tp = StringVar()
#cu = StringVar()
#
## RPI monitoring functions
##tp = CPUtemp()
##cu = CPUuse()
##ram_stat = RAMuse()
##rt = round(int(ram_stat[0])/1000, 1)
##ru = round(int(ram_stat[1])/1000, 1)
##rf = round(int(ram_stat[2])/1000, 1)
##disk_stat = DISKuse()
##dt = disk_stat[0]
##du = disk_stat[1]
##df = disk_stat[2]
##dup = disk_stat[3]
#
##tempVar = StringVar()
##tempVar.trace('w', CPUtemp())
##cuVar = StringVar()
##cuVar.trace('w', CPUuse())
##tempVar.set(CPUtemp())
##cuVar.set(CPUuse())
##mTemp = Label(win, text='Core Temp: {}deg C'.format(tempVar), font=myFont, bg='orange').grid(row=2, sticky='nsew')
##mCPUuse = Label(win, text='CPU Usage: {}%'.format(cuVar), font=myFont, bg='orange').grid(row=3, sticky='nsew')
#
##tempVar.set(tp)
##cuVar.set(cu)
#
##print("tmp:{}'C, cpu use:{}%, ram tot:{}Mb, ram use:{}Mb, ram free:{}Mb, disk tot:{}, disk use:{}, disk free:{}, disk usage perc:{}".format(tp,cu,rt,ru,rf,dt,du,df,dup ))
##print('grid size: {}'.format(win.grid_size()))
#win.mainloop()
