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
        self.dragon = PhotoImage(file="images/112-dragon.gif")
        height = data.height
        width = data.width
<<<<<<< HEAD
        canvas.create_rectangle(5, height//2, 225, height//2 + 35, fill = "dodgerblue4")
=======
        canvas.create_rectangle(5, height//2, width + 5, height + 1,
                                fill="lightblue2", width=0)
        canvas.create_rectangle(5, height//2, 227, height//2 + 37,
                                fill = "dodgerblue4", width = 0)
>>>>>>> 69a2035294d0c46e15e2ab48efd75b89b3874669
        b = Button(canvas, text = "Next Question", command = self.newQuizQuestion)
        canvas.create_window(15, height//2 + 5, anchor=NW, window=b)
        
        canvas.create_text(width//2, height//2 + 30, text = "Your Solution",
         font = "Helvetica 28 bold")
        
        b = Button(canvas, text = "Check Solution", command = self.isGuessesRight)
        canvas.create_window(115, height//2 + 5, anchor=NW, window=b)
        
        
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
        margin = 10
        canvas.create_rectangle(margin, margin,
                                width, height//2,
                                width =10, fill = "white",
                                outline = "dodgerblue4")
<<<<<<< HEAD
        canvas.create_text(width//2, 20, text = self.currentQuestion, anchor = N)
=======
        canvas.create_text(width//2, 56, text = self.currentQuestion, anchor = N)
>>>>>>> 69a2035294d0c46e15e2ab48efd75b89b3874669
        canvas.create_text(margin, height - margin,
                           text = "Study 112", anchor = SW,
                           fill="cornflowerblue", font="Helvetica 30 italic")
        canvas.create_image(width + margin//2, height//2 + margin//2,
                            anchor=NE, image = self.dragon)
<<<<<<< HEAD
=======
        canvas.create_text(width//2, margin,
                           text=self.sectionName, anchor=N,
                           font="Helvetica 36")
>>>>>>> 69a2035294d0c46e15e2ab48efd75b89b3874669
        
def test(winWidth = 850, winHeight = 600):
    root = Tk()
    root.title("Study 112")
    root.state('zoomed')
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