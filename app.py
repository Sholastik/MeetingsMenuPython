from datetime import date

from rumps import App, MenuItem, alert, quit_application

from data.meeting import Meeting
from db.schedule import SCHEDULE
from exceptions.MeetingException import MeetingException


class MeetingMenuItem(MenuItem):
    def __init__(self, number: int, meeting: Meeting) -> None:
        super().__init__(title=f"{number}. {meeting}", callback=self.open)
        self.number = number
        self.meeting = meeting

    def open(self, sender: MenuItem) -> None:
        try:
            self.meeting.open()
        except MeetingException as e:
            if alert("Возникла ошибка", str(e), ok="Закрыть", cancel="Повторить", icon_path="icon.png") == 0:
                self.open(sender)


class MeetingsApp(App):
    def __init__(self) -> None:
        super().__init__("MeetingMenu", icon="icon.png", template=True, quit_button=None)
        self.add_items()

    def add_items(self):
        self.menu.clear()
        for index, item in enumerate(SCHEDULE[date.today().weekday()], start=1):
            if item is not None:
                self.menu.add(MeetingMenuItem(index, item))
        self.menu.add(MenuItem("Обновить", callback=lambda x: self.add_items()))
        self.menu.add(MenuItem("Закрыть", callback=quit_application))


if __name__ == '__main__':
    MeetingsApp().run()
