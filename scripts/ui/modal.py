import bge
from collections import OrderedDict
from mathutils import Vector

class ModalComponent(bge.types.KX_PythonComponent):
    args = OrderedDict([
        ('Tamanho Modal', 10.0),
        ('Tamanho Button', 9.0),
        ('Tamanho Texto', 0.0),
        ('Active', True)
    ])

    def start(self, args):
        # Biding args
        self.size_modal = args["Tamanho Modal"]
        self.size_button = args["Tamanho Button"]
        self.size_text = args["Tamanho Texto"]
        self.active = args["Active"]
        
        # components widgets
        self.button = self.object.childrenRecursive["button"]
        self.texto = self.object.childrenRecursive["texto"]
        self.texto.color = Vector([0.411, 0.411, 0.411, 1])


    def __set_position_text(self):
        # Align LEFT
        difer = (self.size_modal - self.size_text) / 2
        position = -10 + difer
        self.texto.worldPosition = Vector([position, 0, 5])

    def __set_position_button(self):
        # Align LEFT
        difer = (self.size_modal - self.size_button) / 2
        position = -10 + difer
        self.button.worldPosition = Vector([position, -2, 4])

    def update(self):
        self.show_modal()
    
    def show_modal(self):
        if self.active:
            self.__set_position_button()
            self.__set_position_text()
        else:
            self.object.visible = False
            for x in self.object.childrenRecursive:
                x.visible = False