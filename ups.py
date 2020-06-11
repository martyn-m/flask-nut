import os
from pprint import pprint
from dotenv import load_dotenv
from nut2 import PyNUTClient, PyNUTError

class Ups(PyNUTClient):

    def description(self, ups):
        self._connect()
        return super().description(ups)

    def list_ups(self):
        self._connect()
        return super().list_ups()

    def list_vars(self, ups):
        ''' Expanded list_vars
        Returns a list of dicts each containing a variables name,
        type, description and current value.
        '''

        var_list = []
        self._connect()
        source_list = super().list_vars(ups)
        for key, value in source_list.items():
            description = self.var_description(ups, key)
            variable_type = self.var_type(ups, key)
            var_list.append({'name': key, 
                             'value': value, 
                             'description': description, 
                             'type': variable_type,
            })
        return var_list

    def list_rw_vars(self, ups):
        ''' Expanded list_rw_vars
        Returns a list of dicts each containing a writeable
        variables name, type, description and current value.
        '''

        self._connect()
        var_list = []
        source_list = super().list_rw_vars(ups)
        for key, value in source_list.items():
            description = self.var_description(ups, key)
            variable_type = self.var_type(ups, key)
            var_list.append({'name': key, 
                             'value': value, 
                             'description': description, 
                             'type': variable_type,
            })
        return var_list

    def list_commands(self, ups):
        self._connect()
        return super().list_commands(ups)

    def ver(self):
        self._connect()
        return super().ver()


if __name__ == "__main__":
    basedir = os.path.abspath(os.path.dirname(__file__))
    load_dotenv(os.path.join(basedir, '.env'))
    
    host = os.environ.get('NUT_SERVER')
    port = os.environ.get('NUT_PORT') or 3493
    username = os.environ.get('NUT_USER')
    password = os.environ.get('NUT_PASSWORD')
    upsname = os.environ.get('NUT_UPS_NAME')
    
    ups = Ups(host=host, port=port, login=username, password=password)
    
    pprint(ups.list_rw_vars(upsname))
    for item in ups.list_rw_vars(upsname):
        print('Name: ' + item['name'] + ' Type: ' + item['type'])
