import os

# testfile -> [b'line1', b'line2', ...]
# readlines() fails
file_name = "/home/newuser/cool_folder/20183mh.txt"
with open(file_name, "rb") as f:
        for i in range(1,1004):
            line = f.readline(50).decode('utf-8', 'ignore')
            line = line.encode('utf-8')
            print(line)






