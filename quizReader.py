import os
import random
import sys
import subprocess

quizPath = r"C:\Users\Sam\Google Drive\College\Freshman\Spring\hack112\Quizzes"


def test():
    formatQuiz(getOutputOfQuiz(getRandomQuiz(quizPath + os.sep + getSections()[0])))
    
    
#guesses should be lists
def checkSolution(guess, solution):
    formattedQuiz = format(solution) 
    return guess == formattedQuiz

def formatQuiz(solution):
    formatted = []
    solution = solution.replace("\\r", "")
    for line in solution.split("\\n"):
        formatted.append(line)
    print(formatted)

#needs a path to the direct file
def getOutputOfQuiz(quiz):
    s = subprocess.check_output([sys.executable, quiz])
    return str(s)
    
#returns the entire path of a random quiz
def getRandomQuiz(sectionPath):
    quizList = os.listdir(sectionPath)
    selection = random.randint(0, len(quizList)-1)
    return sectionPath + os.sep + quizList[selection]

def getSections():
    sectionNames = []
    for file in os.listdir(quizPath):
        sectionNames.append(file)
    return sectionNames
    

import os
def listFiles(path):
    if (os.path.isdir(path) == False):
        # base case:  not a folder, but a file, so return singleton list with its path
        return [path]
    else:
        # recursive case: it's a folder, return list of all paths
        files = [ ]
        for filename in os.listdir(path):
            files += listFiles(path + "/" + filename)
        return files

