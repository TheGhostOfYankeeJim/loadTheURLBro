import webbrowser

file1 = open('targets.txt', 'r')
Lines = file1.readlines()

# Strips the newline character
for line in Lines:
    #print(line)
    webbrowser.get("firefox").open(line)
