import subprocess

def at_schedule_record(program_xml, time_str):
    cmd=f'echo ./tr.sh  {program_xml}| at -t {time_str}'
    mycmd=subprocess.getoutput(cmd)
    print(mycmd)

