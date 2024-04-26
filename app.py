from kivy.lang import Builder
from kivymd.app import MDApp

from kivy.properties import StringProperty
from kivymd.uix.card import MDCard

from kivy.core.window import Window

Window.size = (1500, 900)


KV = '''
<CourseCard>
    padding: "10dp"
    size_hint: None, None
    size: "240dp", "100dp"
    MDRelativeLayout:
        MDLabel:
            text: root.text
            adaptive_size: True
            color: "grey"
            pos_hint: {"top": 1, "left": 1}
            padding: "5dp"
            bold: True
        MDButton:
            style: "filled"
            pos_hint: {"bottom": 1, "right": 1}
            MDButtonText:
                text: root.btn_text

MDScreen:
    md_bg_color: self.theme_cls.backgroundColor
    MDTopAppBar:
        type: "small"
        pos_hint: {"top": 1}
        MDTopAppBarLeadingButtonContainer:
            MDButton:
                style: "text"
                MDButtonText:
                    text: "Overview"
            MDButton:
                style: "text"
                MDButtonText:
                    text: "Schedule"
            MDButton:
                style: "text"
                MDButtonText:
                    text: "Study plan"
        MDTopAppBarTitle:
            text: " "
        MDTopAppBarTrailingButtonContainer:
            MDIconButton:
                icon: "account-circle-outline"
                style: "filled"
    MDGridLayout:
        id: container
        pos_hint: {"top": 0.9}
        padding: "30dp"
        adaptive_height: True
        cols: 1
        spacing: "20dp"
        MDLabel:
            text: "Active courses"
        MDGridLayout:
            id: active_courses
            adaptive_height: True
            cols: 4
            spacing: "14dp"
        MDLabel:
            text: ""
        MDLabel:
            text: ""
        MDLabel:
            text: "Exams"
        MDGridLayout:
            id: exams
            adaptive_height: True
            cols: 4
            spacing: "14dp"
        MDLabel:
            text: ""
        MDLabel:
            text: ""
        MDLabel:
            text: "Upcoming courses"
        MDGridLayout:
            id: upcoming_courses
            adaptive_height: True
            cols: 4
            spacing: "14dp"
'''

class CourseCard(MDCard):
    text = StringProperty()
    btn_text = StringProperty()

class App(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Darkgrey"
        return Builder.load_string(KV)
    
    def on_start(self):
        for i in range(5):
            self.root.ids.active_courses.add_widget(
                CourseCard(style="elevated", text=f"Course {i}", btn_text="View")
            )
        for i in range(3):
            if i == 0:
                self.root.ids.exams.add_widget(
                    CourseCard(style="elevated", text=f"Exam {i}", btn_text="Register")
                )
            else:
                self.root.ids.exams.add_widget(
                    CourseCard(style="filled", text=f"Exam {i}", btn_text="Unregister")
                )
        for i in range(5):
            if i <= 1:
                self.root.ids.upcoming_courses.add_widget(
                    CourseCard(style="elevated", text=f"Course {i}", btn_text="Enroll")
                )
            else:
                self.root.ids.upcoming_courses.add_widget(
                    CourseCard(style="filled", text=f"Course {i}", btn_text="Unenroll")
                )

if __name__ == '__main__':
    App().run()