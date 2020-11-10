from requests import post, codes

from data.meeting import Meeting
from bs4 import BeautifulSoup

from exceptions.MeetingException import MeetingException


class RequestMeeting(Meeting):
    def __init__(self, title: str, link: str, data: dict, soup_parse: str, status_code: int = codes.ok,
                 allow_redirects=True) -> None:
        super().__init__(title, None)
        self.request_link = link
        self.data = data
        self.soup_parse = soup_parse
        self.allow_redirects = allow_redirects
        self.status_code = status_code

    def open(self) -> None:
        response = post(self.request_link, data=self.data, allow_redirects=self.allow_redirects)
        if response.status_code == self.status_code:
            try:
                soup = BeautifulSoup(response.text, 'lxml')
                self.link = eval(f"soup.{self.soup_parse}")
                super().open()
            except Exception as e:
                raise MeetingException("Не получилось открыть конференцию", e, *e.args, response.text)
        else:
            raise MeetingException("Не получилось открыть конференцию", response.status_code, response.text)

# data = {
#
# }
#
# response = requests.post('', data=data, allow_redirects=False)
# soup = BeautifulSoup(response.text, 'lxml')
# print(soup.a['href'])
