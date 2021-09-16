from bge.logic import restartGame
from bgui.widget import BGUI_CACHE, BGUI_CENTERED, BGUI_CENTERX, BGUI_CENTERY
from scripts import Timer

import bgui
import bgui.bge_utils
import bge

class SimpleLayout(bgui.bge_utils.Layout):
    """A layout showcasing various Bgui features"""

    def __init__(self, sys, data):
        super().__init__(sys, data)
        self.data = data
        self.timer = Timer()
        self.modal_victory = []
        self.restartScene = False

        # Add widgets here
        # Use a frame to store all of our widgets
        self.frame = bgui.Frame(self, border=0)
        self.frame.colors = [(0, 0, 0, 0) for i in range(4)]

        # A themed frame
        self.win = bgui.Frame(self, size=[0.6, 0.8], border=0,
                              options=bgui.BGUI_DEFAULT | bgui.BGUI_CENTERED)
        self.win.colors = [(0, 0, 0, 0) for i in range(4)]    

        ############### Win Label ###############
        self.win_label = bgui.Frame(self, size=[0.2, 0.05], pos=[0, 0.04],
            options=bgui.BGUI_CENTERX)
        self.win_label.colors = [(0, 0, 0, 0.3) for i in range(4)]

        # A Label Current Time
        self.lbl = bgui.Label(self.win_label, text='',
                              pt_size=25, options=bgui.BGUI_CENTERX,
                              pos=[0, 0.3])
        ############### Win Label ###############


        self.btn_again = bgui.FrameButton(
            self.frame, text='Again', size=[0.1, 0.1], pos=[0.38, 0.5], options=bgui.BGUI_CENTERY)
        self.btn_continue = bgui.FrameButton(
            self.frame, text='Continue', size=[0.1, 0.1], pos=[0.52, 0.5], options=bgui.BGUI_CENTERY)
        
        self.btn_again.on_click = self.restartScenes

        self.modal_victory.append(bgui.Label(self.win, text=f'Vitória', sub_theme="Victory",
            options=bgui.BGUI_CENTERX, pos=[0.5, 0.6]))
        self.modal_victory.append(self.btn_again)
        self.modal_victory.append(self.btn_continue)
        for widget in self.modal_victory:
            widget.visible = False

    def update(self):
        self.lbl.text = f'Tempo Atual {self.timer.__str__()}'
        if self.timer.get() > 20:
            self.timer.stop = True
            self.data["player"]["victory"] = True
            for widget in self.modal_victory:
                widget.visible = True
    
    def restartScenes(self, widget):
        if not self.restartScene:
            self.restartScene = True
            for scene in bge.logic.getSceneList():
                scene.restart()


def main(cont):
    own = cont.owner

    if 'sys' not in own:
        own['sys'] = bgui.bge_utils.System('bgui/themes/default')
        own['sys'].load_layout(SimpleLayout, {"player": own})
    else:
        own['sys'].run()

def update(cont):
    mouse = bge.logic.mouse
    own = cont.owner
    if 'sys' in own:
        own['sys'].run()

    if own["victory"]:
        mouse.visible = True
        scene = bge.logic.getSceneList()["Scene"]
        scene.suspend()
