#!/usr/bin/env python
# coding: utf-8

# # weekly favorites
# run from cron - Makefil
# 

#DRY=True
DRY=False


import os


from libtv.da import da_today_is_weekday, da_convert_gmt_local, da_today_date_str, da_is_same_day_of_week
from libtv.da import da_convert_local_gmt_date, da_convert_gmt_local_date, da_convert_gmt_local_time
from libtv.xm import xm_get_download_files, xm_get_favorite_files
from libtv.at import at_schedule_record
from libtv.file import file_uniquify
import xmltodict


print(xm_get_favorite_files('.weekly'))


weekly_favs = xm_get_favorite_files('.weekly')

weekly_favs


WEEKLY='/home/tony/tv/weekly'
def record_me_today(fav, doc):
    today_date_str = da_today_date_str()
    start_date = doc['tv-program-info']['program']['start-date']
    time_str = doc['tv-program-info']['program']['start-time']
    at_time_str = da_convert_gmt_local(start_date, time_str)
    local_time_str = da_convert_gmt_local_time(start_date, time_str)
    print('AT',at_time_str)
    gmt_today_date_str = da_convert_local_gmt_date(today_date_str, local_time_str)
    print('hi', gmt_today_date_str, today_date_str, time_str)
    doc['tv-program-info']['program']['start-date'] = gmt_today_date_str
    doc['tv-program-info']['program']['end-date'] = gmt_today_date_str
    base_name = os.path.basename(fav)
    print(base_name)
    at_out_path = f'{WEEKLY}/{base_name}'
    xml_str = xmltodict.unparse(doc, pretty=True)
    with open(at_out_path, 'w') as file:
        file.write(xml_str)
    #print(xml_str)
    at_schedule_record(at_out_path, at_time_str)


for fav in weekly_favs:
    print(fav)
    with open(fav) as fd:
        doc = xmltodict.parse(fd.read())
        # print(doc)
        start_date = doc['tv-program-info']['program']['start-date']
        time_str = doc['tv-program-info']['program']['start-time']
        my_date = da_convert_gmt_local_date(start_date, time_str)
        print(start_date, my_date)
        print(da_is_same_day_of_week(my_date))
        if da_is_same_day_of_week(my_date):
            print(fav)
            if not DRY:
                record_me_today(fav, doc)
            else:
                print("DRY-RUN BABY!")




