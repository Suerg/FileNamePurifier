from Tkinter import Tk, Text, Menu, BooleanVar, Entry, StringVar, BOTH, INSERT
from ttk import Frame, Button
from tkFileDialog import askdirectory
from Tkconstants import DISABLED, NORMAL, END

class FileNamePurifierGUI(Frame):
    appWidth  = 480
    appHeight = 360
    """
    TODO: 
        add "old separators" menu (possibly including camelCase and custom)
            if(camelCase or custom):
                add logic in Parser
                
        add "preserve text" box to prevent wiping of '.' from names when needed
        add logic to make the separators exclusive 
        add logic to allow the use of camelCase as a separator
    """
    
    
    #important instance variables:
    """
    Separators:
    
    self.spacesButton
    self.underscoresButton
    self.camelcaseButton
    self.finalCustomSeparator
    self.periodButton
    """
    """
    break up by:
    
    self.breakUpByBraces
    self.breakUpByParens
    self.breakUpByBrackets
    self.breakUpByCamelCase
    """
    """
    append to:
    self.finalAppendToFrontText
    self.finalAppendToEndText
    """
    """
    misc:
    
    self.affectSubfolders
    self.cleanFolderNames
        
    self.finalRemoveFirstInstanceText
    """
    
    """
    #newSeparator is a string because self.finalCustomSeparator is a string
    newSeparator = " "
    
    if(self.underscoresButton.get()):
        newSeparator = "_"
    elif(self.camelcaseButton.get()):
        pass
    elif(len(self.finalCustomSeparator) > 0):
        newSeparator = self.finalCustomSeparator
    elif(self.periodButton.get()):
        newSeparator = "."
    
    parser = Parser(self.finalAppendToFrontText, self.finalAppendToEndText, 
    [self.finalRemoveFirstInstanceText], [], [], [' ', '_', '.'], newSeparator, 
    self.breakUpByBraces, self.breakUpByParens, self.breakUpByBrackets, self.breakUpByCamelCase, )
    """ 
    def __init__(self, parent, width, height):
        Frame.__init__(self, parent)
        self.appWidth  = width
        self.appHeight = height   
        
        self.parent = parent
        self.initUI()
        self.centerWindow()
        
        self.dir_opt = {}
    
    def askDirectory(self):
        self.addDirectoryText(askdirectory(**self.dir_opt))
        
    def addDirectoryText(self, stringToAdd):
        
        self.directoryText.config(state = NORMAL)
        self.directoryText.delete("0.0", END)
        self.directoryText.insert("0.0", stringToAdd)
        self.directoryText.config(state = DISABLED)

    
    def purifyFiles(self):
        if(hasattr(self, "finalRemoveFirstInstanceText")):
            self.addDirectoryText(self.finalRemoveFirstInstanceText)
    
    def addSubMenus(self):
        
        self.createSeparatorMenu()
        
        self.addSubCheckbuttons()
    
        self.createBreakUpByMenu()
        
        self.createAppendTextMenu()
        
        self.optionsMenu.add_command(label="Remove First Instance Of", command=self.removeFirstInstanceFrame)
        

    def submitRemoveFirstInstanceText(self):
        self.finalRemoveFirstInstanceText = self.removeFirstInstanceText.get("0.0", END)

    
    def removeFirstInstanceFrame(self):
        root = Tk()
        removeFirstInstanceFrame = Frame(root)
        
        removeFirstInstanceFrame.pack(fill=BOTH, expand=1)
        
        
        self.removeFirstInstanceText = Text(removeFirstInstanceFrame)
        self.removeFirstInstanceText.config(width = 80, height = 1)
        self.removeFirstInstanceText.pack()
        
        
        removeFirstButton = Button(removeFirstInstanceFrame, text="Submit", command=self.submitRemoveFirstInstanceText)
        removeFirstButton.pack()
        
        root.title("Enter text to remove the first instance of: ")
        

        root.mainloop() 

    
    def submitAppendToFrontText(self):
        self.finalAppendToFrontText = self.appendToFrontText.get("0.0", END)
    
    def appendToFrontFrame(self):
        root = Tk()
        
        frame= Frame(root)
        
        frame.pack(fill=BOTH, expand=1)
        
        
        self.appendToFrontText = Text(frame)
        self.appendToFrontText.config(width = 80, height = 1)
        self.appendToFrontText.pack()
        
        
        submitButton = Button(frame, text="Submit", command=self.submitAppendToFrontText)
        submitButton.pack()
        
        root.title("Enter text to append to the front: ")
        

        root.mainloop() 
    
    def submitAppendToEndText(self):
        self.finalAppendToEndText = self.appendToEndText.get("0.0", END)
    
    def appendToEndFrame(self):
        root = Tk()
        
        frame= Frame(root)
        
        frame.pack(fill=BOTH, expand=1)
        
        
        self.appendToEndText = Text(frame)
        self.appendToEndText.config(width = 80, height = 1)
        self.appendToEndText.pack()
        
        
        submitButton = Button(frame, text="Submit", command=self.submitAppendToEndText)
        submitButton.pack()
        
        root.title("Enter text to append to the end: ")
        

        root.mainloop() 
    
    def createAppendTextMenu(self):
        self.appendText             = Menu(self.optionsMenu, tearoff=0)
        
        self.appendText.add_command(label="Append To Front", command=self.appendToFrontFrame)
        self.appendText.add_command(label="Append To End", command=self.appendToEndFrame)
        
        self.optionsMenu.add_cascade(label="Append Text", menu=self.appendText)
        
    def createBreakUpByMenu(self):
        self.charBreakUpBy          = Menu(self.optionsMenu, tearoff=0)
        
        self.breakUpByBraces        = BooleanVar()
        self.breakUpByParens        = BooleanVar()
        self.breakUpByBrackets      = BooleanVar()
        self.breakUpByCamelCase     = BooleanVar()
        
        self.breakUpByParens.set(True)
        self.breakUpByBrackets.set(True)
        
        self.charBreakUpBy.add_checkbutton(label="Braces", onvalue=True, offvalue=False, variable=self.breakUpByBraces)
        self.charBreakUpBy.add_checkbutton(label="Parentheses", onvalue=True, offvalue=False, variable=self.breakUpByParens)
        self.charBreakUpBy.add_checkbutton(label="Brackets", onvalue=True, offvalue=False, variable=self.breakUpByBrackets)
        self.charBreakUpBy.add_checkbutton(label="CamelCase", onvalue=True, offvalue=False, variable=self.breakUpByCamelCase)
        
        
        self.optionsMenu.add_cascade(label="Character to Break Up By", menu=self.charBreakUpBy)
        
    
    def submitCustomSeparator(self):
        self.finalCustomSeparator = self.customSeparator.get("0.0", END)
    
    def customSeparatorFrame(self):
        root = Tk()
        
        frame= Frame(root)
        
        frame.pack(fill=BOTH, expand=1)
        
        
        self.customSeparator = Text(frame)
        self.customSeparator.config(width = 80, height = 1)
        self.customSeparator.pack()
        
        
        submitButton = Button(frame, text="Submit", command=self.submitCustomSeparator)
        submitButton.pack()
        
        root.title("Enter a custom separator:")
        

        root.mainloop() 

    
    def createSeparatorMenu(self):
        self.separatorCharMenu = Menu(self.optionsMenu, tearoff=0)
        
        self.spacesButton      = BooleanVar()
        self.underscoresButton = BooleanVar()
        
        self.separatorCharMenu.add_checkbutton(label="Spaces", onvalue=True, offvalue=False, variable=self.spacesButton)
        
        self.spacesButton.set(True)
        
        self.separatorCharMenu.add_checkbutton(label="Underscores", onvalue=True, offvalue=False, variable=self.underscoresButton)
        
            
        self.separatorCharMenu.add_command(label="Custom Separator", command=self.customSeparatorFrame)

        
        self.camelcaseButton  = BooleanVar()
        self.periodButton     = BooleanVar()
        
        self.separatorCharMenu.add_checkbutton(label="CamelCase", onvalue=True, offvalue=False, variable=self.camelcaseButton)
        self.separatorCharMenu.add_checkbutton(label="Period", onvalue=True, offvalue=False, variable=self.periodButton)
        
        self.optionsMenu.add_cascade(label="Separator Character", menu=self.separatorCharMenu)

         
    
    def addSubCheckbuttons(self):
        self.affectSubfolders = BooleanVar()
        self.cleanFolderNames = BooleanVar()
        
        self.optionsMenu.add_checkbutton(label="Affect Subfolders", onvalue=True, offvalue=False, variable=self.affectSubfolders)
        self.optionsMenu.add_checkbutton(label="Clean Folder Names", onvalue=True, offvalue=False, variable=self.cleanFolderNames)
        
        self.affectSubfolders.set(True)
        self.cleanFolderNames.set(True)
        
    def initUI(self):
        self.parent.title("Filename Purifier")
        self.pack(fill=BOTH, expand=1)
        
        self.directoryButton = Button(self, text="Choose Directory", command=self.askDirectory)
        self.directoryButton.place(x = self.appWidth/3, y = 70)
        
        self.directoryText = Text()
        self.directoryText.config(width = 40, height = 1)
        self.directoryText.config(state = DISABLED)
        self.directoryText.place(x = 100, y = 120)
        
        self.purifyButton = Button(self, text="Purify Files", command=self.purifyFiles)
        self.purifyButton.place(x = self.appWidth/3 + 25, y = 170)
        
        self.menubar = Menu(self)
        
        self.optionsMenu = Menu(self.menubar, tearoff=0)
        
        self.addSubMenus()
        
        self.menubar.add_cascade(label="Options", menu=self.optionsMenu)
        
        self.parent.config(menu=self.menubar)
    
    def centerWindow(self):
        screenWidth  = self.parent.winfo_screenwidth()
        screenHeight = self.parent.winfo_screenheight()
        
        x = (screenWidth - self.appWidth)/2
        y = (screenHeight - self.appHeight)/2
        self.parent.geometry('%dx%d+%d+%d' % (self.appWidth, self.appHeight, x, y))

def main():
    root = Tk()
    app = FileNamePurifierGUI(root, 480, 360)
    root.mainloop()  

main()