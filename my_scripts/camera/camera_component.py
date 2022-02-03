import bge
from collections import OrderedDict

ZOOM_VALUE = 10


class CameraComponent(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ])

    def start(self, args):
        self.mouse_up = self.object.sensors["Mouse Up"]
        self.mouse_down = self.object.sensors["Mouse Down"]

    def update(self):
        if self.mouse_up.positive:
            if self.object.lens <= 18:
                return
            self.object.lens -= ZOOM_VALUE
        
        if self.mouse_down.positive:
            if self.object.lens >= 35:
                return
            self.object.lens += ZOOM_VALUE
