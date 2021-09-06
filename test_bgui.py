from bgui.widget import BGUI_CACHE, BGUI_CENTERED, BGUI_CENTERX, BGUI_CENTERY
from scripts import Timer

import bgui
import bgui.bge_utils


class SimpleLayout(bgui.bge_utils.Layout):
    """A layout showcasing various Bgui features"""

    def __init__(self, sys, data):
        super().__init__(sys, data)
        self.data = data
        self.timer = Timer()

        # Add widgets here
        # Use a frame to store all of our widgets
        self.frame = bgui.Frame(self, border=0)
        self.frame.colors = [(0, 0, 0, 0) for i in range(4)]

        # A themed frame
        self.win = bgui.Frame(self, size=[0.6, 0.8],
                              options=bgui.BGUI_DEFAULT | bgui.BGUI_CENTERED)
        
        self.win_label = bgui.Frame(self, size=[0.2, 0.05], pos=[0, 0.04],
            options=bgui.BGUI_CENTERX)
        self.win_label.colors = [(0, 0, 0, 0.3) for i in range(4)]

        # A Label widget
        self.lbl = bgui.Label(self.win_label, text=f'Tempo atual {0}',
                              pt_size=25, options=bgui.BGUI_CENTERX,
                              pos=[0, 0.3])
        
        # self.image_person = bgui.Image(self, 'textures/face_player_image_small.png', size=[.08, .095], pos=[0.000001, 0.002],
		# 	options = bgui.BGUI_DEFAULT
        # )
    
    def update(self):
        # int(self.data["player"]["timer"])
        self.lbl.text = f'Tempo atual {self.timer.__str__()}'


def main(cont):
    own = cont.owner

    if 'sys' not in own:
        # Create our system and show the mouse
        own['sys'] = bgui.bge_utils.System('../../themes/default')
        own['sys'].load_layout(SimpleLayout, {"player": own})
    else:
        own['sys'].run()

def update(cont):
    own = cont.owner
    if 'sys' in own:
        own['sys'].run()
