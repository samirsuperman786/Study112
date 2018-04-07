import os
import random
import sys
import subprocess

quizPath = r"C:\Users\Sam\Google Drive\College\Freshman\Spring\hack112\Quizzes"


def test():
    print(getQuizSolution(getRandomQuiz(quizPath + os.sep + getSections()[2])))
    
    
#guess for each line should in lists
def checkSolution(guess, solution):
    for i in range(len(guess)):
        if(guess[i] != solution[i]):
            return False
    return True

#needs a path to the direct file
def getQuizSolution(quiz):
    s = subprocess.check_output([sys.executable, quiz]).decode("utf-8")
    output = []
    for line in s.splitlines():
        output.append(line)
    return output
    
#returns the entire path of a random quiz
def getRandomQuiz(sectionPath):
    quizList = os.listdir(sectionPath)
    selection = random.randint(0, len(quizList)-1)
    print(sectionPath + os.sep + quizList[selection])
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

