import sys
from datetime import date

from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem

from data.meeting import Meeting
from db.schedule import SCHEDULE
from exceptions.MeetingException import MeetingException


class MeetingListWidgetItem(QListWidgetItem):
    def __init__(self, number: int, meeting: Meeting) -> None:
        super().__init__(f"{number}. {meeting}")
        self.meeting = meeting

    def on_doubleclick(self) -> None:
        try:
            self.meeting.open()
        except MeetingException as e:
            print(e)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        weekday = date.today().weekday()

        self.setWindowTitle(f"Конференции")

        self.schedule_list = QListWidget(self)
        for index, item in enumerate(SCHEDULE[weekday], start=1):
            if item is not None:
                self.schedule_list.addItem(MeetingListWidgetItem(index, item))

        self.schedule_list.adjustSize()
        self.schedule_list.doubleClicked.connect(self.open_conference)

        self.setFixedSize(self.schedule_list.size())

    def open_conference(self) -> None:
        self.schedule_list.currentItem().on_doubleclick()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
