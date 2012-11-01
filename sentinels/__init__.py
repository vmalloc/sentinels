from .__version__ import __version__
import platform

_PY_3_3 = platform.python_version() >= "3.3.0"
try:
    # python3 renamed copy_reg to copyreg
    import copyreg
except ImportError:
    import copy_reg as copyreg

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
    def __new__(cls, name, obj_id=None):
        if obj_id in cls._existing_instances:
            return cls._existing_instances[obj_id]
        if _PY_3_3:
            return super(Sentinel, cls).__new__(cls)
        else:
            return super(Sentinel, cls).__new__(cls, name)

def _sentinel_unpickler(name, obj_id):
    if obj_id in Sentinel._existing_instances:
        return Sentinel._existing_instances[obj_id]
    return Sentinel(name)
def _sentinel_pickler(sentinel):
    return _sentinel_unpickler, sentinel.__getnewargs__()


copyreg.pickle(Sentinel, _sentinel_pickler, _sentinel_unpickler)

NOTHING = Sentinel('NOTHING')
