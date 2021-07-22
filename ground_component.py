import bge
from collections import OrderedDict
from mathutils import Vector

class GroundComponent(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ])

    def start(self, args):
        self.mouse_sensor = self.object.sensors["Mouse"]

    def update(self):
        if self.mouse_sensor.hitObject:
            self.object.position = Vector(
                [self.mouse_sensor.hitPosition.x, self.mouse_sensor.hitPosition.y, self.object.position.z]
            )