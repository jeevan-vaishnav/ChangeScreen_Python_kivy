from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager


class HomeScreen(Screen):
    pass


class FirstScreen(Screen):
    pass


class Manager(ScreenManager):
    pass


class MyApp(App):
    pass


if __name__ == "__main__":
    MyApp().run()
