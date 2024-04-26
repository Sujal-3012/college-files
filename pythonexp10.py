import os 
import shutil
with open('new.txt' , 'w') as f:
    f.write("This is a python file in computer science ")

with open('new.txt' , 'r') as f:
    data = f.read()
    print(data)

with open('copied_expt.txt' , 'w') as f:
    shutil.copy('new.txt' , 'copied_expt.txt')


with open('copied_expt.txt' , 'r') as fn:
    data_new = fn.read()
    print(data_new)
