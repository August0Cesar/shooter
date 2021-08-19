import bge
from collections import OrderedDict

class GoopCollideComponent(bge.types.KX_PythonComponent):
    args = OrderedDict([])

    def start(self, args):
        self.object.collisionCallbacks.append(self.on_collison)
        self.objects_collide = self.object["objects_collide"].split(",")
        self.colidiu = False
    
    def update(self):
        ...
    
    def on_collison(self, obj):
        if obj.name in self.objects_collide:
            if not self.colidiu:
                self.colidiu = True
                obj['vida'] -= 20