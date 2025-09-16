import datetime

def mood_advisor():
    now = datetime.datetime.now()
    hour = now.hour
    weekday = now.weekday()  # 0=Пн, 6=Вс

    if weekday >= 5:  # выходные
        mood = "расслабленный 🛌"
    elif 9 <= hour < 18:
        mood = "рабочий муравей 🐜"
    elif hour < 7:
        mood = "совсем ещё спишь? 🌙"
    else:
        mood = "уже мечтаешь о диване 🛋️"

    print(f"Сегодня ты — {mood}. Прими это.")

mood_advisor()
