from datetime import datetime, timedelta

def get_last_month():
    today = datetime.today()
    first_day_of_this_month = today.replace(day=1)
    last_month = first_day_of_this_month - timedelta(days=1)
    return last_month.year, last_month.month