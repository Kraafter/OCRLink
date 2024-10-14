import tkinter
from tkinter import *
from tkinter import messagebox
import webbrowser

from ImageProcess import *


def processing():
    try:
        return splitlink(ocrproc())
    except:
        return "No image to convert"


def run():
    inn = processing()
    linktoopen = ""
    print(inn)
    if inn == "No image to convert":
        textout.configure(text="Check if you have copied an image containing a link")
        return None
    elif inn is None:
        textout.configure(text="Check if you have copied an image containing a link")
        return None
    else:
        textout.configure(text=inn)
        return inn


def openLink():
    linktoopen = textout.cget("text")
    print(linktoopen)
    if not (linktoopen == "Check if you have copied an image containing a link" or linktoopen == "                     "
                                                                                                 "                  "):
        webbrowser.open(str(linktoopen))
    else:
        messagebox.showerror(title="Error", message="There is no link to open")

def opengithub():
    webbrowser.open("https://github.com/Kraafter/OCRLink")


def helpsect():
    p2 = PhotoImage(file='C:\\Program Files\\KraaftWare\\ocrlink\\resource\\icon.png')

    helpwin = tkinter.Toplevel()
    helpwin.title("Help")
    helpwin.geometry("550x400")
    helpwin.resizable(width=False, height=False)
    helpwin.iconphoto(True, p2)

    text1 = tkinter.Label(helpwin, text="ImageLink is a tool capable of extracting a link within\nan image containing text. To use it, "
                                        "first copy\na part of the screen containing a link with\nwin+shift+s. Then press"
                                        " the 'get link' button to\nget the link from what you screenshotted."
                                        "\n\nOnly open links you trust, I am not responsible for damages caused by "
                                        "opening bad links")
    empty1 = tkinter.Label(helpwin)
    text2 = tkinter.Label(helpwin, text='Program was built by Kraafter using Python\n\nCopyright 2023 '
                                        'Kraafter\nLicensed under the Apache License, Version 2.0 (the '
                                        '"License");\nyou may not use this file except in compliance with the '
                                        'License.\nYou may obtain a copy of the License at\n\n    '
                                        'https://www.apache.org/licenses/LICENSE-2.0\n\nUnless required by applicable'
                                        'law or agreed to in writing, software\ndistributed under the License is '
                                        'distributed on an "AS IS" BASIS,\nWITHOUT WARRANTIES OR CONDITIONS OF ANY '
                                        'KIND, either express or implied.\nSee the License for the specific language '
                                        'governing permissions and\nimitations under the License.')
    empty2 = tkinter.Label(helpwin)
    button1 = tkinter.Button(helpwin, text="Github", command=opengithub)

    text1.pack()
    empty1.pack()
    text2.pack()
    empty2.pack()
    button1.pack()

# GUI


appl = Tk()

appl.title('ImageLink')
appl.geometry("550x120")
appl.resizable(width=False, height=False)

txthead = Label(appl, text = "ImageLink link grabber")
textout = Label(appl, text="                                       ",background='lightgray', justify="center")
GetButton = Button(appl, text="Get link", command=run)
openlink = Button(appl, text="Open link", command=openLink)
texter = Label(appl, text="Warning: only open links you trust")
helpbutton = Button(appl, text="Help", command=helpsect)

txthead.place(x=10, y=3)
textout.place(x=80, y=40)
GetButton.place(x=10, y=40)
openlink.place(x=10, y=80)
texter.place(x=80, y=80)
helpbutton.place(x=500, y=80)

appl.mainloop()
