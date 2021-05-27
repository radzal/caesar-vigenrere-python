#2020

#!/usr/bin/python

import sys
import getopt
import time
import random

from tkinter import filedialog as fd
from tkinter import *
from tkinter import scrolledtext, Tk, Label, Button, Menu
from tkinter import messagebox

from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror

from tkinter import ttk
from tkinter.ttk import *
import tkinter.font as tkFont



    
class MyFirstGUI:
    
    def __init__(self, master):     # GUI function and widgets initiation 
        self.master = master        # 
        master.title("Caesar GUI")
        
        self.initUI()               # init window
        
        selected = IntVar()
        
        
        # Create Frame widget
        m_frame = Frame(master, width=600, height=580)      # size in pixs
        m_frame.grid(row=1, column=0, padx=10, pady=5)      # position and paddings
        
        top_m_frame = Frame(m_frame, width=180, height=50)
        top_m_frame.grid(row=1, column=0, padx=10, pady=5)
        
        ra_frame = Frame(m_frame, width=180, height=50)
        ra_frame.grid(row=0, column=0, padx=10, pady=5)
        
        btn_frame = Frame(m_frame, width=400, height=580)
        btn_frame.grid(row=5, column=0, padx=10, pady=5)
        
       # RadioButtons Labels
        self.lblRadioC = Label(ra_frame, text="Caesar",font=("Arial Bold", 10)) # where nested, name, font
        self.lblRadioC.grid(column=0, row=1, padx=10, pady=10)                  # position and paddings
        self.lblRadioC.configure(foreground="green")                            # colour
        
        self.lblRadioV = Label(ra_frame, text="Vigenère",font=("Arial Bold", 10))
        self.lblRadioV.grid(column=4, row=1, padx=10, pady=10)
        self.lblRadioV.configure(foreground="black")
        
        # Radiobutton block
        self.selected = IntVar()
        self.selected.set(1)
        self.rad1 = Radiobutton(ra_frame,text='Encrypt', value=1, variable = self.selected, command=self.sel) # calls def sel
        self.rad2 = Radiobutton(ra_frame,text='Decrypt', value=2, variable = self.selected,command=self.sel)
        self.rad3 = Radiobutton(ra_frame,text='Brute Force', value=3, variable = self.selected,command=self.sel)
        self.rad4 = Radiobutton(ra_frame,text='Encrypt', value=4, variable = self.selected,command=self.sel)
        self.rad5 = Radiobutton(ra_frame,text='Decrypt', value=5, variable = self.selected,command=self.sel)
        
        # Radiobutton position
        self.rad1.grid(column=0, row=2, padx=6)
        self.rad2.grid(column=1, row=2, padx=6)
        self.rad3.grid(column=2, row=2, padx=6)
        # spacers in some frames
        ra_frame.grid_columnconfigure(3, minsize=40)
        self.rad4.grid(column=4, row=2, padx=4)
        self.rad5.grid(column=5, row=2, padx=4)
        
        # Buttons
        self.force_button = Button(btn_frame, text="       EXECUTE       ", command=self.execute)
        self.force_button.grid(column=1, row=0, padx=8, pady=10)
        
        btn_frame.grid_columnconfigure(2, minsize=80)

        self.reset_button = Button(btn_frame, text="RESET", command=self.reset)
        self.reset_button.grid(column=3, row=0, padx=30, pady=10)
        
        self.close_button = Button(btn_frame, text="CLOSE", command=master.destroy)
        self.close_button.grid(column=4, row=0, padx=8, pady=10)
        
        
        
        self.label = Label(top_m_frame, text="Input shift number",font=("Arial Bold", 10))
        self.label.grid(sticky="W", column=0, row=0, padx=3, pady=10)
        
        self.txtInput = Entry(top_m_frame, width = 2, font=("Courier", 10))
        self.txtInput.grid(sticky="E", column=1, row = 0, padx=4, pady=10)
        self.txtInput.config(state = 'normal')
        
        self.txtInputLength = Entry(top_m_frame, width = 2, font=("Courier", 10))
        
        
        self.labelOr = Label(top_m_frame, text="or",font=("Arial Bold", 10))
        self.keyGen_button = Button(top_m_frame, text="GENERATE", command=self.kGen)
        self.labelLenght = Label(top_m_frame, text="lenght (3-12)",font=("Arial Bold", 10))
                
        
        self.lblInput = Label(m_frame, text="Input plane text",font=("Arial Bold", 10))
        self.lblInput.grid(sticky="NW",column=0, row=2, padx=10, pady=10)
        
        self.txtBoxIn = scrolledtext.ScrolledText(m_frame, width=40,height=10, font=8)
        self.txtBoxIn.grid(column=0, row=3, padx=10, pady=10)
        self.txtBoxIn.focus()
        
        self.lblOut = Label(m_frame, text="Encoded text",font=("Arial Bold", 10))
        self.lblOut.grid(sticky="NW",column=0, row=6, padx=10, pady=10)
        
        self.txtBoxOut = scrolledtext.ScrolledText(m_frame, width=40,height=10, font=8)
        self.txtBoxOut.grid(column=0, row=7, padx=10, pady=10)
        self.txtBoxOut.bind("<1>", lambda event: self.txtBoxOut.focus_set()) # enable Ctrl+C on 'no-edit' textbox
        
    def oFile(self):    # open file
        
        self.filename =  fd.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Text Files", "*.txt"),("all files","*.*")))
        
        fl = self.filename
        with open(fl, 'r') as file:
            data = file.read().replace('\n', '')
        self.txtBoxIn.insert(END, data[1:])
        
        
    def file_save(self):    # save file
        
        self.txtBoxOut.config(state='normal')
        self.fileToSave = fd.asksaveasfile(mode='w', defaultextension=".txt")
        if self.fileToSave is None: # if return `None` if dialog closed with "cancel".
            return
        self.text2save = str(self.txtBoxOut.get(1.0, END)) # starts from `1.0`, not `0.0`
        self.txtBoxOut.config(state='disabled')
        self.fileToSave.write(self.text2save)
        self.fileToSave.close()
        
    
    def initUI(self):   # init menu
        self.menubar = Menu(self.master)
        self.master.config(menu=self.menubar)
        
        self.fileMenu = Menu(self.menubar)
        self.helpMenu = Menu(self.menubar)
        
        self.menubar.add_cascade(label="File", underline = 0, menu=self.fileMenu)        
        self.fileMenu.add_command(label="Open", underline = 0, command=self.onOpen)
        self.fileMenu.add_command(label="Save as...", underline = 0, command=self.onSave)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", underline = 1, command=self.onExit)

        self.menubar.add_cascade(label="Help", underline = 0, menu=self.helpMenu)
        self.helpMenu.add_command(label="Handbook", underline = 3, command=self.onHandbook)
        self.helpMenu.add_command(label="About...", underline = 0, command=self.onAbout)

        
    def onExit(self):   # exit to system
        sys.exit(2)
        
    def onOpen(self):   # wraper for open file
        self.oFile()
        
    def onSave(self):   # wraper for save file
        self.file_save()
    
    def sel(self):  # window widgets set up for each Radiobutton

        if self.selected.get() == 1:
            self.labelOr.grid_forget()
            self.keyGen_button.grid_forget()
            self.txtInputLength.grid_forget()
            self.labelLenght.grid_forget()
            self.label.configure(text="Input shift number")
            self.lblInput.configure(text = 'Input plane text:')
            self.lblOut.configure(text = 'Caesar encoded text:')
            self.reset()
            self.txtInput.config(width = 2)
            self.txtInput.config(state = 'normal')
            self.lblRadioC.configure(foreground="green")
            self.lblRadioV.configure(foreground="black")
        
        elif self.selected.get() == 2:
            self.labelOr.grid_forget()
            self.keyGen_button.grid_forget()
            self.txtInputLength.grid_forget()
            self.labelLenght.grid_forget()
            self.label.configure(text="Input shift number")
            self.lblInput.configure(text = 'Input Caesar encoded text:')
            self.lblOut.configure(text = 'Decoded text:')
            self.reset()
            self.txtInput.config(width = 2)
            self.txtInput.config(state = 'normal')
            self.lblRadioC.configure(foreground="green")
            self.lblRadioV.configure(foreground="black")
            
        elif self.selected.get() == 3:
            self.labelOr.grid_forget()
            self.keyGen_button.grid_forget()
            self.txtInputLength.grid_forget()
            self.labelLenght.grid_forget()
            self.label.configure(text="Input shift number")
            self.lblInput.configure(text = 'Input Caesar encoded text:')
            self.lblOut.configure(text = 'All possible combinations:')
            self.reset()
            self.txtInput.config(width = 2)
            self.txtInput.config(state = 'disabled')
            self.lblRadioC.configure(foreground="green")
            self.lblRadioV.configure(foreground="black")
            
        elif self.selected.get() == 4:
            self.labelOr.grid(column=2, row=0, padx=2, pady=10)
            self.keyGen_button.grid(column=3, row=0, padx=2, pady=10)
            self.txtInputLength.grid(column=4, row = 0, padx=2, pady=10)
            self.labelLenght.grid(column=5, row = 0, padx=2, pady=10)
            self.txtInputLength.config(state = 'normal')
            self.label.configure(text="Input key")
            self.lblInput.configure(text = 'Input plane text:')
            self.lblOut.configure(text = 'Vigenère encoded text:')
            self.reset()
            self.txtInput.config(width = 12)
            self.txtInput.config(state = 'normal')
            self.lblRadioC.configure(foreground="black")
            self.lblRadioV.configure(foreground="green")
            
            
        elif self.selected.get() == 5:
            self.labelOr.grid_forget()
            self.keyGen_button.grid_forget()
            self.txtInputLength.grid_forget()
            self.labelLenght.grid_forget()
            self.label.configure(text="Input key")
            self.lblInput.configure(text = 'Input Vigenère encoded text:')
            self.lblOut.configure(text = 'Decoded text:')
            self.reset()
            self.txtInput.config(width = 12)
            self.txtInput.config(state = 'normal')
            self.lblRadioC.configure(foreground="black")
            self.lblRadioV.configure(foreground="green")
            
            

    def encode(self):   #encode wraper for encoding function and input validation

        toEncode = self.txtBoxIn.get('1.0', END) # string ro encode
        
        shiftV = self.txtInput.get()    # shifting value
        # is number? and range
        if (shiftV.isnumeric() is not True) or int(shiftV) < int(0) or int(shiftV) > int(25):
            messagebox.showwarning('Error', 'The value in Input shift value box\n must be betwenn 0 and 25')
            self.txtInput.delete(0, 'end')
            
        elif not toEncode.strip():
            
            messagebox.showwarning('Error', 'Input plane text is empty') #message box

        else:
            self.txtBoxOut.config(state='normal')        
            # calling encrypt function (str to encode and shifting value)
            decode = str(enString(toEncode, int(shiftV)))
            self.txtBoxOut.insert(INSERT, decode)   #return encoded value
        
        self.txtBoxOut.config(state='disabled')
        
        
    def decode(self):   # wraper works like encode() just calling deString function

        toEncode = self.txtBoxIn.get('1.0', END)
        
        shiftV = self.txtInput.get()
        if (shiftV.isnumeric() is not True) or int(shiftV) < int(0) or int(shiftV) > int(25):
            messagebox.showwarning('Error', 'The value in Input shift value box\n must be betwenn 0 and 25')
            self.txtInput.delete(0, 'end')
            
        elif not toEncode.strip():
            
            messagebox.showwarning('Error', 'Input plane text is empty')

        else:
            self.txtBoxOut.config(state='normal')        
            
            decode = str(deString(toEncode, int(shiftV)))
            self.txtBoxOut.insert(INSERT, decode)
        
        self.txtBoxOut.config(state='disabled')
        
    def force(self):    # function to brute force Caesar
        
        toDecode = self.txtBoxIn.get('1.0', END)
        for element in range(1, 26):    #looping 26 times (26 characters)
                execute = str(element) + '\t' + str(deString(toDecode, element))
                self.txtBoxOut.insert(INSERT, execute)
        self.txtBoxOut.config(state='disabled')
        
    def encodeV(self):  # wraper for enVen() - encode Vigenère Cypher

        toEncode = self.txtBoxIn.get('1.0', END)    # string to encode from input box
        shiftV = self.txtInput.get()                # encoding key
            
        if not toEncode.strip():
            messagebox.showwarning('Error', 'Input plane text is empty')
        else:
            self.txtBoxOut.config(state='normal')   # set output txt as editable
            decode = str(enVen(toEncode, str(shiftV)))  # call encoding function and assign to var
            self.txtBoxOut.insert(INSERT, decode)   # return encoded value
        self.txtBoxOut.config(state='disabled')     # disable output txtbox fromedition
        
    def decodeV(self):  # wraper for deVen() - encode Vigenère Cypher 

        toEncode = self.txtBoxIn.get('1.0', END)
        shiftV = self.txtInput.get()
            
        if not toEncode.strip():
            messagebox.showwarning('Error', 'Input plane text is empty')
        else:
            self.txtBoxOut.config(state='normal')        
            decode = str(deVen(toEncode, str(shiftV)))
            self.txtBoxOut.insert(INSERT, decode)
        self.txtBoxOut.config(state='disabled')
        
    def execute(self):  # 'execute' button control in accordancy to sellected Radiobutton

        if self.selected.get() == 1:
            self.encode()
                  
        elif self.selected.get() == 2:
            self.decode()
                  
        elif self.selected.get() == 3:
            self.force()
            
        elif self.selected.get() == 4:
            self.encodeV()
            
        elif self.selected.get() == 5:
            self.decodeV()

    def kGen(self): # random key generator
        self.txtInput.delete(0, 'end')
        lght = self.txtInputLength.get()
        
        if (lght.isnumeric() is not True) or int(lght) < int(3) or int(lght) > int(12):
            messagebox.showwarning('Wrong Input', 'Only numers in range 3-12')
            self.txtInputLength.delete(0, 'end')
        #elif int(lght) < int(3) or int(lght) > int(25):
            #messagebox.showwarning('Wrong Input', 'Only numers in range 3-12')
            
        else:
            self.txtInput.insert(INSERT, str(keyGen(int(lght))))

    def reset(self):    # reset all values and widgets to defaults
        
        self.txtBoxOut.config(state='normal')
        self.txtInput.delete(0, 'end')
        self.txtInputLength.delete(0, 'end')
        self.txtBoxIn.delete('1.0' , END)
        self.txtBoxOut.delete('1.0' , END)
        
    def clicked(self): # not implemented yet

        messagebox.showinfo('Message title', 'Message content')
        
    def onHandbook(self): # not implemented yet
        self.popupmsg()
            
    def onAbout(self):  # About.. popup
        
        messagebox.showinfo('About...', 'Caesar Cypher Utillity\n\nCreated by Rad Zaleski\nGlyndwr Univesity\nWrexham\n2020')
        

    def popupmsg(self): # popup window init
        self.popup = Toplevel()
        self.popup.grab_set
        self.popup.geometry('600x400+400+400')
        self.popup.wm_title("Handbook")

        self.txtBoxPopUp = scrolledtext.ScrolledText(self.popup, width=40,height=16, font=7)
        self.txtBoxPopUp.pack(side="top", fill="x", pady=10)
        self.txtBoxPopUp.config(wrap=WORD)
        self.txtBoxPopUp.insert(INSERT, "This program is designed to perform Caesar and Vigenere encryption and decryption task. Caesar section is also able to brute force the encrypted message. For both, Caesar and Vigenere Ciphers is possible to load or save generated messages.\n\nProgram can be used with GUI and CLI environments (CLI uses in-line parameters).\n\nAbout Ciphers: \n\nCAESAR CIPHER\nThe action of a Caesar cipher is to replace each plaintext letter with a different one a fixed number of places down \nthe alphabet. The cipher illustrated here uses a left shift of three, so that (for example) each occurrence of E in the plaintext becomes B in the ciphertext. \n\nVIGENERE CIPHER\nThe Vigenère cipher is a method of encrypting alphabetic text by using a series of interwoven Caesar ciphers, based on the letters of a keyword. It employs a form of polyalphabetic substitution.\n\n Usage:\nSyntax:\npython3 Caesar.py [parameter] [message] [shift value]\nNote:\nText string with spaces needs commas\nUsage:\n-e\t- encoding with given shift parameter\n-d\t- decoding with known shift parameter\n-f\t- finding hidden message using brute force\n-eV\t- encoding using Vigenère cypher with literal key\n-dV\t- encoding using Vigenère cypher with literal key\n-gui\t- run with graphic user interface")
        
        self.B1 = Button(self.popup, text="Okay", command = self.popup.destroy)
        self.B1.pack()
        self.popup.mainloop()
        
    # -------------- END GUI ----------------

# ----------- Core ---------------------
# Used directly in CLI and in wrappers in GUI

# the core - encrypting function used for Caesar Cypher and Vigenère Cypher
def encrypt(charIn, cValue):

    ch = charIn                                                     # input character (char)
    codeValue = cValue                                              # inout shift value (int)
    if ch.encode('ascii').isalpha() == False:                       # break if not char (return unchanged value)
        return ord(ch)
    offset = 'A' if ch.isupper() else 'a'                           # offset for lowcase and Caps (return char)
    
    # to asci(character) + shift - mod(lowcase/Caps offset) + offset
    ch = ((ord(ch) + codeValue - ord(offset)) % 26 + ord(offset))
    #print('dec\t',ch,'\tchar',chr(ch))
    return ch

def enString(deMessage, val):   # put encoded chars to string (could be in one function but it distingue steps)
    toString = ''
    deMess = deMessage
    for element in deMess: 
        toString +=  chr(encrypt(element, val))
    return toString
    
def deString(enMessage, val):   # put decoded chars to string (could be in one function but it distingue steps)
    # referse proces of encoding by substracting number 26 (number of letters) by shift value
    toString = ''

    enMess = enMessage
    for element in enMess: 
        toString +=  chr(encrypt(element, 26 - val))
    return toString
    
def force(stringToForce):   # force loop
    for element in range(26):   # looping range 26
        print(str(element) + '\t' + str(deString(stringToForce, element)))
        if element == 0:
            #element = ''
            print('\n------------------ SEARCHING... -------------------')
        time.sleep(0.2) # delay just to make presentation more natural
    print('-------------------- FINISHED ---------------------')
        

def enVen(txtVenIn, keyVen):    # Vigenère Cypher encription function
    
    ind = 0
    outEnVen = ''

    for indStr, value in enumerate(txtVenIn):   # loop through each character in string
        if value.encode('ascii').isalpha() == False:                       # break if not char (return unchanged value)
           ind = ind-1
        
        offVen = 'A' if keyVen[ind].isupper() else 'a'  # is char Upper or lowcase
        # calling encrypt() (same like in Caesar) and passing chars one by one pulled from string and key in parallel
        outEnVen += chr(encrypt(value, ord(keyVen[ind])-ord(offVen)))   
        # counting key index possible if larger then key length reset to zero and incrase again in each step to the ond
        # of encripting string
        if ind == (len(keyVen))-1:
            ind = 0
        else:
            ind += 1
    # returns encrypted string
    return outEnVen
            
            
def deVen(txtVenIn, keyVen):    # Vigenère Cypher decription function same as enVen() but substract shift from 26
    
    ind = 0
    outDeVen = ''

    for indStr, value in  enumerate(txtVenIn):
        if value.encode('ascii').isalpha() == False:        # break if not char (return unchanged value)
           ind = ind-1                                      # Keyword index one step back
        offVen = 'A' if keyVen[ind].isupper() else 'a'      # Offset for Cap or lowcase
        shift = ord(keyVen[ind])-ord(offVen)                # Shift for each input char about complementing key char
        outDeVen += chr(encrypt(value, 26 - shift))         # returned decoded char and added to string
        
        if ind == (len(keyVen))-1:                          # wrapping key around
            ind = 0
        else:
            ind += 1
            
    return outDeVen
        
def keyGen(kLength):    # key gen pseudo rendomising function (not used in CLI
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    keyR = ''
    for c in range(kLength):
        keyR += random.choice(chars)
    return keyR

def help(): #help
    print('Program is encoding and decoding the text string with given shift value')
    print('using Caesar cipher algorithm also can decrypt message without known')
    print('shift value using brute force technique.')
    print('Program is able to encode and decode using Vigenère Cypher')
    print('\nSyntax:')
    print('\tPython3 Caesar.py [parameter] [message] [shift value]\n')
    print('Note:')
    print('\tText string with spaces needs commas\n')
    print('\nUsage:')
    print('\t-e\t- encoding with given shift parameter')
    print('\t-d\t- decoding with known shift parameter')
    print('\t-f\t- finding hidden message using brute force')
    print('\t-eV\t- encoding using Vigenère cypher with literal key')
    print('\t-dV\t- encoding using Vigenère cypher with literal key')
    print('\t-gui\t- run with graphic user interface\n')

# ----------------- MAIN ------------------

def main():
    
   
    print('\n')
    try:            # CLI line argument selection
        if len(sys.argv) == 2:
            if sys.argv[1] == '-h':
                help()
                sys.exit(2)
                
            elif sys.argv[1] == '-gui':
                root = Tk()
                my_gui = MyFirstGUI(root)
                root.mainloop()
            else:
                help()
                sys.exit(2)
                
        # -- FORCE ---
        elif len(sys.argv) == 3 and sys.argv[1] == '-f':
            msgIn = sys.argv[2]
            force(msgIn)
        elif len(sys.argv) < 3 and sys.argv[1] == '-f':
            help()
            sys.exit(2)
        # -- Encrypt --
        elif len(sys.argv) == 4 and sys.argv[1] == '-e':
            msgIn = sys.argv[2]
            val = int(sys.argv[3])
            enStr = enString(msgIn, val)
            print(enStr)
            
        # -- Decrypt --
        elif len(sys.argv) == 4 and sys.argv[1] == '-d':
            enStr = sys.argv[2]
            val = int(sys.argv[3])
            print(deString(enStr, val))
            
        # -- Encrypt Vigenère --
        elif len(sys.argv) == 4 and sys.argv[1] == '-eV':
            enStr = sys.argv[2]
            val = str(sys.argv[3])
            vEnStr = enVen(enStr, val)
            print(vEnStr)
            
        # -- Decrypt Vigenère --
        elif len(sys.argv) == 4 and sys.argv[1] == '-dV':
            enStr = sys.argv[2]
            val = str(sys.argv[3])
            vDeStr = deVen(enStr, val)
            print(vDeStr)
            
        # -- Error trap --
        else:
            print('Missing parameters.')
            print('Use:\n\t-h\tfor help\n')
            sys.exit(2)     
            
        # -- Exception --
    except IndexError:
        print('Missing parameters.')
        print('Use:\n\t-h\tfor help\n')
        sys.exit(2)
        
    print('\n')
    



if __name__ == "__main__":

    main()
    
    
    
    
