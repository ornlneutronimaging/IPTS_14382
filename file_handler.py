import os
import pyfits
import numpy as np
import pickle

def load_data(file_name):
    '''
    load the various file_name format
    '''
    data_type = get_data_type(file_name)
    if data_type == '.fits':
        hdulist = pyfits.open(file_name)
        hdu = hdulist[0]
        _image = np.asarray(hdu.data)
        hdulist.close()
        return _image
    else:
        raise NotImplementedError
    
    
def get_data_type(file_name):
    '''
    using the file name extension, will return the type of the data
    
    Arguments:
        full file name
        
    Returns:
        file extension    ex:.tif, .fits
    '''
    filename, file_extension = os.path.splitext(file_name)
    return file_extension.strip()

def save_file(folder='', base_file_name='', suffix='', dictionary={}):
    if folder == '':
        return
    
    output_file = folder + base_file_name + '_time_dictionary.dat'
    pickle.dump(dictionary, open(output_file, "wb"))
    
    return output_file

def get_file_duration(file_name):
    hdu_list = pyfits.open(file_name)
    hdu_0 = hdu_list[0]
    return hdu_0.header['EXPOSURE']