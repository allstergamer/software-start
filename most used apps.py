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












def work():
    work_there.configure(bg=rgb_hack((141, 192, 252)))
    #tkinter.messagebox.showinfo('work', 'now u are working!')
    #tkinter.messagebox.showwarning('work', 'now u are working!')
    #tkinter.messagebox.showerror('work', 'now u are working!')
    worked=tkinter.Tk()
    worked.title('WORK')  
    worked.geometry('500x700')  
    worked.configure(bg=rgb_hack((82, 161, 240)))  
  
    #icon for work
    worked.iconbitmap("work.ico")


    #part for apps i need on work  
    moodle = Button(worked, text="Moodle", font=("helvetica", 14), width="40", bg=rgb_hack((141, 192, 252)), command=moodle_login)
    moodle.pack(pady=5)

    azn = Button(worked, text="Ausbildungsnachweise", font=("helvetica", 14), width="40", bg=rgb_hack((141, 192, 252)), command=open_azn)
    azn.pack(pady=5)

    outlook = Button(worked, text="outlook", font=("helvetica", 14), width="40", bg=rgb_hack((141, 192, 252)), command=open_outlook)
    outlook.pack(pady=5)

    word = Button(worked, text="word", font=("helvetica", 14), width="40", bg=rgb_hack((141, 192, 252)), command=open_word)
    word.pack(pady=5)

    excell = Button(worked, text="excell", font=("helvetica", 14), width="40", bg=rgb_hack((141, 192, 252)), command=open_excell)
    excell.pack(pady=5)

    powerpoint = Button(worked, text="powerpoint", font=("helvetica", 14), width="40", bg=rgb_hack((141, 192, 252)), command=open_powerpoint)
    powerpoint.pack(pady=5)

    gmail0 = Button(worked, text="gmail 1", font=("helvetica", 14), width="40", bg=rgb_hack((141, 192, 252)), command=open_gmail1)
    gmail0.pack(pady=5)

    gmail1 = Button(worked, text="gmail 2", font=("helvetica", 14), width="40", bg=rgb_hack((141, 192, 252)), command=open_gmail2)
    gmail1.pack(pady=5)

    gmail2 = Button(worked, text="gmail 3", font=("helvetica", 14), width="40", bg=rgb_hack((141, 192, 252)), command=open_gmail3)
    gmail2.pack(pady=5)
    
    vm = Button(worked, text="VM", font=("helvetica", 14), width="40", bg=rgb_hack((141, 192, 252)), command=open_vm)
    vm.pack(pady=5)

    github = Button(worked, text="github", font=("helvetica", 14), width="40", bg=rgb_hack((141, 192, 252)) ,command=open_github)
    github.pack(pady=5)

    googledrive = Button(worked, text="Google Drive", font=("helvetica", 14), width="40", bg=rgb_hack((141, 192, 252)), command=open_drive)
    googledrive.pack(pady=5)

    whatsapp_web = Button(worked, text="web.whatsapp.com", font=("helvetica", 14), width="40", bg=rgb_hack((141, 192, 252)), command=open_whatsapp)
    whatsapp_web.pack(pady=5)

    spotify = Button(worked, text="spotify.com", font=("helvetica", 14), width="40", bg=rgb_hack((141, 192, 252)), command=open_spotify)
    spotify.pack(pady=5)









def privHome():
    privHome.configure(bg=rgb_hack((141, 192, 252))) 
    print("now you are at home")
    #tkinter.messagebox.showinfo('private', 'now you are at home')
    #tkinter.messagebox.showwarning('private', 'now you are at home')
    #tkinter.messagebox.showerror('private', 'now you are at home')
    root=tkinter.Tk()
    root.title('HOME')  
    root.geometry('500x700')  
    root.configure(bg=rgb_hack((82, 161, 240)))
    #icon for work
    root.iconbitmap("home.ico")

    #part for my apps
    wh = Button(root, text="wohnheim login", font=("helvetica", 14), width="40", bg=rgb_hack((141, 192, 252)), command=login_wh)
    wh.pack(pady=5)
    pihole = Button(root, text="pihole admin dashboard", font=("helvetica", 14), width="40", bg=rgb_hack((141, 192, 252)), command=pihole_login)
    pihole.pack(pady=5)
    whatsapp_web = Button(root, text="web.whatsapp.com", font=("helvetica", 14), width="40", bg=rgb_hack((141, 192, 252)), command=open_whatsapp)
    whatsapp_web.pack(pady=5)
    spotify = Button(root, text="spotify.com", font=("helvetica", 14), width="40", bg=rgb_hack((141, 192, 252)), command=open_spotify)
    spotify.pack(pady=5)

root = Tk()
root.geometry('300x100')

frame1 = Frame(root)
frame2 = Frame(root)
root.title("where are you")
root.configure(bg=rgb_hack((82, 161, 240))) 
root.iconbitmap("start.ico")
label= Label(frame1,text="choose one",justify=LEFT, bg=rgb_hack((82, 161, 240)))
label.pack(side=LEFT)

work_there = Button(frame2,text="work",width=10, command=work, bg=rgb_hack((141, 192, 252)))
work_there.pack()

privHome = Button(frame2,text="private",width=10,command=privHome, bg=rgb_hack((141, 192, 252)))
privHome.pack()

frame1.pack(padx=1,pady=1)
frame2.pack(padx=10,pady=10)

root.mainloop()