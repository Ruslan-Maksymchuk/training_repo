from datetime import datetime

def get_days_from_today(date):
    date_transformation = datetime.strptime(date, "%Y-%m-%d")
    today = datetime.today()
    difference = today - date_transformation
    return difference.days
date = "2024-06-20"
print(get_days_from_today(date))
