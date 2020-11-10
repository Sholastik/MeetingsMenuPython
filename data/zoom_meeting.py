from data.meeting import Meeting


class ZoomMeeting(Meeting):
    def __init__(self, title: str, id: str, password: str) -> None:
        super().__init__(title, f"zoommtg://zoom.us/join?confno={id}&pwd={password}")
