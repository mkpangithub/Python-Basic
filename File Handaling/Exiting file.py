f = open("demofile.txt", "x")
f.write("Woops! I have deleted the content!")
f.close()

f = open("demofile.txt", "r")
print(f.read())