import typing as tp
from dataclasses import dataclass


@dataclass
class TelegramPost:
    title: str
    url: str
    description: tp.Optional[str]

    def as_telegram_message(self) -> str:
        title = self.title
        description = ""
        if self.description is not None:
            description = self.description + "\n"
        url = self.url
        return f"{title}\n\n{description}\n{url}"
