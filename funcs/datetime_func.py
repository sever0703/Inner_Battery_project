import datetime


def get_welcome() -> str:
    current_time = datetime.datetime.now()
    if 0 <= current_time.hour < 6:
        return "Добро пожаловать, полуночник!🌃\n*Нажимай на кнопку ниже, если мотивацию надо подняяяять)*\n\n" \
               "/motivate_me"
    if 6 <= current_time.hour < 12:
        return "С добрым утром, самурай!☕️\n*Нажимай на кнопку ниже, если мотивацию надо подняяяять)*\n\n" \
               "/motivate_me"
    if 12 <= current_time.hour < 18:
        return "Добрый день! Вперед за новыми свершениями!💪\n*Нажимай на кнопку ниже, если мотивацию надо подняяяять)*\n\n" \
               "/motivate_me"
    else:
        return "Добрый вечер! Вперед за порцией вдохновения!📚\n*Нажимай на кнопку ниже)*\n\n" \
               "/motivate_me"
