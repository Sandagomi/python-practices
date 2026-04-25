filenames = ["file1.txt", "file2.txt", "file3.txt"]

filenames = [filename.replace('.','-') + ".exe"for filename in filenames ]

print(filenames)