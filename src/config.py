import configparser as cp

class Config:
    _instance = None
    def __init__(self):
        self._config_file = None
        self._config = cp.ConfigParser()

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
        return cls._instance
    
    def __getitem__(self, key):
        return self.get_config()[key]

    def set_config_file(self, config_file:str):
        if type(config_file) != str:
            raise TypeError
        self._config_file = config_file
        
    def get_config(self):
        return self._config
    
    def read(self):
        self._config.read(self._config_file)