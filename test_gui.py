import bge
from collections import OrderedDict
import bgui
import bgui.bge_utils
from bgui.widget import BGUI_CACHE, BGUI_CENTERED, BGUI_CENTERX, BGUI_CENTERY


class SimpleLayout(bgui.bge_utils.Layout):
    """A layout showcasing various Bgui features"""

    def __init__(self, sys, data):
        super().__init__(sys, data)


        self.frame = bgui.Frame(self, border=0)
        self.frame.colors = [(0, 0, 0, 0) for i in range(4)]

            

        
        self.frame_time = bgui.Frame(self, size=[0.2, 0.05], pos=[0, 0.04],
            options=bgui.BGUI_CENTERX)
        self.frame_time.colors = [(0, 0, 0, 0.3) for i in range(4)]

        self.lbl = bgui.Label(self.frame, text='Teste Augusto',
                              pt_size=25, options=bgui.BGUI_CENTERX,
                              pos=[0, 0.3])



class TestGUIComponent(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ])

    def start(self, args):
        self.sys = bgui.bge_utils.System('themes/default')
        self.sys.load_layout(SimpleLayout, None)

    def update(self):
        self.sys.run()
