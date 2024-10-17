#!/usr/bin/env python
# coding: utf-8



import sys, os, os.path
import subprocess
import signal, datetime
import logging
import heapq
from classes import TITAN_NOW, TITAN, CHANNEL, uniquify, state_recording

def rec_now(titan_file):
    
    global logfile
    logfile = 'recorder.log'
    FORMAT = "%(asctime)-15s: %(message)s"
    logging.basicConfig(level=logging.INFO, filename=logfile, filemode='w',
                        format=FORMAT)


    logging.info("Main process PID: %d, use this for sending SIGHUP "
                 "for re-reading the schedule-file", os.getpid())

    print("hello tony")  

    t=TITAN_NOW(titan_file)
    prog_name=t.title() + '_' + t.episode()

    
    basedir = '/home/tony/tv/video'
 
    now = datetime.datetime.now()

    start = now
    period = t.duration()
    if period > 60:
        period = period + 60

    print(f'period = {period}')

    # channel='21'
    # subchannel='4'

    c = CHANNEL()

    human_channel = t.human_channel()
    print(f'human = {human_channel}')

    channel, subchannel = c.phys(human_channel)
    print( channel, subchannel )

    jb = JOB(basedir, prog_name, start, period, channel, subchannel)
    state_recording(titan_file)
    
    jb.record()


def rec_main(titan_file):
    
    global logfile
    logfile = 'recorder.log'
    FORMAT = "%(asctime)-15s: %(message)s"
    logging.basicConfig(level=logging.INFO, filename=logfile, filemode='w',
                        format=FORMAT)


    logging.info("Main process PID: %d, use this for sending SIGHUP "
                 "for re-reading the schedule-file", os.getpid())

    print("hello tony")  

    t=TITAN(titan_file)
    prog_name=t.title() + '_' + t.episode()

    
    basedir = '/home/tony/tv/video'
 
    now = datetime.datetime.now()

    start = now
    period = t.duration()
    if period > 60:
        period = period + 60

    print(f'period = {period}')

    # channel='21'
    # subchannel='4'

    c = CHANNEL()

    human_channel = t.human_channel()
    print(f'human = {human_channel}')

    channel, subchannel = c.phys(human_channel)
    print( channel, subchannel )

    jb = JOB(basedir, prog_name, start, period, channel, subchannel)
    state_recording(titan_file)
    
    jb.record()
    

def sighup_handler(signum, frame):
    global reload_jobs
    logging.info("Received SIGHUP, reloading schedule-file")
    reload_jobs = True

def sigterm_handler(signum, frame):
    # TODO: Kill any recorder threads?
    logging.info("Received SIGTERM, shutting down")
    global shutdown
    shutdown = True

def schedule_jobs(sched, schedule_file, channelmap, media_dir):
    import shlex
    for line in open(schedule_file):
        try:
            (prog_name, start, period, vchannel, days) = shlex.split(line, True)
        except ValueError:
            if not line.strip() or line.strip().startswith('#'):
                continue    # Comment or a blank line
            else:
                logging.warning("Incorrect line:%s" % line) 
                continue

        FORMAT = "%Y-%m-%d %H:%M"
        start = datetime.datetime.strptime(start, FORMAT)
        if days == 'once' or days == '9': # FIXME compatibility issue
            repeat = False
        else:
            repeat = True
        (channel, subchannel) = channelmap[vchannel]
        period = int(period)
        job = JOB(media_dir, prog_name, start, period, channel, subchannel)

        if repeat:
            sched.add_cron_job(job.record, hour=start.hour,
                               minute=start.minute, second=0,
                               day_of_week=days, name=job.prog_name)
        else:
            # Don't schedule if it can never be run!
            now = datetime.datetime.now()
            if start > now:
                sched.add_cron_job(job.record, year=start.year,
                        month=start.month, day=start.day,
                        hour=start.hour, minute=start.minute,
                        second=0, name=job.prog_name)
import time
import yaml
from filelock import Timeout, FileLock

class TUNERS:
    def __init__(self):
        self._read_cfg()
        pass

    def _read_cfg(self):
        with open("tuners.yaml", "r") as stream:
            try:
                self.tuners = yaml.safe_load(stream)
                print(self.tuners)
            except yaml.YAMLError as exc:
                print(exc)


    def get_tuner(self):
#         self.lock.acquire()
#         try:
#             tuner = heapq.heappop(self.tuner_list)
#         except IndexError:
#             tuner = None
#         finally:
#             self.lock.release()
#         return tuner

        
        k=0
        for i in self.tuners:
            print(f'i={i}')
            lock_path = f'{i}.lock'
            self.lock = FileLock(lock_path, timeout=1)
            try:
                self.lock.acquire()
                device_id, tuner = self.tuners[k].split('-')
                print('NICE Lock for YOU!')
                return device_id, tuner, self.lock
            except Exception as e:
                print(e)
                print('No Lock for YOU!')
                k=k+1
                pass

        return '0', '0', self.lock


    def put_tuner(self, tuner, lock):
        lock.release()

class JOB:
    def __init__(self, basedir, prog_name, start, period, channel, subchannel):
        self.basedir = os.path.normpath(basedir)
        self.prog_name = prog_name
        self.start = start
        self.period = period
        # TODO: We should correct stripping at the source.
        self.channel = channel.strip()
        self.subchannel = subchannel.strip()

    def record(self):
#         tuner = tuners.get_tuner()
#         if tuner == None:
#             return
        device_id, tuner_num, lock = TUNERS().get_tuner()
        #device_id = '103AF69D'
        #tuner_num = 0

        with lock:
            self._record(device_id, tuner_num)


    def _record(self, device_id, tuner_num):
        import time
        import tempfile

        hdhomerun_config = '/usr/bin/hdhomerun_config'
        logging.info("Started recording %s on device: (%s, %s, %s:%s)" % (
                     self.prog_name, device_id, tuner_num,
                     self.channel, self.subchannel))
        now = datetime.datetime.now()
        date = now.strftime("%Y-%m-%d")
        dirname = self.basedir
        # dirname = os.path.join(self.basedir, self.prog_name)
        # if not os.path.exists(dirname):
            # os.makedirs(dirname)
        filename = os.path.join(dirname, f"{self.prog_name}__{date}.mpg")
        filename = uniquify(filename)
        cmd = [hdhomerun_config, device_id, "set"]
        cmd.extend(["/tuner%s/channel" % tuner_num, self.channel])
        subprocess.Popen(cmd).wait()

        cmd = [hdhomerun_config, device_id, "set"]
        cmd.extend(["/tuner%s/program" % tuner_num, self.subchannel])
        subprocess.Popen(cmd).wait()

        cmd = [hdhomerun_config, device_id, "save"]
        cmd.extend(["/tuner%s" % tuner_num, filename])
        f = tempfile.TemporaryFile("w+")
        p = subprocess.Popen(cmd, stdout=f, stderr=subprocess.STDOUT)

        # Record from now to the end of the program.
        now = datetime.datetime.now()
        td = (datetime.datetime.combine(now.date(), self.start.time()) +
              datetime.timedelta(minutes=self.period) - now)
        timeleft = td.days * 24 * 60 * 60 + td.seconds
        print(timeleft)
        time.sleep(timeleft)
        os.kill(p.pid, signal.SIGINT)
        p.wait()

        # Read the output from the save process
        f.seek(0)
        data = f.read()
        f.close()
        logging.info("Ended recording %s on device: (%s, %s, %s:%s), "
                     "status: %s" % (
                     self.prog_name, device_id, tuner_num,
    

                 self.channel, self.subchannel, data))



if __name__ == '__main__':
    rec_main()



