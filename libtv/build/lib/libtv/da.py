import datetime

da_today_is_weekday()
    # Get today's date
    today = datetime.date.today()

    # Check if today is a weekday (0-4: Monday to Friday)
    is_weekday = today.weekday() < 5

    return(is_weekday)
