from data.meeting import Meeting


class DiscordMeeting(Meeting):
    def __init__(self, title: str, server_id: str, channel_id: str) -> None:
        super().__init__(title, f"discord://discordapp.com/channels/{server_id}/{channel_id}")