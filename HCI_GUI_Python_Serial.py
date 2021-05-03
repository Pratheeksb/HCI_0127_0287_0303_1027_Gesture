import tkinter as tk
import tkinter.font as tkFont
import serial 
import time
import pyautogui

ArduinoSerial = serial.Serial('com3',9600) 
time.sleep(2) 

class App:
    def __init__(self, root):
        #setting title
        root.title("Gesture Based Control")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_400=tk.Button(root)
        GButton_400["bg"] = "#e66c6c"
        ft = tkFont.Font(family='Times',size=14)
        GButton_400["font"] = ft
        GButton_400["fg"] = "#000000"
        GButton_400["justify"] = "center"
        GButton_400["text"] = "Video"
        GButton_400.place(x=140,y=190,width=100,height=75)
        GButton_400["command"] = self.GButton_400_command

        GButton_932=tk.Button(root)
        GButton_932["bg"] = "#39b7ed"
        ft = tkFont.Font(family='Times',size=14)
        GButton_932["font"] = ft
        GButton_932["fg"] = "#000000"
        GButton_932["justify"] = "center"
        GButton_932["text"] = "Browser"
        GButton_932.place(x=330,y=190,width=100,height=75)
        GButton_932["command"] = self.GButton_932_command

        GMessage_794=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_794["font"] = ft
        GMessage_794["fg"] = "#333333"
        GMessage_794["justify"] = "center"
        GMessage_794["text"] = "Welcome to SwipeSense! Please choose the mode."
        GMessage_794.place(x=140,y=40,width=292,height=90)

    def GButton_400_command(self):
        while 1:
        	incoming = str (ArduinoSerial.readline())
        	print (incoming)
    
        	if 'Play/Pause' in incoming:
            		pyautogui.typewrite(['space'], 0.2)

        	if 'Rewind' in incoming:
            		pyautogui.hotkey('ctrl', 'left')  

        	if 'Forward' in incoming:
            		pyautogui.hotkey('ctrl', 'right') 

        	if 'Vup' in incoming:
            		pyautogui.hotkey('ctrl', 'down')
        

        	if 'Vdown' in incoming:
            		pyautogui.hotkey('ctrl', 'up')

        	incoming = "";


    def GButton_932_command(self):
        while 1:
        	incoming = str (ArduinoSerial.readline())
        	print (incoming)
    
        	if 'Play/Pause' in incoming:
            		pyautogui.typewrite(['space'], 0.2)

        	if 'Rewind' in incoming:
            		pyautogui.hotkey('alt', 'left')  

        	if 'Forward' in incoming:
            		pyautogui.hotkey('alt', 'right') 

        	if 'Vup' in incoming:
            		pyautogui.hotkey('up')

        	if 'Vdown' in incoming:
            		pyautogui.hotkey('down')

        	incoming = "";
 

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
