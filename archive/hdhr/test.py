#!/usr/bin/env python3

from sys import exit
from pprint import pprint
from os import chdir

from hdhr.adapter import HdhrUtility, HdhrDeviceQuery
from hdhr.constants import MAP_US_CABLE

def find_devices():
    devices = HdhrUtility.discover_find_devices_custom()
    
    for device in devices:
        print("Found: %s" % (device))

    return devices

def set_tuner_vchannel(device_adapter, vchannel):
    
    device_adapter.set_tuner_vchannel(vchannel)

    (vstatus, raw_data) = device_adapter.get_tuner_vstatus()
    print(vstatus)

def set_stream(device_adapter, vchannel, target_uri):

    device_adapter.set_tuner_vchannel(vchannel)
    device_adapter.set_tuner_target(target_uri)

def get_supported(device_adapter):

    pprint(device_adapter.get_supported())

def scan(device_adapter):

    def found(result, scan_info):
        result.dump_programs()

    def progress_update(scan_info, progress):
        print("Progress: %.2f  Scanned= (%d)" % (progress, 
                                                 scan_info.scanned_channels))

    device_adapter.scan_channels(MAP_US_CABLE, found_cb=found, 
                                 incremental_cb=progress_update)

def get_count():

    return HdhrUtility.get_channels_in_range(MAP_US_CABLE)

devices = find_devices()

if not devices:
    print("Could not find any devices.")
    exit()

i = 0
for device in devices:
    print("%d: %s" % (i, device))

    hd = HdhrUtility.device_create_from_str(device.nice_device_id)
    device_adapter = HdhrDeviceQuery(hd)

    hw_model = device_adapter.get_hw_model_str()
    print("HW Model: %s" % (hw_model))

    model = device_adapter.get_model_str()
    print("Model: %s" % (model))

    version = device_adapter.get_version()
    print("Version: %s" % (version))

    features = device_adapter.get_supported()
    print("Features: %s" % (features))

    i += 1
    
print

for tuner in range(0, devices[0].tuner_count):
    first_device_str = ("%s-%d" % (devices[0].nice_device_id, tuner))

    hd = HdhrUtility.device_create_from_str(first_device_str)

    device_adapter = HdhrDeviceQuery(hd)

    (status, raw_data) = device_adapter.get_tuner_status()
    print("Status: %s" % (status))

    (vstatus, raw_data) = device_adapter.get_tuner_vstatus()
    print("Vstatus: %s" % (vstatus))

    streaminfo = device_adapter.get_tuner_streaminfo()
    print("Streaminfo: %s" % (streaminfo))

    program = device_adapter.get_tuner_program()
    print("Program: %s" % (program))

#device_adapter.set_tuner_vchannel(49)
#device_adapter.set_tuner_target('rtp://192.168.5.13:7891')
#device_adapter.set_tuner_target(None)

#get_supported(device_adapter)

#print get_count()

#scan(device_adapter)

print("Done.")
