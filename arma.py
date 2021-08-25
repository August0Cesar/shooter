import bge
from collections import OrderedDict

class ArmaComponent(bge.types.KX_PythonComponent):
    args = OrderedDict([])

    def start(self, args):
        ...
    
    def update(self):
        print(self.object.worldOrientation)