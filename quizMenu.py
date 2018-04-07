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
        self.currentEntry = ""
        self.quizPath = ""
        self.solution = None
        self.playerEntries = []
        self.guesses = []
        height = data.height
        width = data.width
        b = Button(canvas, text = "Next Question", command = self.newQuizQuestion)
        canvas.create_window(0, height//2, anchor=NW, window=b)
        
        canvas.create_text(width//2, height//2 + 30, text = "Your Solution",
         font = "Helvetica 28 bold")
        
        b = Button(canvas, text = "Check Solution", command = self.isGuessesRight)
        canvas.create_window(100, height//2, anchor=NW, window=b)
        
        
    def isGuessesRight(self):
        guess = []
        for elem in self.guesses:
            guess.append(elem.get())
        return(checkSolution(guess,self.solution))
        
    def newQuizQuestion(self):
        height = self.data.height
        width = self.data.width
        self.quizPath = getRandomQuiz(self.sectionName)
        self.currentQuestion = getQuizPrompt(self.quizPath)
        self.solution = getQuizSolution(self.quizPath)
        for elem in self.playerEntries:
            self.canvas.delete(elem)
        
        self.guesses = []
        for i in range(len(getQuizSolution(self.quizPath))):
            e = Entry(self.canvas)
            self.guesses.append(e)
            self.playerEntries.append(self.canvas.create_window(width//2,
             height//2 + 60 + ((i) * 20), window=e))
        self.draw(self.data, self.canvas)
        
    def draw(self, data, canvas):
        height = data.height
        width = data.width
        canvas.create_rectangle(0, 0, width, height//2, width =10, fill = "white",
         outline = "red")
        canvas.create_text(width//2, 20, text = self.currentQuestion, anchor = N)
        
def test(winWidth = 1200, winHeight = 600):
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

