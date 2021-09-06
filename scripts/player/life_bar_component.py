import bge
from collections import OrderedDict

class LifeBarComponent(bge.types.KX_PythonComponent):
    
    args = OrderedDict([])

    def start(self, args):
        pass

    def update(self):
        # interface = bge.logic.getSceneList().get("Interface_Game_Play")
        interface = bge.logic.getSceneList().get("Interface_Game_BG-UI")
        if interface:
            life_bar = interface.objects.get("lifeBar")
            hp = self.object['vida'] / 100
            if hp < 0:
                hp = 0
            if hp > 1:
                hp = 1

            life_bar.worldScale.x = hp