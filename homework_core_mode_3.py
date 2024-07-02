from datetime import datetime

def get_days_from_today(date):
    try
        date_transformation = datetime.strptime(date, "%Y-%m-%d")
        today = datetime.today()
        difference = today - date_transformation
        return difference.days
    except ValueError:
        return "Невірний фортат дати. 'Введіть РРРР-мм-дд'"
date = "2024-06-19"
print(get_days_from_today(date))