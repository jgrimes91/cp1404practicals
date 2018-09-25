from kivy.app import App
from kivy.lang import Builder



class ConvertToKmApp(App):
    def build(self):
        self.title = "Convert miles to kilometres"
        self.root = Builder.load_file('convert_to_km.kv')
        return self.root



ConvertToKmApp().run()