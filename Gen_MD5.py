import os
import hashlib
path_dir = os.path.dirname( os.path.abspath( __file__ ))
file_list = os.listdir(path_dir)
for file_name in file_list : 
    if os.path.isfile(file_name):
        f = open(file_name, 'rb')
        data = f.read()
        f.close()
        print(file_name + "\n" + hashlib.md5(data).hexdigest() + "\n")

