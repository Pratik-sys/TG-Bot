import random, re

time_re = re.compile(r'^(([01]\d|2[0-3]):([0-5]\d)|24:00)$')

def getRandomWord():
  try:
    fileread = open("./Words.txt", "r")
    splitwords = fileread.read().split("\n")
    getrannumber = random.randint(0, len(splitwords)+1)
    getword  = splitwords[getrannumber]
    return getword
  except Exception as err:
    print(err)


def is_time_format(inpt):
    return bool(time_re.match(inpt))

