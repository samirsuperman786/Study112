import os
import random
import sys
import subprocess

quizPath = r"C:\Users\Sam\Google Drive\College\Freshman\Spring\hack112\Quizzes"
    
def checkSolution(guess, solution):
    for i in range(len(guess)):
        if(guess[i] != solution[i]):
            return False
    return True

#needs a path to the direct file
def getQuizSolution(quizPath):
    s = subprocess.check_output([sys.executable, quizPath]).decode("utf-8")
    output = []
    for line in s.splitlines():
        output.append(line)
    return output
    
#returns the entire path of a random quiz in a section
def getRandomQuiz(sectionPath):
    quizList = os.listdir(sectionPath)
    index = random.randint(0, len(quizList)-1)
    return sectionPath + os.sep + quizList[selection]

#returns all the available sections
def getSections():
    sectionNames = []
    for file in os.listdir(quizPath):
        sectionNames.append(file)
    return sectionNames