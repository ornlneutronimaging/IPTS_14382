import numpy as np


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
