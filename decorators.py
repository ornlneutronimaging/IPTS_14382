import os

def format_directory(function):
    '''
    This decorator will make sure the directory format is correct for the right
    os system. On Mac, pyqt does not like seing the '\' replacing the white spaces.
    '''
    
    def new_function(dir=None):

        if dir is None:
            dir = './'
        elif dir == "":
            dir = './'
        else:
            if os.sys.platform == 'darwin':
                dir = dir.replace('\\','')
        return function(dir=dir)
                
    return new_function
        