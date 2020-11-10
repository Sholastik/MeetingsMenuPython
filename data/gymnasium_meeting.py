from requests import get, codes

from data.meeting import Meeting
from exceptions.MeetingException import MeetingException

TOKEN = "r84ef682FIMcGygw6pVtLp6pDKmqfty5MIaTyf00xxI5P5v6MWKDYIqhVBrTfTHq"
HEADERS = {"Authorization": f"Bearer {TOKEN}"}


class GymnasiumMeeting(Meeting):
    def __init__(self, title: str, group: int) -> None:
        super().__init__(title, None)
        self.pattern = f"https://gymnasium.msu.ru/groups/{group}/conferences/{'{id}'}/join"
        self.group = group

    def open(self) -> None:
        response = get(
            f"https://gymnasium.msu.ru/api/v1/groups/{self.group}/conferences",
            headers=HEADERS
        )

        if response.status_code == codes.ok:
            try:
                meetings = response.json()['conferences']

                if len(meetings) == 0:
                    raise MeetingException("Конференции нет")

                meeting = meetings[0]
                id = meeting['id']

                if meeting['ended_at'] is not None:
                    raise MeetingException("Конференции нет")

                if meeting['started_at'] is None:
                    raise MeetingException("Конференция не началась")

                self.link = self.pattern.format(id=id)
                super().open()

            except Exception as e:
                if isinstance(e, MeetingException):
                    raise e
                raise MeetingException("Не получилось открыть конференцию", e, *e.args, response.text)
        else:
            raise MeetingException("Не получилось открыть конференцию", response.status_code, response.text)
