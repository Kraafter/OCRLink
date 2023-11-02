from PIL import ImageGrab, Image
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"


def ocrproc():
    try:
        image = ImageGrab.grabclipboard()
    except:
        return "Not an image file"
    else:
        try:
            image.save('C:\\AppData\\Local\\Temp\\pgetimage.png', 'PNG')
        except:
            return "Not an image file"
        else:
            textgot = str(pytesseract.image_to_string(Image.open('C:\\AppData\\Local\\Temp\\pgetimage.png')))
            os.remove('C:\\AppData\\Local\\Temp\\pgetimage.png')
            print(textgot)
            return textgot.replace('\n', '')


def splitlink(textstring=str):
    textuse = f"{textstring} l"
    foundspace = False
    gettinglink = False
    scancomplete = False
    linkgot = ''
    linkgotsave = ''
    checking = 0
    hsecure = False
    for i in textuse:
        # checks for link
        if not gettinglink and not scancomplete:
            if i == 'h' and checking == 0:
                checking = 1
                linkgot = i
            elif i == 't' and checking == 1:
                checking = 2
                linkgot = linkgot + i
            elif i == 't' and checking == 2:
                checking = 3
                linkgot = linkgot + i
            elif i == 'p' and checking == 3:
                checking = 4
                linkgot = linkgot + i
            elif i == 's' or i == ':' and checking == 4:
                if i == 's':
                    hsecure = True
                else:
                    hsecure = False
                checking = 5
                linkgot = linkgot + i
            elif i == ':' or i == '/' and checking == 5:
                checking = 6
                linkgot = linkgot + i
            elif i == '/' and checking == 6:
                if not hsecure:
                    gettinglink = True
                checking = 7
                linkgot = linkgot + i
            elif i == '/' and checking == 7:
                checking = 8
                linkgot = linkgot + i
                gettinglink = True
            else:
                checking = 0
                linkgot = ''
                hsecure = False

        elif gettinglink and not scancomplete:
            if i == ' ':
                linkgotsave = linkgot
                scancomplete = True
            elif not foundspace:
                linkgot = linkgot + i
                print(linkgot)

        elif scancomplete:
            print(linkgotsave)
            return linkgotsave
