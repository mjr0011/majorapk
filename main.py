from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.utils import get_color_from_hex


class CalculatorLayout(GridLayout):
    def __init__(self, **kwargs):
        super(CalculatorLayout, self).__init__(**kwargs)
        self.cols = 4
        self.spacing = [10, 10]
        self.padding = [20, 20, 20, 10]

        self.expression = TextInput(
            multiline=False,
            readonly=True,
            font_size="30sp",
            background_color=get_color_from_hex("#FFFFFF"),
            foreground_color=get_color_from_hex("#000000"),
        )
        self.add_widget(self.expression)

        self.add_widget(
            Button(
                text="7",
                on_release=self.button_pressed,
                background_color=get_color_from_hex("#000000"),
                background_normal="",
                font_size="30sp",
            )
        )
        self.add_widget(
            Button(
                text="8",
                on_release=self.button_pressed,
                background_color=get_color_from_hex("#000000"),
                background_normal="",
                font_size="30sp",
            )
        )
        self.add_widget(
            Button(
                text="9",
                on_release=self.button_pressed,
                background_color=get_color_from_hex("#000000"),
                background_normal="",
                font_size="30sp",
            )
        )
        self.add_widget(
            Button(
                text="/",
                on_release=self.button_pressed,
                background_color=get_color_from_hex("#4CAF50"),
                background_normal="",
                font_size="30sp",
            )
        )

        self.add_widget(
            Button(
                text="4",
                on_release=self.button_pressed,
                background_color=get_color_from_hex("#000000"),
                background_normal="",
                font_size="30sp",
            )
        )
        self.add_widget(
            Button(
                text="5",
                on_release=self.button_pressed,
                background_color=get_color_from_hex("#000000"),
                background_normal="",
                font_size="30sp",
            )
        )
        self.add_widget(
            Button(
                text="6",
                on_release=self.button_pressed,
                background_color=get_color_from_hex("#000000"),
                background_normal="",
                font_size="30sp",
            )
        )
        self.add_widget(
            Button(
                text="*",
                on_release=self.button_pressed,
                background_color=get_color_from_hex("#4CAF50"),
                background_normal="",
                font_size="30sp",
            )
        )

        self.add_widget(
            Button(
                text="1",
                on_release=self.button_pressed,
                background_color=get_color_from_hex("#000000"),
                background_normal="",
                font_size="30sp",
            )
        )
        self.add_widget(
            Button(
                text="2",
                on_release=self.button_pressed,
                background_color=get_color_from_hex("#000000"),
                background_normal="",
                font_size="30sp",
            )
        )
        self.add_widget(
            Button(
                text="3",
                on_release=self.button_pressed,
                background_color=get_color_from_hex("#000000"),
                background_normal="",
                font_size="30sp",
            )
        )
        self.add_widget(
            Button(
                text="-",
                on_release=self.button_pressed,
                background_color=get_color_from_hex("#4CAF50"),
                background_normal="",
                font_size="30sp",
            )
        )

        self.add_widget(
            Button(
                text="C",
                on_release=self.clear_expression,
                background_color=get_color_from_hex("#E53935"),
                background_normal="",
                font_size="30sp",
            )
        )
        self.add_widget(
            Button(
                text="0",
                on_release=self.button_pressed,
                background_color=get_color_from_hex("#000000"),
                background_normal="",
                font_size="30sp",
            )
        )
        self.add_widget(
            Button(
                text="=",
                on_release=self.calculate_expression,
                background_color=get_color_from_hex("#4CAF50"),
                background_normal="",
                font_size="30sp",
            )
        )
        self.add_widget(
            Button(
                text="+",
                on_release=self.button_pressed,
                background_color=get_color_from_hex("#4CAF50"),
                background_normal="",
                font_size="30sp",
            )
        )

    def button_pressed(self, instance):
        self.expression.text += instance.text

    def clear_expression(self, instance):
        self.expression.text = ""

    def calculate_expression(self, instance):
        try:
            result = eval(self.expression.text)
            self.expression.text = str(result)
        except ZeroDivisionError:
            self.expression.text = "Error: Division by zero"
        except Exception:
            self.expression.text = "Error: Invalid expression"


class ONAHApp(App):
    def build(self):
        self.icon="onahicon.png"
        Window.clearcolor = get_color_from_hex("#000000")
        return CalculatorLayout()


# Run the app
if __name__ == "__main__":
    ONAHApp().run()
