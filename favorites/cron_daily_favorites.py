#!/usr/bin/env python
# coding: utf-8

# # daily favorites cronjob
# 
# 1. run daily cron at 12:01 am
# 2. if its a weekday then add to todays schedule recordings

import os


from libtv.da import da_today_is_weekday, da_convert_gmt_local, da_today_date_str, da_convert_gmt_local_time, da_convert_local_gmt_date
from libtv.xm import xm_get_download_files, xm_get_favorite_files
from libtv.at import at_schedule_record
import xmltodict


print(da_today_is_weekday())



print(xm_get_favorite_files('.daily'))


prog_files = xm_get_favorite_files('.daily')


DAILY='/home/tony/tv/daily'
def record_me_today(fav, doc):
    today_date_str = da_today_date_str()
    start_date = doc['tv-program-info']['program']['start-date']
    time_str = doc['tv-program-info']['program']['start-time']
    at_time_str = da_convert_gmt_local(today_date_str, time_str)
    local_time_str = da_convert_gmt_local_time(start_date, time_str)
    print('AT',at_time_str)
    gmt_today_date_str = da_convert_local_gmt_date(today_date_str, local_time_str)
    print('hi', gmt_today_date_str, today_date_str, time_str)
    doc['tv-program-info']['program']['start-date'] = gmt_today_date_str
    doc['tv-program-info']['program']['end-date'] = gmt_today_date_str
    base_name = os.path.basename(fav)
    print(base_name)
    at_out_path = f'{DAILY}/{base_name}'
    xml_str = xmltodict.unparse(doc, pretty=True)
    with open(at_out_path, 'w') as file:
                file.write(xml_str)
    #print(xml_str)
    at_schedule_record(at_out_path, at_time_str)


for prog in prog_files:
    print(prog)
    
    with open(prog) as fd:
        doc = xmltodict.parse(fd.read())
        # print(doc)
        if da_today_is_weekday():
             record_me_today(prog, doc)
             print('record')
        else:
            print('not a WEEKDAY!')

