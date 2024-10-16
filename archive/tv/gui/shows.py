import xmltodict
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
from subprocess import check_output

def convert_gmt_local(date, time):
    mytime = f"{date} {time} GMT"
    dtobj = datetime.strptime(mytime, '%Y%m%d %H:%M %Z')
    dtobj = dtobj.replace(tzinfo=timezone.utc)
    dtobj = dtobj.astimezone(ZoneInfo('US/Central'))
    a = dtobj
    # print(a.strftime('%Y%m%d%H%M'))
    return(a.strftime('%Y-%m-%d %a %I%M%p'))

p2 = check_output(["atq", "-q", "a"]).decode("utf-8") 

print(p2)

job = p2.split()[0]

print(job)


cmd = ["at", "-c", job]

details = check_output(cmd).decode("utf-8")

at_item = details.split('\n')[-3]

print(at_item)

the_file = at_item.split()[-1]

print(the_file)


with open(the_file) as fd:
    doc = xmltodict.parse(fd.read())

print(doc)

sd = doc['tv-program-info']['program']['start-date']
st =  doc['tv-program-info']['program']['start-time']
rec_time = convert_gmt_local(sd,st) 

print(rec_time)
