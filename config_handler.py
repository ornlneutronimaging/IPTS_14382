try:
    from PyQt4.QtCore import QSettings
except ImportError:
    from PyQt5.QtCore import QSettings
    
def init_config():
    settings = QSettings('settings.ini', QSettings.IniFormat)
    
def save_config(key='', value=''):
    settings = QSettings('settings.ini')
    if value == '':
        value = None
    settings.setValue(key, str(value))
    
def load_config(key='', default_value=''):
    settings = QSettings('settings.ini')
    value = settings.value(key)
    if (value is None) or (value == 'None'):
        return default_value
    else:
        return str(value)

    