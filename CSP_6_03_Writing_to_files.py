import random

def writeFile(inputList, fileName):
    file = open(fileName, "w")
    for item in inputList:
        file.write(item + "\n")
    file.close()

def sortNames(fileName, targetFile):
    file = open(fileName, "r")
    names = file.readlines()
    file.close()

    names = [name.strip() for name in names]
    names.sort()

    file = open(targetFile, "w")
    for name in names:
        file.write(name + "\n")
    file.close()

sortNames("names.txt", "namesNew.txt")

def highScore(newScore: int):
    file = open("scores.txt", "a")
    file.write(str(newScore) + "\n")
    file.close()

    file = open("scores.txt", "r")
    scores = file.readlines()
    file.close()

    scores = [int(score.strip()) for score in scores]
    average = sum(scores) / len(scores)
    return average

print(highScore(random.randint(1, 100)))
