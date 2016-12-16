try:
    from PyQt4.QtGui import QFileDialog
    from PyQt4 import QtCore, QtGui
except ImportError:
    from PyQt5.QtWidgets import QFileDialog
    from PyQt5 import QtCore, QtGui
import os
from decorators import format_directory


@format_directory
def gui_dname(dir=None, message=''):
    """Select files"""
    dirname = QFileDialog.getExistingDirectory(None, "Select Folder ...", 
                                            dir, 
                                            QFileDialog.ShowDirsOnly)
    return dirname


@format_directory
def gui_fname(dir=None, message='', ext='tif'):
    """Select one or more file via a dialog and returns the file name.
    """
    _filter = ''
    if ext == 'tif':
        _filter = "TIFF (*.tif)"
    elif ext == 'fits':
        _filter = "FITS (*.fits)"
    elif ext == 'txt':
        _filter = "ascii (*.txt)"
    elif ext == 'dat':
        _filter = "data (*.dat)"
    _filter = _filter + ";;All (*.*)"
        
    fname = QFileDialog.getOpenFileNames(None, message,
                                         directory = dir, 
                                         filter = _filter)

    return fname


@format_directory
def gui_single_file(dir=None, message=''):
    """Select one o file via a dialog and returns the file name.
    """
    if dir is None: 
        dir ='./'
    if message == '':
        message = 'Select File ...'
    fname = QFileDialog.getOpenFileName(None, message, 
            dir, filter="Spectra File (*_Spectra.txt)")
    return fname


@format_directory
def gui_csv_fname(dir=None, message=''):
    """Select one or more file via a dialog and returns the file name.
    """
    if dir is None: 
        dir ='./'
    if message == '':
        message = 'Select Files(s) ...'
    fname = QFileDialog.getOpenFileNames(None, message, 
            dir, filter="Fits files(*.csv)")
    return fname
