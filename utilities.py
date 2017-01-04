import numpy as np
import os


def calculate_file_temperature(left_T=-1, right_T=-1, left_time=-1, right_time=-1, file_time = -1):
    coeff = (float(right_T) - float(left_T)) / (float(right_time) - float(left_time))
    part1 = coeff * (float(file_time) - float(left_time))
    return part1 + float(left_T)

def get_first_temperature_and_index_value(index=-1, data_array=[], direction='left'):
    if direction == 'left':
        coeff = -1
    else:
        coeff = 1

    while (np.isnan(data_array[index])):
        index += coeff
    return [data_array[index], index]

def extract_temperature(index=-1, temperature_array=[], time_stamp_array=[]):
    
    [left_T, left_index] = get_first_temperature_and_index_value(index=index, data_array=temperature_array, direction='left')
    [right_T, right_index] = get_first_temperature_and_index_value(index=index, data_array=temperature_array, direction='right')
    
    left_time = time_stamp_array[left_index]
    right_time = time_stamp_array[right_index]
    
    file_time = time_stamp_array[index]

    file_temperature = calculate_file_temperature(left_T = left_T, right_T = right_T, 
                                                 left_time = left_time, right_time = right_time,
                                                 file_time = file_time)

    return file_temperature

def retrieve_T_from_file_vs_temperature_array(file_name='', file_array=[], temperature_array=[]):
    index = file_array.index(file_name)
    return temperature_array[index]

def make_output_file_name(_files_to_merge, algorithm='mean'):
    '''
    takes the list of files to add and create the output file name 
    
    Paramters:
        * _files_to_merge: list of files to merge
        * algorithm: (optional) default value 'add'. Name of algorithm used to bin data
            will be used in the new output file name
            
    Return:
        * string file name of the output file
        
    Example:
        _files_to_merge = []'/Users/me/Image0001_00000.fits','/Users/me/Image0002_00000.fits']
        
        will return  'Image00001_Image00002_0000_add.fits
    
    '''
    
    ext = '.fits'
    list_output_file_name = []
    
    for _file in _files_to_merge:
            _basename = os.path.basename(_file)
            [_basename, suffix] = _basename.split('_')
            list_output_file_name.append(_basename)

    _output_file_name = '_'.join(list_output_file_name)
    return (_output_file_name, _output_file_name + '_' + algorithm + '.' + suffix)

def keep_folder_name(image):
    image_array = image.split('_')
    return image_array[0]

def is_extension(filename='', ext='.fits'):
    _ext = os.path.splitext(filename)[1]
    if _ext == ext:
        return True
    else:
        return False
    
