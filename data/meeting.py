from os import system


class Meeting:
    def __init__(self, title: str, link: str) -> None:
        self.title = title
        self.link = link

    def open(self) -> None:
        system(f"open \"{self.link}\"")

    def __str__(self) -> str:
        return self.title
