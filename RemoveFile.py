import os
if os.path.exists("file-write.txt"):
    os.remove("file-write.txt")
else:
    print("File doesn't exists")
