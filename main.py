from kivy.app import App
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
import csv
import random
import os

# ✅ Register Korean-friendly font
LabelBase.register(name="KoreanFont", fn_regular="NotoSansKR-VariableFont_wght.ttf")


class ModeSelectScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        layout.add_widget(Label(text="💖 장르를 선택하세요:", font_size=24, font_name="KoreanFont"))

        btn_romance = Button(text="로맨스", size_hint_y=None, height=50, font_name="KoreanFont",
                             on_press=self.choose_romance)
        btn_bl = Button(text="BL", size_hint_y=None, height=50, font_name="KoreanFont",
                        on_press=self.choose_bl)

        layout.add_widget(btn_romance)
        layout.add_widget(btn_bl)
        self.add_widget(layout)

    def choose_romance(self, *args):
        self.manager.get_screen('randomizer').set_mode('romance')
        self.manager.current = 'randomizer'

    def choose_bl(self, *args):
        self.manager.get_screen('randomizer').set_mode('bl')
        self.manager.current = 'randomizer'


class RandomizerScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mode = None
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        self.add_widget(self.layout)

        # Widgets we keep reusing
        self.back_btn = Button(
            text="🔙 장르 선택으로 돌아가기",
            size_hint_y=None,
            height=50,
            font_name="KoreanFont",
            on_press=self.go_back
        )

        self.generate_btn = Button(
            text="🔁 키워드 생성",
            size_hint_y=None,
            height=50,
            font_name="KoreanFont",
            on_press=self.generate_prompt
        )

        self.output_label = Label(text="", size_hint_y=None, font_name="KoreanFont")
        self.scroll = ScrollView(size_hint=(1, 0.5))
        self.scroll.add_widget(self.output_label)

    def set_mode(self, mode):
        self.mode = mode
        self.layout.clear_widgets()
        self.spinners = {}

        # 🔄 Clear previous result
        self.output_label.text = ""

        # ✅ First widget should be the back button
        self.layout.add_widget(self.back_btn)

        # Set category list
        if mode == 'romance':
            self.categories = [
                ('로맨스 장르', 'Romance_Genre.csv'),
                ('남주', 'Namju.csv'),
                ('여주', 'Yeoju.csv')
            ]
        else:
            self.categories = [
                ('BL 장르', 'BL_Genre.csv'),
                ('공', 'Gong.csv'),
                ('수', 'Soo.csv')
            ]

        # Spinner instructions
        self.layout.add_widget(Label(
            text="🎯 각 항목에서 뽑을 키워드 수를 선택하세요 (0~6):",
            font_size=18,
            font_name="KoreanFont"
        ))

        # Add spinner rows
        for label, file in self.categories:
            row = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
            row.add_widget(Label(text=label, size_hint_x=0.5, font_name="KoreanFont"))
            spinner = Spinner(text='0', values=[str(i) for i in range(7)],
                              size_hint_x=0.5, font_name="KoreanFont")
            row.add_widget(spinner)
            self.spinners[file] = spinner
            self.layout.add_widget(row)

        self.layout.add_widget(self.generate_btn)
        self.layout.add_widget(self.scroll)

    def load_csv(self, filename):
        path = os.path.join(os.getcwd(), filename)
        try:
            with open(path, newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader)  # Skip header
                return [row[0].strip() for row in reader if row and row[0].strip()]
        except Exception as e:
            return [f"(Error loading {filename})"]

    def generate_prompt(self, *args):
        output = ""
        for label, file in self.categories:
            count = int(self.spinners[file].text)
            entries = self.load_csv(file)
            selected = random.sample(entries, min(count, len(entries)))
            output += f"{label}:\n" + ', '.join(selected) + "\n\n"

        self.output_label.text = output

    def go_back(self, *args):
        self.manager.current = 'mode'


class RandomizerApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ModeSelectScreen(name='mode'))
        sm.add_widget(RandomizerScreen(name='randomizer'))
        return sm


if __name__ == '__main__':
    RandomizerApp().run()
