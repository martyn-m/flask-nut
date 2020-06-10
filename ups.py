from nut2 import PyNUTClient, PyNUTError

class Ups(PyNUTClient):

    def description(self, ups):
        self._connect()
        return super().description(ups)

    def list_ups(self):
        self._connect()
        return super().list_ups()

    def list_vars(self, ups):
        self._connect()
        return super().list_vars(ups)

    def list_rw_vars(self, ups):
        self._connect()
        return super().list_rw_vars(ups)

    def list_commands(self, ups):
        self._connect()
        return super().list_commands(ups)

    def ver(self):
        self._connect()
        return super().ver()