from tkinter import *

def runCode(event=None):
    global userResult
    result = userResult.split("\n")
    print(result)
    
def newLine(event=None):
    global userResult
    userResult = userResult + "\n"
    return userResult
    
def run(width=300,height=300):
    global userResult
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    #checkCodeScreen(canvas,data)
    textEntry = StringVar()
    textEntry.set(userResult)
    userResult = textEntry.get()
    textBox = Entry(canvas,textvariable=textEntry)
    canvas.create_window(width//2, height//2, 
        window=textBox, height=height//3, width=width//2)
    checkSol = Button(canvas,text="Check Solution", command=runCode)
    checkSol.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
    canvas.create_window(10, 10, anchor=NW, window=checkSol)
    
    textBox.bind('<Return>', newLine)
    userResult = newLine()
    root.mainloop()
global userResult
userResult = "Stay Gold Ponyboy"
run()

