# Updated Animation Starter Code

from tkinter import *
from rapidFireQuiz import *
from quizReader import *

class Screen(object):
    def __init__(self, name):
        self.name = name
    
    def draw(self, canvas, data):
        pass
        
class TitleScreen(Screen):
    
    def draw(self, canvas, data):
        
        canvas.create_text(data.width/2, 0 , text = "Study 112", anchor = "n", font = "Times 30 bold")
        
        height = 100
        for topic in data.x:
            Topic = Button(canvas, text = topic, width = data.width// 10, command = changeMode(data, topic))
            canvas.create_window(data.width/2,height, window = Topic)
            #Topic.config(bg = "blue", fg = "white")
            height += 50
            
class TopicScreen(Screen):
    def draw(self, canvas, data):
        canvas.create_text(data.width/2, 0 , text = self.name, anchor = "n", font = "Times 30 bold")
        
        height = 100
        rapid = Button(canvas, text = "Rapid Fire", width = data.width//10, command = lambda: changeMode(data, "rapidFire"))
        canvas.create_window(data.width/2,height, window = rapid)
        height += 50
        
        random = Button(canvas,text = "Random Question", width = data.width//10, command = lambda: changeMode(data, "random"))
        canvas.create_window(data.width/2,height, window = random)
    
def changeMode(data, mode):
    print(data.mode)
    data.mode = mode


####################################
# customize these functions
####################################

def init(data):
    data.mode = "Title"
    data.topics = [] 
    data.x = getSections()
    for topic in data.x:
        y = TopicScreen(topic)
        data.topics += [y]
    data.title = TitleScreen("Title")

def mousePressed(event, data):
    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def redrawAll(canvas, data):
    if data.mode == "Title":
        data.title.draw(canvas, data)
    else:
        for topic in data.topics:
            if data.mode == topic.name:
                topic.draw(canvas, data)

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    redrawAll(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(1200, 600)