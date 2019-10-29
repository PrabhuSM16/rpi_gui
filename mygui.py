# !/usr/bin/python3

from tkinter import *
from tkinter.font import Font
import os
from PIL import Image, ImageTk

import numpy as np

win_w, win_h = 640, 360
win = Tk()
win.title('ProgComd')
win.geometry('{}x{}+0+0'.format(win_w, win_h)) #win_w, win_h, origin_x, origin_y
win.attributes('-fullscreen', True)
#win_w = win.winfo_screenwidth()
#win_h = win.winfo_screenheight()
print('Original window size: w={}, h={}'.format(win_w, win_h))

myFont = Font(family='Helvetica', size=12, weight='bold')
showIm = False
isFS = False

def pressButton():
 global showIm, disp
 if not showIm:
  showIm = True
  photo = ImageTk.PhotoImage(Image.open('saitama.jpg').resize((450,200), Image.ANTIALIAS))
  disp = Label(win, image=photo)
  disp.image = photo
  disp.grid(row=3, columnspan=3, sticky='nsew')
 else:
  showIm = False
  disp.grid_forget()

def exitPgm():
 win.quit()

def killPgm():
 os.system('sudo shutdown -r now')

def CPUtemp():
 temps = os.popen('vcgencmd measure_temp').readline()
 return(temps.replace('temp=','').replace("'C\n",''))

def RAMuse():
 p = os.popen('free')
 i=0
 while 1:
  i+=1
  line = p.readline()
  if i==2:
   return(line.split()[1:4])

def CPUuse():
 return(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip('\n')))

def DISKuse():
 p = os.popen('df -h /')
 i=0
 while 1:
  i+=1
  line = p.readline()
  if i==2:
   return(line.split()[1:5])

button1 = Button(win, text='Show Saitama',  font=myFont, command=pressButton, bg='bisque2', compound='c')
win.grid_columnconfigure(0, weight=1)
button1.grid(row=1, columnspan=3, sticky='nsew')

exitButton = Button(win, text='Quit', font=myFont, command=exitPgm, bg='cyan', compound='c')
win.grid_columnconfigure(1, weight=1)
exitButton.grid(row=0, sticky='w')

offButton = Button(win, text='Kill', font=myFont, command=killPgm, bg='red', compound='c')
offButton.grid(row=0, column=2, sticky='e')

tp = StringVar()
cu = StringVar()

tp = CPUtemp()
cu = CPUuse()
ram_stat = RAMuse()
rt = round(int(ram_stat[0])/1000, 1)
ru = round(int(ram_stat[1])/1000, 1)
rf = round(int(ram_stat[2])/1000, 1)
disk_stat = DISKuse()
dt = disk_stat[0]
du = disk_stat[1]
df = disk_stat[2]
dup = disk_stat[3]

tempVar = StringVar()
tempVar.trace('w', CPUtemp())
cuVar = StringVar()
cuVar.trace('w', CPUuse())
tempVar.set(CPUtemp())
cuVar.set(CPUuse())
mTemp = Label(win, text='Core Temp: {}deg C'.format(tempVar), font=myFont, bg='orange').grid(row=2, sticky='nsew')
mCPUuse = Label(win, text='CPU Usage: {}%'.format(cuVar), font=myFont, bg='orange').grid(row=3, sticky='nsew')
#tempVar.set(tp)
#cuVar.set(cu)

#print("tmp:{}'C, cpu use:{}%, ram tot:{}Mb, ram use:{}Mb, ram free:{}Mb, disk tot:{}, disk use:{}, disk free:{}, disk usage perc:{}".format(tp,cu,rt,ru,rf,dt,du,df,dup ))
#print('grid size: {}'.format(win.grid_size()))
win.mainloop()
