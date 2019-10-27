import os
file_name= input("Enter file name ")
ftype = input("file type (cpp,py)")
os.system("mkdir "+str(file_name)+"&& cd "+str(file_name)+"&& echo >main.txt && start main.txt")
os.system("pause")
if ftype == "cpp":
    os.system("cd "+str(file_name)+"&& rename main.txt main.cpp")
else:
    os.system("cd "+str(file_name)+"&& rename main.txt main.py")
    
