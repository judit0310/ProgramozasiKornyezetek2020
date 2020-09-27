from kivy.uix.button import Button
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.widget import Widget


class ExampleViewer(RecycleView):
    def __init__(self,**kwargs):
        super(ExampleViewer, self).__init__(**kwargs)

class RVItem(Button):
    def get_data_index(self):
        return self.parent.get_view_index_at(self.center)
    def on_press(self):
        print(self.get_data_index())


Builder.load_string('''

<ExampleViewer>: 
    viewclass: 'RVItem'
    id:rv
    orientation: "vertical"
    spacing: 40
    padding:10, 10
    space_x: self.size[0]/3
    RecycleBoxLayout: 
        color:(0, 0.7, 0.4, 0.8) 
        default_size: None, dp(56) 
        # defines the size of the widget in reference to width and height 
        default_size_hint: 1, None 
        size_hint_y: None
        height: self.minimum_height 
        orientation: 'vertical' # defines the orientation of data items 

''')