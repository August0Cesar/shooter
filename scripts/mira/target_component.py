import bge
from collections import OrderedDict
from mathutils import Vector

class TargetComponent(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ])

    def start(self, args):
        self.mouse_sensor = self.object.sensors["Mouse"]

    def update(self):
        if self.object["active"] and self.mouse_sensor.hitObject:
            self.object.position = self.mouse_sensor.hitPosition
            self.object.alignAxisToVect(self.mouse_sensor.hitNormal)
