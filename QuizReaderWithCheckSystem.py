from tkinter import *
from rapidFireQuiz import *
from quizReader import *

from tkinter import *

class QuizMenu(object):
    
    def __init__(self, data, canvas, sectionName):
        self.canvas = canvas
        self.data = data
        self.sectionName = sectionName
        self.currentQuestion = ""
        self.font = 10
        data.margin = 10
        self.currentEntry = ""
        self.quizPath = ""
        self.solution = None
        self.playerEntries = []
        self.answers = []
        self.guesses = []
        self.dragon = PhotoImage(file="images/112-dragon.gif")
        self.correctMark = PhotoImage(file="images/correctMark.gif")
        self.wrongMark = PhotoImage(file="images/wrongMark.gif")
        height = data.height
        width = data.width
        canvas.create_rectangle(5, height//2, 225, height//2 + 35, fill = "dodgerblue4")
        b = Button(canvas, text = "Next Question", command = self.newQuizQuestion)
        canvas.create_window(15, height//2 + 5, anchor=NW, window=b)
        
        canvas.create_text(width//2, height//2 + 30, text = "Your Solution",
         font = "Helvetica 28 bold")
        
        b = Button(canvas, text = "Check Solution", command = lambda: self.isGuessesRight(canvas,data))
        canvas.create_window(115, height//2 + 5, anchor=NW, window=b)
    def drawCheck(self,canvas,data,answer,i):
        x = data.width//2 + 100
        y = data.height//2 + 60 + (i * 20)
        if answer:
            self.answers.append(canvas.create_image(x,y,anchor=W, image = self.correctMark))
        else:
            self.answers.append(canvas.create_image(x,y,anchor=W, image = self.wrongMark))
    
    def isGuessesRight(self,canvas,data):
        guess = []
        for i in range(len(self.guesses)):
            elem = self.guesses[i]
            guess.append(elem.get())
            answer = checkSolution(guess,self.solution,i)
            self.drawCheck(canvas,data,answer,i)
        
    def newQuizQuestion(self):
        height = self.data.height
        width = self.data.width
        self.quizPath = getRandomQuiz(self.sectionName)
        self.currentQuestion = getQuizPrompt(self.quizPath)
        self.solution = getQuizSolution(self.quizPath)
        print(self.solution)
        for elem in self.playerEntries:
            self.canvas.delete(elem)
        for elem in self.answers:
            self.canvas.delete(elem)
            
        
        self.guesses = []
        for i in range(len(getQuizSolution(self.quizPath))):
            e = Entry(self.canvas)
            self.guesses.append(e)
            self.playerEntries.append(self.canvas.create_window(width//2,
             height//2 + 60 + (i * 20), window=e))
        self.draw(self.data, self.canvas)
        
    def draw(self, data, canvas):
        height = data.height
        width = data.width
        margin = 10
        canvas.create_rectangle(margin, margin,
                                width, height//2,
                                width =10, fill = "white",
                                outline = "dodgerblue4")
        canvas.create_text(width//2, 20, text = self.currentQuestion, anchor = N)
        canvas.create_text(margin, height - margin,
                           text = "Study 112", anchor = SW,
                           fill="cornflowerblue", font="Helvetica 30 italic")
        canvas.create_image(width + margin//2, height//2 + margin//2,
                            anchor=NE, image = self.dragon)
        
    
def test(winWidth = 850, winHeight = 600):
    root = Tk()
    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.pack()
    class Struct(object): pass
    data = Struct()
    data.width = winWidth
    data.height = winHeight
    data.menu = QuizMenu(data, canvas, getSections()[4])
    data.menu.newQuizQuestion()
    data.menu.draw(data, canvas)
    root.mainloop()

test()