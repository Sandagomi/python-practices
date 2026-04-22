contents = ["import zipfile", "Export ZipFile", "Delete ZipFile"]

files = ["file1.txt", "file2.txt", "file3.txt"]


for content, file in zip(contents, files):
    
    file = open(f"/Users/sandagomithilakarathne/Desktop/Python practice/5 Processing Text Files/files{file}", 'w')
    file.write(content)
    file.close()
    
