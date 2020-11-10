from data.discord_meeting import DiscordMeeting
from data.gymnasium_meeting import GymnasiumMeeting
from data.request_meeting import RequestMeeting
from data.zoom_meeting import ZoomMeeting

ALGEBRA = ZoomMeeting("Алгебра", "7266529370", "k4WJH3")
BIOLOGY = ZoomMeeting("Биология", "9105234849", "L2tuUHVkSjVwMGdpWEpsemRjL3JPZz09")
CHEMISTRY = GymnasiumMeeting("Химия", 25)
COMPUTER_SCIENCE = RequestMeeting("Информатика",
                                  "https://teaching.lozhnikov.org/b/and-mmz-kwm-ka5",
                                  data={'/b/and-mmz-kwm-ka5[join_name]': '123'},
                                  soup_parse="a['href']",
                                  status_code=302,
                                  allow_redirects=False)
COMPUTER_SCIENCE_MODULE = DiscordMeeting("Модуль по информатике", "580678871066738689", "690507823234285589")
ENGLISH = ZoomMeeting("Английский язык", "79076606653", "1304")
GEOGRAPHY = DiscordMeeting("География", "750356917469053159", "750356917469053164")
GEOMETRY = ZoomMeeting("Геометрия", "7266529370", "k4WJH3")
GERMAN = ZoomMeeting("Немецкий", "4781164535", "7Qm12U")
HISTORY = ZoomMeeting("История", "2362162973", "241617")
LITERATURE = ZoomMeeting("Литература", "4644708335", "565505")
PHYSICAL_EDUCATION = ZoomMeeting("Физкультура", "5254109489", "830384")
PHYSICS = GymnasiumMeeting("Физика", 51)
RUSSIAN = ZoomMeeting("Русский", "9930162561", "631566")
SOCIAL_STUDIES = ZoomMeeting("Обществознание", "83487519411", "720198")
