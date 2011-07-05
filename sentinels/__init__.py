from .__version__ import __version__

class Sentinel(object):
    _existing_instances = {}
    def __init__(self, name):
        super(Sentinel, self).__init__()
        self._existing_instances[id(self)] = self
        self._name = name
    def __repr__(self):
        return "<{0}>".format(self._name)
    def __getnewargs__(self):
        return (self._name, id(self))
    def __new__(self, name, obj_id=None):
        if obj_id in self._existing_instances:
            return self._existing_instances[obj_id]
        return super(Sentinel, self).__new__(self, name)

NOTHING = Sentinel('NOTHING')
