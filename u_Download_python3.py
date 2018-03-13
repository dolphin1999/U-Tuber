#!/usr/bin/env python

import tkinter
from tkinter import *
import os
import datetime


"""
import urllib2
proxy = urllib2.ProxyHandler({'http':'edcguest:edcguest@172.31.100.14:3128', 'https':'edcguest:edcguest@172.31.100.14:3128'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)
"""

from pytube import YouTube
from pytube import Playlist

top = tkinter.Tk()

#link_file = open("links.txt","w+")
global st, pt,v1,v2, linkFile, pth, Frame1, Frame2, Frame3, Lable1, Lable2, Lable3, Entry1, Entry2, Button1, Button2


linkFile = "links.txt"
#pth = "playlist/"


def on_clickNext():
    global st, linkFile, pth
    st = Entry1.get()
    print('st')
    if(st != "") :
        link_file = open(linkFile,"a+")
        link_file.write(st+"\n")
        link_file.close()

        st = ""
        Entry1.delete(0, END)


def on_clickDownloadAll():
		global linkFile, pth, v1
		path = v1.get()
		print(path)
		if(path == "<path if any>") :
			today=datetime.datetime.now()
			year,month,day=today.year,today.strftime("%b"),today.day
			custom_path=str(month)+'_'+str(day)+'_'+str(year)
			path=custom_path
			if not (os.path.exists(custom_path)): os.mkdir(custom_path)

		on_clickNext()
		links = open(linkFile,"r")
		for lk in links:
			flag = True
			while flag:
				try:
					yt = YouTube(lk)
					flag = False
				except:
					print("Connection Error")
					continue
			
			yt.streams.first().download(path)

		v1.set("<path if any>")
		links.close()
		links = open(linkFile,"w")
		links.truncate()


def on_clickDownload():
	global pt, pth
	"""
    path = v2.get()
    if(path == "<path if any>") :
    	path = ""
    """
	pt=Entry2.get()
	if(pt != ""):
		pl = Playlist(pt)
		pl.download_all()
		#v2.set("<path if any>")
		Entry2.delete(0,END)


v1 = StringVar()
#v2 = StringVar()

Frame1 = Frame(top)
Label3 = Label(Frame1)
Frame2 = Frame(top)
Label1 = Label(Frame2)
Entry1 = Entry(Frame2)
Button1 = Button(Frame2,command = on_clickNext)
Button2 = Button(Frame2, command = on_clickDownloadAll)
Frame3 = Frame(top)
Label2 = Label(Frame3)
Entry2 = Entry(Frame3)
Button3 = Button(Frame3, command = on_clickDownload)
Entry3 = Entry(Frame2, textvariable = v1)
#Entry4 = Entry(Frame3, textvariable = v2)

v1.set("<path if any>")
#v2.set("<path if any>")

def main():
	_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
	_fgcolor = '#000000'  # X11 color: 'black'
	_compcolor = '#d9d9d9' # X11 color: 'gray85'
	_ana1color = '#d9d9d9' # X11 color: 'gray85' 
	_ana2color = '#d9d9d9' # X11 color: 'gray85' 
	font10 = "-family {Noto Sans CJK JP} -size 25 -weight bold "  \
	    "-slant roman -underline 0 -overstrike 0"
	font11 = "-family {Noto Sans CJK JP} -size 11 -weight bold "  \
	    "-slant roman -underline 0 -overstrike 0"
	font9 = "-family FreeSans -size 9 -weight bold -slant roman "  \
	    "-underline 0 -overstrike 0"

	top.geometry("600x500+491+116")
	top.title("U_TUBER")
	top.configure(background="#060403")
	top.configure(highlightcolor="black")



	#Frame1 = Frame(top)
	Frame1.place(relx=0.0, rely=0.0, relheight=0.11, relwidth=1.01)
	Frame1.configure(relief=GROOVE)
	Frame1.configure(borderwidth="2")
	Frame1.configure(relief=GROOVE)
	Frame1.configure(background="#f81118")
	Frame1.configure(width=605)

	#Label3 = Label(Frame1)
	Label3.place(relx=0.21, rely=0.18, height=28, width=350)
	Label3.configure(activebackground="#f81118")
	Label3.configure(background="#f81118")
	Label3.configure(font=font10)
	Label3.configure(text='''U-TUBER''')

	#Frame2 = Frame(top)
	Frame2.place(relx=0.0, rely=0.2, relheight=0.29, relwidth=1.01)
	Frame2.configure(relief=GROOVE)
	Frame2.configure(borderwidth="2")
	Frame2.configure(relief=GROOVE)
	Frame2.configure(background="Gray23")
	Frame2.configure(width=605)

	#Label1 = Label(Frame2)
	Label1.place(relx=0.02, rely=0.14, height=28, width=90)
	Label1.configure(activebackground="cyan3")
	Label1.configure(background="cyan3")
	Label1.configure(font=font11)
	Label1.configure(text='''Video Link''')

	#Entry1 = Entry(Frame2)
	Entry1.place(relx=0.18, rely=0.14,height=30, relwidth=0.8)
	Entry1.configure(background="white")
	Entry1.configure(font="TkFixedFont")
	Entry1.configure(selectbackground="#c4c4c4")


	#Button1 = Button(Frame2,command = on_clickNext)
	Button1.place(relx=0.03, rely=0.48, height=36, width=87)
	Button1.configure(activebackground="DarkOrange3")
	Button1.configure(text='''Add More''')
	Button1.configure(background = "coral1")

	#Button2 = Button(Frame2, command = on_clickDownloadAll)
	Button2.place(relx=0.76, rely=0.48, height=36, width=107)
	Button2.configure(activebackground="DarkOrange3")
	Button2.configure(text='''Download All''')
	Button2.configure(background = "coral1")

	#Frame3 = Frame(top)
	Frame3.place(relx=-0.02, rely=0.66, relheight=0.27, relwidth=1.02)
	Frame3.configure(relief=GROOVE)
	Frame3.configure(borderwidth="2")
	Frame3.configure(relief=GROOVE)
	Frame3.configure(background="Gray23")
	Frame3.configure(width=615)

	#Label2 = Label(Frame3)
	Label2.place(relx=0.03, rely=0.22, height=28, width=86)
	Label2.configure(activebackground="cyan3")
	Label2.configure(background="cyan3")
	Label2.configure(font=font9)
	Label2.configure(text='''Playlist Link''')

	#Entry2 = Entry(Frame3)
	Entry2.place(relx=0.18, rely=0.22,height=30, relwidth=0.81)
	Entry2.configure(background="white")
	Entry2.configure(font="TkFixedFont")
	Entry2.configure(selectbackground="#c4c4c4")

	#Button3 = Button(Frame3)
	Button3.place(relx=0.78, rely=0.59, height=36, width=97)
	Button3.configure(activebackground="DarkOrange3")
	Button3.configure(text='''Download''')
	Button3.configure(background = "coral1")

	Entry3.place(relx=0.23, rely=0.48,height=30, relwidth=0.3)
	Entry3.configure(background="white")
	Entry3.configure(font="TkFixedFont")
	Entry3.configure(selectbackground="#c4c4c4")

	"""
	Entry4.place(relx=0.25, rely=0.62,height=30, relwidth=0.3)
	Entry4.configure(background="white")
	Entry4.configure(font="TkFixedFont")
	Entry4.configure(selectbackground="#c4c4c4")
	"""



	top.mainloop()


if __name__ == '__main__':
    main()
