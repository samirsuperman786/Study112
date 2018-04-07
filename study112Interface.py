# Updated Animation Starter Code

from tkinter import *
from rapidFireQuiz import *
from quizReader import *

class Button(object):
    
    def __init__(self, left, right, top, bottom, text, connection):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
        self.text = text
        self.connection = connection
        
    def draw(self, canvas, data):
        canvas.create_rectangle(self.left,
                                self.top,
                                self.right,
                                self.bottom,
                                fill="sandybrown")
        canvas.create_text((self.left + self.right) // 2,
                           (self.top + self.bottom) // 2,
                           text=self.text,
                           fill="white")
                           
    def clicked(self, data, event):
        if self.left <= event.x <= self.right and \
           self.top <= event.y <= self.bottom:
            data.mode = self.connection
            return True

class Screen(object):
    def __init__(self, name):
        self.name = name
        self.buttons = self.makeButtons()

    def makeButtons(self):
        result = []
        height = 100
        for year in range(18, 15, -1):
            for semester in ("F", "S"):
                name = "%s%d" % (semester, year)
                connection = self.name + name
                result += [Button(50, 550, height, height + 25, name,
                                  connection)]
                height += 50
        result += [Button(25, 75, 525, 575, "To Start", "Title")]
        return result
        
    def screenMousePressed(self, event, data):
        for button in self.buttons:
            if button.clicked(data, event):
                break
            
    def draw(self, canvas, data):
        canvas.create_text(data.width // 2,
                        data.height // 10,
                        text=self.name,
                        font="Ariel 40",
                        fill="black")
        for button in self.buttons:
            button.draw(canvas, data)
            
class TitleScreen(Screen):        
    def makeButtons(self):
        result = []
        height = 100
        topics = topicList()
        for topic in topics:
            result += [Button(50, 550, height, height + 25, topic, topic)]
            height += 30
        return result
    def draw(self, canvas, data):
        canvas.create_text(data.width // 2,
                        data.height // 10,
                        text="Study112",
                        font="Ariel 40",
                        fill="black")
        for button in self.buttons:
            button.draw(canvas, data)
        
class TopicScreen(Screen):
    def makeButtons(self):
        result = []
        height = 100
        for year in range(18, 15, -1):
            for semester in ("F", "S"):
                name = "%s%d" % (semester, year)
                connection = self.name + name
                result += [Button(50, 550, height, height + 25, name,
                                  connection)]
                height += 35
        result += [Button(25, 75, 525, 575, "To Start", "Title")]
        return result

def makeTopics():
    result = []
    topics = topicList()
    for topic in topics:
        result += [TopicScreen(topic)]
    return result
    
def topicList():
    return getSections()
    
####################################
# customize these functions
####################################

def init(data):
    # load data.xyz as appropriate
    data.mode = "Title"
    data.topics = makeTopics()
    data.title = TitleScreen("Title")

def mousePressed(event, data):
    # use event.x and event.y
    if data.mode == "Title":
        data.title.screenMousePressed(event, data)
    else:
        for topic in data.topics:
            if data.mode == topic.name:
                topic.screenMousePressed(event, data)
                break
   
def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    # draw in canvas
    if data.mode == "Title":
        data.title.draw(canvas, data)
    else:
        for topic in data.topics:
            if data.mode == topic.name:
                topic.draw(canvas, data)
                break

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

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
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
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(600, 600)
