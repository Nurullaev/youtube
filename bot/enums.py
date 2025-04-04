from enum import Enum


class ErrorMessage(Enum):
    SIZE_LIMIT = "⚠️ К сожалению, из-за ограничений телеграма, мы не можем отправлять видео больше 50 мегабайт. Попытка выложить файл на filebin.net"
    GENERAL_ERROR = "⚠️ Произошла ошибка."
    MULTIPLE_VIDEOS_ERROR = "⚠️ Пожалуйста, подождите пока скачается прошлое видео и повторите снова."
    YT_DLP_ERROR = "⚠️ Видео могло не скачаться из-за особенностей хостинга."


class StatusMessage(Enum):
    PREPARING = "⏳ Файл подготавливается. Пожалуйста, подождите немного."
    PROMO = "Привет! Я <b>@NurVPNbot</b> — полностью бесплатный, без рекламы и обязательных подписок. Если тебе нравится моя работа, загляни на мой <b><a href='https://t.me/NurVPN_news'>телеграм канал</a></b> — это большая поддержка для меня! 😊\n\n<b>Это сообщение самоудалится через 10 секунд</b>"
    BOT_CAPTION = "<b>@NurVPNbot</b>"


class Links(Enum):
    YOUTUBE = [
        "https://www.youtube.com/",
        "https://youtu.be/",
        "https://www.youtube.com/shorts/",
        "https://youtube.com/shorts/",
    ]
    STANDART = [
        "https://www.tiktok.com/",
        "https://vt.tiktok.com/",
        "https://vm.tiktok.com/",
        "https://www.instagram.com/reel/",
        "https://instagram.com/reel/",
        "https://www.instagram.com/share/",
        "https://x.com/",
        "https://twitter.com/",
    ]
