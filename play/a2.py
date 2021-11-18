import os

def get_file(filename):
    with open(filename,'r',encoding='utf8') as  f:
        a = f.readline();
        print(filename,a)
