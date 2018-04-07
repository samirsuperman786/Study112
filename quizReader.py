import os
import random
import sys
import subprocess

quizPath = os.path.dirname(os.path.realpath(__file__)) + os.sep + "Quizzes"

#returns all the available sections
def getSections():
    sectionNames = []
    for file in os.listdir(quizPath):
        sectionNames.append(file)
    return sectionNames
    
#returns the entire path of a random quiz in a section
def getRandomQuiz(sectionName):
    quizList = os.listdir(quizPath + os.sep + sectionName)
    index = random.randint(0, len(quizList)-1)
    return quizPath + os.sep + sectionName + os.sep + quizList[index]
    
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

#checks entire solution or part of it
def checkSolution(guess, solution, index = None):
    if(index!=None):
        return guess[index] == solution[index]
    else:
        for i in range(len(guess)):
            if(guess[i] != solution[i]):
                return False
        return True
