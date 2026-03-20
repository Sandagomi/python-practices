fileNames = ["file1.txt", "file2.txt", "file3.txt"]

for filename in fileNames:
    new = filename.replace(".", "-")
    print(new)