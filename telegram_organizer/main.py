"""Подключение к личному аккаунту Telegram через Telethon."""

import asyncio
from pathlib import Path

from telethon import TelegramClient

from config import API_HASH, API_ID, PHONE

# Сессия всегда создаётся рядом со скриптом: organizer_session.session
SESSION = Path(__file__).resolve().parent / "organizer_session"


def _display_name(user) -> str:
    """Собирает имя пользователя из полей, которые реально отдаёт Telegram."""
    full_name = " ".join(
        part for part in (user.first_name, user.last_name) if part
    ).strip()
    if full_name:
        return full_name
    if user.username:
        return user.username
    return "без имени"


async def main() -> None:
    """Авторизуется в личном аккаунте и печатает имя пользователя."""
    client = TelegramClient(str(SESSION), API_ID, API_HASH)
    try:
        # start() сам подключается и, если сессии ещё нет, запрашивает код из Telegram.
        await client.start(phone=PHONE)
        me = await client.get_me()
        print(f"Подключение успешно. Пользователь: {_display_name(me)}")
    finally:
        # disconnect() сохраняет сессию и закрывает соединение.
        await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
