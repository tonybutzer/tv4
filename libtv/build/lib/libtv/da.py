#import datetime
from datetime import datetime, timezone, timedelta, date
import pytz


def da_today_is_weekday():
    # Get today's date
    today = date.today()

    # Check if today is a weekday (0-4: Monday to Friday)
    is_weekday = today.weekday() < 5

    return(is_weekday)

def da_today_date_str():
    today = date.today()
    date_obj = today
    # Extract year, month, and day
    year = date_obj.year
    month = date_obj.month
    day = date_obj.day
    date_str = f'{year}{month}{day}'
    return(date_str)


def da_convert_gmt_local(date, time):
    mytime = f"{date} {time} GMT"
    dtobj = datetime.strptime(mytime, '%Y%m%d %H:%M %Z')
    dtobj = dtobj.replace(tzinfo=timezone.utc)
    #dtobj = dtobj.astimezone(ZoneInfo('US/Central')) - breaks when its CDT
    dtobj = dtobj.astimezone()
    a = dtobj
    # print(a.strftime('%Y%m%d%H%M'))
    return(a.strftime('%Y%m%d%H%M'))

def da_convert_gmt_local_time(date, time):
    mytime = f"{date} {time} GMT"
    dtobj = datetime.strptime(mytime, '%Y%m%d %H:%M %Z')
    dtobj = dtobj.replace(tzinfo=timezone.utc)
    #dtobj = dtobj.astimezone(ZoneInfo('US/Central')) - breaks when its CDT
    dtobj = dtobj.astimezone()
    a = dtobj
    # print(a.strftime('%Y%m%d%H%M'))
    return(a.strftime('%H:%M'))


def da_convert_gmt_local_date(date, time):
    mytime = f"{date} {time} GMT"
    dtobj = datetime.strptime(mytime, '%Y%m%d %H:%M %Z')
    dtobj = dtobj.replace(tzinfo=timezone.utc)
    #dtobj = dtobj.astimezone(ZoneInfo('US/Central')) - breaks when its CDT
    dtobj = dtobj.astimezone()
    a = dtobj
    # print(a.strftime('%Y%m%d%H%M'))
    return(a.strftime('%Y%m%d'))

def da_convert_local_gmt_date(date, time):
    central = pytz.timezone('US/Central')
    gmt = pytz.timezone('GMT')
    # Example datetime in Central Time
    mytime = f"{date} {time}"

    central_time = central.localize(datetime.strptime(mytime, '%Y%m%d %H:%M'))

    # Convert to GMT
    gmt_time = central_time.astimezone(gmt)

    #print("Central Time:", central_time)
    #print("GMT:", gmt_time)
    gm = gmt_time
    dt_str = f'{gm.year}{gm.month}{gm.day}'
    #print(dt_str)
    return(dt_str)


# Function to check if the given date is the same day of the week as today
def da_is_same_day_of_week(date_str):
    date_obj = datetime.strptime(date_str, "%Y%m%d")
    today = datetime.now()
    return date_obj.weekday() == today.weekday()


