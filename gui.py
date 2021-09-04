# sys.path.append('../..')

from collections import OrderedDict

# gui.GUIComponent
# import bge
import bgui
import bgui.bge_utils

# So we can find the bgui module

class SimpleLayout(bgui.bge_utils.Layout):
    """A layout showcasing various Bgui features"""

    def __init__(self, sys, data):
        super().__init__(sys, data)

        # Use a frame to store all of our widgets
        self.frame = bgui.Frame(self, border=0)
        self.frame.colors = [(0, 0, 0, 0) for i in range(4)]

        # A Label widget
        self.lbl = bgui.Label(self.frame, text='I sure wish someone would push that button...',
                pt_size=70, pos=[0, 0.7], options=bgui.BGUI_CENTERX)

        # A FrameButton widget
        self.btn = bgui.FrameButton(self.frame, text='Click Me!', size=[0.3, 0.1], pos=[0, 0.4],
                options=bgui.BGUI_CENTERX)

# def main(cont):
#     own = cont.owner
#     mouse = bge.logic.mouse

#     if 'sys' not in own:
#         # Create our system and show the mouse
#         own['sys'] = bgui.bge_utils.System('../../themes/default')
#         own['sys'].load_layout(SimpleLayout, None)
#         mouse.visible = True
#     else:
#         own['sys'].run()

class GUIComponent(bge.types.KX_PythonComponent):
    # Put your arguments here of the format ("key", default_value).
    # These values are exposed to the UI.
    args = OrderedDict([
    ])

    def start(self, args):
        self.sys = bgui.bge_utils.System('../../../themes/default')
        self.sys.load_layout(SimpleLayout, None)

    def update(self):
        # Put your code executed every logic step here.
        # self.object is the owner object of this component.
        # self.object.scene is the main scene.
        pass
