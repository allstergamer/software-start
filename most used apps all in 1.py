from tkinter import *
import tkinter
import tkinter.messagebox
import webbrowser
import os




def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb

#website definition i need
def open_whatsapp():
    webbrowser.open_new("https://web.whatsapp.com/")
def open_spotify(): 
    webbrowser.open_new("https://open.spotify.com/")
def open_word():
    webbrowser.open_new("https://www.office.com/launch/word?auth=1")
def open_excell():
    webbrowser.open_new("https://www.office.com/launch/excel?auth=1")
def open_powerpoint():
    webbrowser.open_new("https://www.office.com/launch/powerpoint?auth=1")
def open_gmail1():
    webbrowser.open_new("https://mail.google.com/mail/u/0/#inbox")
def open_gmail2():
    webbrowser.open_new("https://mail.google.com/mail/u/1/#inbox")
def open_gmail3():
    webbrowser.open_new("https://mail.google.com/mail/u/2/#inbox")
def open_outlook():
    webbrowser.open_new("https://mail.srhk.de/")
def open_vm():
    os.startfile("C:\Program Files\Oracle\VirtualBox\VirtualBox.exe")
def open_github():
    webbrowser.open_new("https://github.com/allstergamer")
def open_drive():
    webbrowser.open_new("https://drive.google.com/")
def open_udemy():
    webbrowser.open_new("https://bbw-dresden.udemy.com/")
def open_azn():
    os.startfile("H:\AZN")


def login_wh():
    webbrowser.open_new("https://gw.srhk.net:4100/")
def pihole_login():
    webbrowser.open_new("https://192.168.8.50/admin")
def moodle_login():
    webbrowser.open_new("https://online-learning-bbws.de/login/index.php")





#app icons













#tkinter.messagebox.showinfo('private', 'now you are at home')
#tkinter.messagebox.showwarning('private', 'now you are at home')
#tkinter.messagebox.showerror('private', 'now you are at home')
root=tkinter.Tk()
root.configure(bg=rgb_hack((141, 192, 252))) 
root.title('HOME')  
root.geometry('500x800')  
root.configure(bg=rgb_hack((82, 161, 240)))
#icon for work
#icon for work



#part for apps i need on work  
moodle = Button(root, text="Moodle", font=("helvetica", 14), width="40", bg=rgb_hack((141, 192, 252)), command=moodle_login)
moodle.pack(pady=5)

azn = Button(root, text="Ausbildungsnachweise", font=("helvetica", 14), width="40", bg=rgb_hack((141, 192, 252)), command=open_azn)
azn.pack(pady=5)

outlook = Button(root, text="outlook", font=("helvetica", 14), width="40", bg=rgb_hack((141, 192, 252)), command=open_outlook)
outlook.pack(pady=5)

word = Button(root, text="word", font=("helvetica", 14), width="40", bg=rgb_hack((141, 192, 252)), command=open_word)
word.pack(pady=5)

excell = Button(root, text="excell", font=("helvetica", 14), width="40", bg=rgb_hack((141, 192, 252)), command=open_excell)
excell.pack(pady=5)

powerpoint = Button(root, text="powerpoint", font=("helvetica", 14), width="40", bg=rgb_hack((141, 192, 252)), command=open_powerpoint)
powerpoint.pack(pady=5)

gmail0 = Button(root, text="gmail 1", font=("helvetica", 14), width="40", bg=rgb_hack((141, 192, 252)), command=open_gmail1)
gmail0.pack(pady=5)

gmail1 = Button(root, text="gmail 2", font=("helvetica", 14), width="40", bg=rgb_hack((141, 192, 252)), command=open_gmail2)
gmail1.pack(pady=5)

gmail2 = Button(root, text="gmail 3", font=("helvetica", 14), width="40", bg=rgb_hack((141, 192, 252)), command=open_gmail3)
gmail2.pack(pady=5)

vm = Button(root, text="VM", font=("helvetica", 14), width="40", bg=rgb_hack((141, 192, 252)), command=open_vm)
vm.pack(pady=5)

github = Button(root, text="github", font=("helvetica", 14), width="40", bg=rgb_hack((141, 192, 252)) ,command=open_github)
github.pack(pady=5)

googledrive = Button(root, text="Google Drive", font=("helvetica", 14), width="40", bg=rgb_hack((141, 192, 252)), command=open_drive)
googledrive.pack(pady=5)

whatsapp_web = Button(root, text="web.whatsapp.com", font=("helvetica", 14), width="40", bg=rgb_hack((141, 192, 252)), command=open_whatsapp)
whatsapp_web.pack(pady=5)

spotify = Button(root, text="spotify.com", font=("helvetica", 14), width="40", bg=rgb_hack((141, 192, 252)), command=open_spotify)
spotify.pack(pady=5)











#part for my apps
wh = Button(root, text="wohnheim login", font=("helvetica", 14), width="40", bg=rgb_hack((141, 192, 252)), command=login_wh)
wh.pack(pady=5)
pihole = Button(root, text="pihole admin dashboard", font=("helvetica", 14), width="40", bg=rgb_hack((141, 192, 252)), command=pihole_login)
pihole.pack(pady=5)




root.mainloop()