
import os 

rootdir = os.getcwd()
def get_uploaded_images():
    rootdir = os.getcwd()
    for files in os.walk(rootdir + '/app/static/uploads'):     
        for file in files:
            if fnmatch.fnmatch(file, '*.png'):
                print os.path.join(file)