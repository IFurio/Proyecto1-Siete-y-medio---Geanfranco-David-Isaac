def logToFile(text):
    f = open("./logfileSevenAndHalf.txt", "a")
    f.write(text + "\n")
    f.close()
