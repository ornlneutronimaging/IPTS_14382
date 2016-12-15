try:
    from PyQt4.QtCore import QSettings
except ImportError:
    from PyQt5.QtCore import QSettings
    
def save_config(key='', value=''):
    settings = QSettings()
    settings.setValue(key, str(value))
    
def load_config(key='', default_value=''):
    settings = QSettings()
    value = settings.value(key)
    if value is None:
        return str(value)
    else:
        return default_value


    

    
    