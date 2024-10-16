#!/usr/bin/env python
# coding: utf-8

from classes import TITAN, get_files_titan_xml, uniquify, state_record_todo

short_list = state_record_todo() # sets up xml files in queue

my_programs = short_list

p = my_programs[0]

t = TITAN(p)

# # titan recorder

video_dir = '/home/tony/tv/video'
my_title = t.title()
mpg_file = f'{video_dir}/{my_title}.mpg'


import subprocess

def schedule_record(program_xml, time_str):
    cmd=f'echo ./tr.sh  {program_xml}| at -t {time_str}'
    mycmd=subprocess.getoutput(cmd)
    print(mycmd)


for p in my_programs:
    print(p)
    t = TITAN(p)
    start_time = t.start_time()
    print(start_time)
    schedule_record(p, start_time)

for p in my_programs:
    print(p)
    t=TITAN(p)
    print(t.duration())


