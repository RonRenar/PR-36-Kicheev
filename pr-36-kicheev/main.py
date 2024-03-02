from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class CalculatorApp(App):
    def build(self):
        self.expression = ""
        self.prev_result = 0
        layout = GridLayout(cols=4)

        self.label = Label(text='0', font_size=40, size_hint=(1, 0.5))
        layout.add_widget(self.label)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '.', '0', '=', '+',
            'C', 'CE'
        ]

        for button in buttons:
            btn = Button(text=button, font_size=40)
            btn.bind(on_press=self.on_button_press)
            layout.add_widget(btn)

        return layout

    def on_button_press(self, instance):
        if instance.text == '=':
            try:
                result = str(eval(self.expression))
                self.label.text = result
                self.prev_result = float(result)
            except Exception as e:
                self.label.text = "Error"
            self.expression = ""

        elif instance.text == 'C':
            self.expression = ""
            self.prev_result = 0
            self.label.text = "0"

        elif instance.text == 'CE':
            self.expression = self.expression[:-1]
            self.label.text = self.expression

        else:
            self.expression += instance.text
            self.label.text = self.expression


if __name__ == '__main__':
    CalculatorApp().run()
