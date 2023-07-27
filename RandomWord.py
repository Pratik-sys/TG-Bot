import random

def getRandomWord():
  try:
    fileread = open("./Words.txt", "r")
    splitwords = fileread.read().split("\n")
    getrannumber = random.randint(0, len(splitwords)+1)
    getword  = splitwords[getrannumber]
    return getword
  except Exception as err:
    print(err)


