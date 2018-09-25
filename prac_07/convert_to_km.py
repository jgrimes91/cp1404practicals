from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class ConvertToKmApp(App):
    def build(self):
        self.title = "Convert miles to kilometres"
        self.root = Builder.load_file('convert_to_km.kv')
        return self.root

    def get_validated_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0

    def handle_increment(self, change):
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.calculate()

    def calculate(self):
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)


ConvertToKmApp().run()
