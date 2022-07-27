from tkinter import *
import tkinter
import tkinter.messagebox
import webbrowser
import os


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








#app icons












def work():
    work_there.configure(bg='darkgreen')
    #tkinter.messagebox.showinfo('work', 'now u are working!')
    #tkinter.messagebox.showwarning('work', 'now u are working!')
    #tkinter.messagebox.showerror('work', 'now u are working!')
    root=tkinter.Tk()
    
    root.title('WORK')  
    root.geometry('500x700')  
    root.configure(bg='darkgreen')  
    
  
    #icon for work
    root.iconbitmap("work.ico")


    #part for apps i need on work  

    whatsapp_web = Button(root, text="web.whatsapp.com", font=("helvetica", 14), width="40", bg='lightgreen', command=open_whatsapp)
    whatsapp_web.pack(pady=3)

    spotify = Button(root, text="spotify.com", font=("helvetica", 14), width="40", bg='lightgreen', command=open_spotify)
    spotify.pack(pady=3)

    outlook = Button(root, text="outlook", font=("helvetica", 14), width="40", bg='lightgreen', command=open_outlook)
    outlook.pack(pady=3)

    word = Button(root, text="word", font=("helvetica", 14), width="40", bg='lightgreen', command=open_word)
    word.pack(pady=3)

    excell = Button(root, text="excell", font=("helvetica", 14), width="40", bg='lightgreen', command=open_excell)
    excell.pack(pady=3)

    powerpoint = Button(root, text="powerpoint", font=("helvetica", 14), width="40", bg='lightgreen', command=open_powerpoint)
    powerpoint.pack(pady=3)

    gmail0 = Button(root, text="gmail 1", font=("helvetica", 14), width="40", bg='lightgreen', command=open_gmail1)
    gmail0.pack(pady=3)

    gmail1 = Button(root, text="gmail 2", font=("helvetica", 14), width="40", bg='lightgreen', command=open_gmail2)
    gmail1.pack(pady=3)

    gmail2 = Button(root, text="gmail 3", font=("helvetica", 14), width="40", bg='lightgreen', command=open_gmail3)
    gmail2.pack(pady=3)
    
    vm = Button(root, text="VM", font=("helvetica", 14), width="40", bg='lightgreen', command=open_vm)
    vm.pack(pady=3)

    github = Button(root, text="github", font=("helvetica", 14), width="40", bg='lightgreen' ,command=open_github)
    github.pack(pady=3)

    googledrive = Button(root, text="Google Drive", font=("helvetica", 14), width="40", bg='lightgreen', command=open_drive)
    googledrive.pack(pady=3)

    azn = Button(root, text="Ausbildungsnachweise", font=("helvetica", 14), width="40", bg='lightgreen', command=open_azn)
    azn.pack(pady=3)








def privHome():
    privHome.configure(bg='darkgreen') 
    print("now you are at home")
    #tkinter.messagebox.showinfo('private', 'now you are at home')
    #tkinter.messagebox.showwarning('private', 'now you are at home')
    #tkinter.messagebox.showerror('private', 'now you are at home')
    root=tkinter.Tk()
    root.title('HOME')  
    root.geometry('500x700')  
    root.configure(bg='darkgreen')
    #icon for work
    root.iconbitmap("home.ico")

    #part for my apps

    whatsapp_web = Button(root, text="web.whatsapp.com", font=("helvetica", 14), width="40", bg='lightgreen', command=open_whatsapp)
    whatsapp_web.pack(pady=3)
    spotify = Button(root, text="spotify.com", font=("helvetica", 14), width="40", bg='lightgreen', command=open_spotify)
    spotify.pack(pady=3)

root = Tk()
root.geometry('300x100')
frame1 = Frame(root)
frame2 = Frame(root)
root.title("where are you")
root.iconbitmap("start.ico")
label= Label(frame1,text="choose one",justify=LEFT)
label.pack(side=LEFT)

work_there = Button(frame2,text="work",command=work)
work_there.pack()

privHome = Button(frame2,text="private",command=privHome)
privHome.pack()

frame1.pack(padx=1,pady=1)
frame2.pack(padx=10,pady=10)

root.mainloop()