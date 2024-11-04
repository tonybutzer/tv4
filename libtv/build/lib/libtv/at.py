import subprocess

RUNNER='/home/tony/opt/tv4/shell/at_record.sh'

def at_schedule_record(program_xml, time_str):
    cmd=f'echo {RUNNER} {program_xml}| at -t {time_str}'
    mycmd=subprocess.getoutput(cmd)
    print(mycmd)

