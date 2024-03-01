print("Hi :)")
searchVar = input("Enter what word you want to look for: ")

num_watch = 0
with open("x-files.txt","r") as f:
    # inside here the f file is open for reading
    # print(f.read())
    for line in f:
        num_watch += line.lower().count(searchVar)

print("the word",searchVar, "shows up", num_watch,"times in the file.")
