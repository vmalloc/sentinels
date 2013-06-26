from .__version__ import __version__
import sys

_PY_2_5 = sys.version_info < (2, 6)
try:
    # python3 renamed copy_reg to copyreg
    import copyreg
except ImportError:
    import copy_reg as copyreg

class Sentinel(object):
    _existing_instances = {}
    def __init__(self, name):
        super(Sentinel, self).__init__()
        self._name = name
        self._existing_instances[self._name] = self
    def __repr__(self):
        return "<{0}>".format(self._name)
    def __getnewargs__(self):
        return (self._name,)
    def __new__(cls, name, obj_id=None): # obj_id is for compatibility with previous versions
        if name in cls._existing_instances:
            return cls._existing_instances[name]
        if _PY_2_5 :
            return super(Sentinel, cls).__new__(cls, name)
        else:
            return super(Sentinel, cls).__new__(cls)

def _sentinel_unpickler(name, obj_id=None): # obj_id is for compat. with prev. versions
    if name in Sentinel._existing_instances:
        return Sentinel._existing_instances[name]
    return Sentinel(name)
def _sentinel_pickler(sentinel):
    return _sentinel_unpickler, sentinel.__getnewargs__()


copyreg.pickle(Sentinel, _sentinel_pickler, _sentinel_unpickler)

NOTHING = Sentinel('NOTHING')
