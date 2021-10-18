import os
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

            

        
        self.frame_time = bgui.Frame(self, size=[0.2, 0.05], pos=[0, 0.04],
            options=bgui.BGUI_CENTERX)
        self.frame_time.colors = [(0, 0, 0, 0.3) for i in range(4)]

        # A Label Current Time
        self.lbl = bgui.Label(self.frame_time, text='',
                              pt_size=25, options=bgui.BGUI_CENTERX,
                              pos=[0, 0.3])
        

        self.win = bgui.Frame(self, size=[0.4, 0.4], pos=[0, 0.], border=1,
            options=bgui.BGUI_CENTERX | bgui.BGUI_CENTERED)
        self.win.colors = [(1, .655, .235, 1) for i in range(4)]

        self.win_title = bgui.Frame(self.win, size=[1, 0.1], pos=[0, 1], border=1,
            options=bgui.BGUI_CENTERX)
        self.win_title.colors = [(1, 150, .235, 1) for i in range(4)]

        self.label_victory = bgui.Label(self.win_title, text=f'Vitória', sub_theme="Victory",
            options=bgui.BGUI_CENTERX, pos=[0, 0.2])

        self.btn_again = bgui.FrameButton(
            self.win, text='Again', size=[0.18, 0.10], pos=[0.3, 0.2])
        self.btn_again.label.options = bgui.BGUI_CENTERX   
        self.btn_again.label.position=[0, 0.3]
        self.btn_continue = bgui.FrameButton(
            self.win, text='Continue', size=[0.18, 0.10], pos=[0.6, 0.2], )
        self.btn_continue.label.options = bgui.BGUI_CENTERX   
        self.btn_continue.label.position=[0, 0.3]
        
        self.btn_again.on_click = self.restartScenes

        self.modal_victory.append(self.label_victory)
        
        self.modal_victory.append(self.win)
        self.modal_victory.append(self.win_title)
        self.modal_victory.append(self.btn_again)
        self.modal_victory.append(self.btn_continue)
        for widget in self.modal_victory:
            widget.visible = False

    def update(self):
        self.lbl.text = f'Tempo Atual {self.timer.__str__()}'
        if self.timer.get() > 12:
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
    # print(own.name)

    if 'sys' not in own:
        own['sys'] = bgui.bge_utils.System(os.getcwd() + '/shooter/themes/default')
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
