import os
import a2
current_path=os.getcwd()

file_path = os.path.join(current_path,'output')

baseze=os.path.join(file_path,'baseze')
logze=os.path.join(file_path,'logze')

if not os.path.exists(file_path):
    os.makedirs(file_path)
if not os.path.exists(baseze):
    os.makedirs(baseze)
if not os.path.exists(logze):
    os.makedirs(logze)

with open(os.path.join(baseze,'b.txt'),'w+') as f:
    f.write('------------------')
with open(os.path.join(logze,'l.txt'),'w+') as f:
    f.write('=====================')

bFile=os.path.join(baseze,'b.txt')
lFile=os.path.join(logze,'l.txt')

a2.get_file(bFile)
a2.get_file(lFile)


