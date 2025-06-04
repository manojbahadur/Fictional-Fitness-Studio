from pytz import timezone

def convert_to_timezone(dt, tz_name):
    ist = timezone("Asia/Kolkata")
    target = timezone(tz_name)
    dt_ist = ist.localize(dt)
    return dt_ist.astimezone(target)