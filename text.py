import fnmatch
import os 

def get_uploaded_images():
    ##images = []
    rootdir = os.getcwd()
    for files in os.walk(rootdir + '/app/static/uploads'):     
        for file in files:
            ##images.append( 2009 )
            ##print os.path.join(file)
            print('test')
            
def get_uploaded_imagess():
    images = []
    rootdir = os.getcwd()
    for files in os.walk(rootdir + '/app/static/uploads'):     
        for file in files:
            ##images.append( 2009 )
            Image=os.path.join(file)
            print(Image)
            images.append(Image)
    return(images)