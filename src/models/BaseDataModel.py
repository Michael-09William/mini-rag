from helper.config import get_settings, Settings

class BaseDataModel:
 
    def __init__(self, dbclient: object):
        self.dbclient=dbclient
        self.app_settigns=get_settings()