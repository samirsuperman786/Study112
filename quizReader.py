import os
import random
import sys
import subprocess

quizPath = os.path.dirname(os.path.realpath(__file__)) + os.sep + "Quizzes"


def checkSolution(guess, solution):
    for i in range(len(guess)):
        if(guess[i] != solution[i]):
            return False
    return True

#returns quiz prompt
def getQuizPrompt(quizPath):
    with open(quizPath, "r") as content_file:
        return content_file.read()
        
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
    return sectionPath + os.sep + quizList[index]

#returns all the available sections
def getSections():
    sectionNames = []
    for file in os.listdir(quizPath):
        sectionNames.append(file)
    return sectionNames