
def find_most_common_word():
  a__dict = {}
  
  with open("article01.txt", "r") as f:
    # read line
    line = f.readline()
    while line != "":
      words = str(line).split(" ")
      lowerwords = [x.lower() for x in words]

      for word in lowerwords:  
        if word in a__dict:
          a__dict[word] += 1
        else:
          a__dict[word] = 1

      line = f.readline()

  with open("article02.txt", "r") as f:
    # read line
    line = f.readline()
    while line != "":
      words = str(line).split(" ")
      lowerwords = [x.lower() for x in words]

      for word in lowerwords:  
        if word in a__dict:
          a__dict[word] += 1
        else:
          a__dict[word] = 1

      line = f.readline()

  with open("article03.txt", "r") as f:
    # read line
    line = f.readline()
    while line != "":
      words = str(line).split(" ")
      lowerwords = [x.lower() for x in words]

      for word in lowerwords:  
        if word in a__dict:
          a__dict[word] += 1
        else:
          a__dict[word] = 1

      line = f.readline()

  with open("article04.txt", "r") as f:
    # read line
    line = f.readline()
    while line != "":
      words = str(line).split(" ")
      lowerwords = [x.lower() for x in words]

      for word in lowerwords:  
        if word in a__dict:
          a__dict[word] += 1
        else:
          a__dict[word] = 1

      line = f.readline()

  print(a__dict)

if __name__ == "__main__":
  find_most_common_word()