"""Загрузка настроек Telegram API из файла .env."""

import os
from pathlib import Path

from dotenv import load_dotenv

# Ищем .env рядом с этим модулем, а не в текущей рабочей папке.
ENV_PATH = Path(__file__).resolve().parent / ".env"
load_dotenv(ENV_PATH)


def _require(name: str) -> str:
    """Возвращает обязательную переменную окружения или завершает запуск с пояснением."""
    value = os.getenv(name, "").strip()
    if not value:
        raise RuntimeError(
            f"Переменная {name} не задана. Создайте файл .env по инструкции из README.md."
        )
    return value


_api_id_raw = _require("API_ID")
try:
    API_ID = int(_api_id_raw)
except ValueError as exc:
    raise RuntimeError("API_ID должен быть целым числом из my.telegram.org.") from exc

if API_ID <= 0:
    raise RuntimeError("API_ID должен быть положительным числом.")

API_HASH = _require("API_HASH")
PHONE = _require("PHONE")
